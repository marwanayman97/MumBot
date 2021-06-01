from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from grad import models
from .serializers import *


# Create your views here.

@api_view(['GET', ])
def api_parent_view(request, id):
    
    parent = models.Parent.objects.get(id=id)
    serializer = ParentSerializer(parent)
    return Response(serializer.data)

@api_view(['GET', ])
def api_specialist_view(request, id):
    
    specialist = models.Specialist.objects.get(id=id)
    serializer = SpecialistSerializer(specialist)
    return Response(serializer.data)

@api_view(['GET', ])
def api_inquiry_view(request, id):
    
    inquiry = models.SingleInquiry.objects.get(id=id)
    serializer = InquirySerializer(inquiry)
    return Response(serializer.data)

@api_view(['GET', ])
def api_video_view(request, id):
    
    video = models.VideoSession.objects.get(id=id)
    serializer = VideoSessionSerializer(video)
    return Response(serializer.data)

@api_view(['GET', ])
def api_question_view(request, id):
    
    question = models.Question.objects.get(id=id)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)

@api_view(['GET', ])
def api_answer_view(request, id):
    
    answer = models.Answer.objects.get(id=id)
    serializer = AnswerSerializer(answer)
    return Response(serializer.data)

@api_view(['GET', ])
def api_schedule_view(request, id):
    
    schedule = models.Schedules.objects.get(id=id)
    serializer = ScheduleSerializer(schedule)
    return Response(serializer.data)
