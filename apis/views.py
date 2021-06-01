from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from grad import models
from .serializers import *


# Create your views here.

@api_view(['GET', ])
def api_parent_view(request, id):
    
    parent = models.Parent.objects.get(id=id)
    serializer = ParentSerializer(parent)
    return Response(serializer.data)

@api_view(['POST', ])
@csrf_exempt
def api_create_parent_view(request):
    
    parent = models.Parent()
    serializer = ParentSerializer(parent, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
@csrf_exempt
def api_update_parent_view(request, id):
    
    parent = models.Parent.objects.get(id=id)
    serializer = ParentSerializer(parent, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Update Successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def api_delete_parent_view(request, id):
    
    parent = models.Parent.objects.get(id=id)
    operation = parent.delete()
    data = {}
    if operation:
        data["success"] = "Delete Successful"
    else:
        data["failure"] = "Delete Failed"
    return Response(data=data)

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
def api_slot_view(request):
    
    slots = models.Slots.objects.all()
    serializer = SlotSerializer(slots, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def api_status_view(request, id):
    
    status = models.SpecialistActiveStatus.objects.get(specialist_id=id)
    serializer = StatusSerializer(status)
    return Response(serializer.data)
