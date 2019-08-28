from django.db import models


class UserInfo(models.Model):
    login_id = models.CharField(max_length=100, default=None)
    login_pw = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.login_id


class ModelInfo(models.Model):
    master_user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    model_code = models.CharField(max_length=100, default=None)
    model_name = models.CharField(max_length=100, default=None)
    key_value = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.model_code


class ConnectInfo(models.Model):
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    model_info_id = models.ForeignKey(ModelInfo, on_delete=models.CASCADE)
    connect_flag = models.IntegerField(default=0)
