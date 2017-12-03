from message.models import Message
from message.serializers import MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from message.helpers.dialogflow import query_dialogflow

class MessageView(APIView):
    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            r = query_dialogflow(serializer.data.get('text'))            
            json_response = r.json()
            response = json_response.get('result', {}).get("fulfillment", {}).get("speech", "Je n'ai pas compris...")              
            return Response({"speech_answer": response}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
