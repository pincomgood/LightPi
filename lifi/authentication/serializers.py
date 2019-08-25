from rest_framework import serializers
from .models import UserInfo, ModelInfo, ConnectInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'login_id', 'login_pw']


class ModelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelInfo
        fields = ['id', 'master_user_info_id_id', 'model_code', 'model_name', 'key_value']


class ConnectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectInfo
        fields = ['id', 'user_info_id', 'model_info_id', 'connect_flag']
