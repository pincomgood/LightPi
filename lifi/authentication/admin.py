from django.contrib import admin
from authentication.models import UserInfo, ModelInfo, ConnectInfo

admin.site.register(UserInfo)
admin.site.register(ModelInfo)
admin.site.register(ConnectInfo)
