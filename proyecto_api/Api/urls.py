from django.urls import path
from Api import views


urlpatterns = [
    path('helloworld/', views.HelloAPIView.as_view()),
]