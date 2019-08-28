from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserInfo, ModelInfo, ConnectInfo
from .serializers import UserInfoSerializer, ModelInfoSerializer, ConnectInfoSerializer


@api_view(['GET'])
def getModelList(request, userInfoLoginId):
    try:
        userInfoLoginId = UserInfo.objects.get(login_id=userInfoLoginId)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserInfoSerializer(userInfoLoginId)
        model_list = ConnectInfo.objects.filter(user_info_id=serializer.data['id'])
        temp = []
        for model in model_list.values():
            item = ModelInfo.objects.filter(id=model['model_info_id_id'])
            if model['connect_flag'] != 0:
                temp.append(item[0])
        result = ModelInfoSerializer(temp, many=True)
        return Response(result.data)


@api_view(['GET'])
def getModelKey(request, modelId):
    try:
        key = ModelInfo.objects.filter(id=modelId)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        result = ModelInfoSerializer(key.values()[0])
        print(result)
        return Response(result.data['key_value'])
