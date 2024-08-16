from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Call, Transcript
from .serializers import CallSerializer, TranscriptSerializer

@api_view(['POST'])
def start_call(request):
    serializer = CallSerializer(data=request.data)
    if serializer.is_valid():
        call = serializer.save()
        # Simulate call initiation logic here
        return Response({'call_sid': call.call_sid})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def end_call(request):
    call_sid = request.data.get('call_sid')
    call = get_object_or_404(Call, call_sid=call_sid)
    call.status = 'ended'
    call.save()
    return Response({'status': 'Call ended'})

@api_view(['GET'])
def call_status(request, call_sid):
    call = get_object_or_404(Call, call_sid=call_sid)
    return Response({'status': call.status})

@api_view(['GET'])
def all_transcripts(request):
    transcripts = Transcript.objects.all()
    serializer = TranscriptSerializer(transcripts, many=True)
    return Response({'transcripts': serializer.data})

@api_view(['GET'])
def transcript(request, call_sid):
    call = get_object_or_404(Call, call_sid=call_sid)
    transcripts = call.transcripts.all()
    serializer = TranscriptSerializer(transcripts, many=True)
    return Response({'transcript': serializer.data})