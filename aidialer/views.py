from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import get_object_or_404

from APIENDPOINTS import fetch_all_transcripts

# from .serializers import CallSerializer, TranscriptSerializer

# @api_view(['POST'])
# def start_call(request):
#     serializer = CallSerializer(data=request.data)
#     if serializer.is_valid():
#         call = serializer.save()
#         # Simulate call initiation logic here
#         return Response({'call_sid': call.call_sid})
#     return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def end_call(request):
#     call_sid = request.data.get('call_sid')
#     call = get_object_or_404(Call, call_sid=call_sid)
#     call.status = 'ended'
#     call.save()
#     return Response({'status': 'Call ended'})

# @api_view(['GET'])
# def call_status(request, call_sid):
#     call = get_object_or_404(Call, call_sid=call_sid)
#     return Response({'status': call.status})

# @api_view(['GET'])
# def all_transcripts(request):
#     transcripts = Transcript.objects.all()
#     serializer = TranscriptSerializer(transcripts, many=True)
#     return Response({'transcripts': serializer.data})

# @api_view(['GET'])
# def transcript(request, call_sid):
#     call = get_object_or_404(Call, call_sid=call_sid)
#     transcripts = call.transcripts.all()
#     serializer = TranscriptSerializer(transcripts, many=True)
#     return Response({'transcript': serializer.data})


def ai_dialer_view(request):
    """
    View for fetching and displaying all transcripts in AiDialer.
    """
    # transcripts = fetch_all_transcripts()
    
    '''
    EXAMPLE RESPONSE:
    {'call_sid': 'CA72d2d7a52fc61e02e94bc840871cd493',
    'transcript': [{'role': 'user', 'content': 'Hello'},
    {'role': 'assistant',
    'content': 'I am an AI voice assistant here to answer any
    questions you may have. At any point during this call you 
    can say Transfer me which will transfer you to a live
    representative. Ask away!'},
    {'role': 'user', 'content': " Hey. What's the weather today?",
    'name': 'user'}, {'role': 'assistant', 'content': "Sure thing!
    Could you tell me which city you're in?"}, {'role': 'user', 
    'content': " I'm in Atlanta.", 'name': 'user'}, {'role': 'user',
    'content': " I'm in Atlanta. Thanks for your help.",
    'name': 'user'}]}
    '''
    transcripts = [{'call_sid': 'CA72d2d7a52fc61e02e94bc840871cd493',
    'transcript': [{'role': 'user', 'content': 'Hello'},
    {'role': 'assistant',
    'content': 'I am an AI voice assistant here to answer any \
    questions you may have. At any point during this call you \
    can say Transfer me which will transfer you to a live \
    representative. Ask away!'},
    {'role': 'user', 'content': " Hey. What's the weather today?",
    'name': 'user'}, {'role': 'assistant', 'content': "Sure thing! \
    Could you tell me which city you're in?"}, {'role': 'user', 
    'content': " I'm in Atlanta.", 'name': 'user'}, {'role': 'user',
    'content': " I'm in Atlanta. Thanks for your help.",
    'name': 'user'}]}, {'call_sid': 'numer 2',
    'transcript': [{'role': 'user', 'content': 'Hello'},
    {'role': 'assistant',
    'content': 'I am an AI voice assistant here to answer any \
    questions you may have. At any point during this call you \
    can say Transfer me which will transfer you to a live \
    representative. Ask away!'},
    {'role': 'user', 'content': " Hey. What's the weather today?",
    'name': 'user'}, {'role': 'assistant', 'content': "Sure thing! \
    Could you tell me which city you're in?"}, {'role': 'user', 
    'content': " I'm in Atlanta.", 'name': 'user'}, {'role': 'user',
    'content': " I'm in Atlanta. Thanks for your help.",
    'name': 'user'}]}]
    
    template_name = 'dashboard/pages/aidialer/aidialer_home.html'
    
    # Return the transcripts as JSON or pass them to a template
    return render(request, template_name, {'transcripts': transcripts})

def call_contact(request, call_sid):
    template_name = 'dashboard/pages/aidialer/aidialer_call.html'

    return render(request, template_name, {'message': f'call details form for sid: {call_sid}'})
