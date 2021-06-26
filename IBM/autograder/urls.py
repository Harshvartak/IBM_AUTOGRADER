from django.urls import path
from .views import *

urlpatterns = [
    path('essay',EssayGradeView.as_view(),name="Essay Grade"),
]