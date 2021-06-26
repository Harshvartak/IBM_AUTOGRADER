from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
import sys

def myfunc(text):
    print(text)
    score=0
    return score

# Create your views here.

class EssayGradeView(CreateAPIView):
    queryset=Essay
    serializer_class=EssaySerializer
    
    def post(self,request):
        try:
            print("HELLO")
            text=request.data['text']
            score=myfunc(text)
            request.data['score']=score
            serializer=self.get_serializer(data=request.data)              
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({'status':True,'score':score},status=status.HTTP_200_OK)
        except KeyError:
            return Response({'status':False,'message':str(sys.exc_info()[1]) + " is missing in request."},status=status.HTTP_200_OK)		
        except Exception as e:
            return Response({'status':False,'error':str(e)},status=status.HTTP_200_OK)		
        except ValueError:
            return Response({'ValueError':str(sys.exc_info()[1])},status=status.HTTP_200_OK)   
