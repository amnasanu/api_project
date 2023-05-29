from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InputData
from .serializer import InputDataSerializer

# Create your views here.




@api_view(['POST'])
def store_input_data(request):
    serializer = InputDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_input_data(request):
    input_data = InputData.objects.all()
    serializer = InputDataSerializer(input_data, many=True)
    return Response(serializer.data)
