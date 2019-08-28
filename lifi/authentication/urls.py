from django.urls import path
from authentication import views

urlpatterns = [
    path('model/<str:userInfoLoginId>', views.getModelList),
    path('key/<int:modelId>', views.getModelKey),
]