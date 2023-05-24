from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("postapi/", views.LCSPostList.as_view()),
   
    path("postapi/<int:pk>", views.RUDPostAPI.as_view()),
    path('auth/', include("rest_framework.urls", namespace='rest_framework'))
    
]