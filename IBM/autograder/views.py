from logging import raiseExceptions
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
import sys

from .autograder.autograder.t5_autograder import *
from .autograder.autograder.svm import *

def myfunc(text,ref_ans1,model1):
    score1=find_correctness(text,ref_ans1,model1)
    score2=find_correctness_svm(text,ref_ans1)
    avg_score=(score1+score2)/2
    if score1 == 5.0:
        return score1
    else:
        return avg_score


# Create your views here.

class EssayGradeView(CreateAPIView):
    queryset=Essay
    serializer_class=EssaySerializer
    
    def post(self,request):
        try:
            
            text=request.data['text']
            ref_ans1=request.data['ref_Ans1']
            score=myfunc(text,ref_ans1,model)
            
            request.data['score']=score
            serializer=self.get_serializer(data=request.data)
            #print(request.data['score'])
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({'status':True,'score':score},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_200_OK)
        except KeyError:
            return Response({'status':False,'message':str(sys.exc_info()[1]) + " is missing in request."},status=status.HTTP_200_OK)		
        except Exception as e:
            return Response({'status':False,'error':str(e)},status=status.HTTP_200_OK)		
        except ValueError:
            return Response({'ValueError':str(sys.exc_info()[1])},status=status.HTTP_200_OK)   
