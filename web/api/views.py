

from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import GenericAPIView

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .mypaginations import MyPageNumberPagination
#from rest_framework.pagination import PageNumberPagination



from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# List and Create  - PK Not requierd
class LCSPostList(GenericAPIView, ListModelMixin, CreateModelMixin):
 queryset = Post.objects.all()
 serializer_class  = PostSerializer
 
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]
 #permission_classes = [IsAdminUser]
 
 
 filterset_fields = ['title']
 filter_backends = [DjangoFilterBackend]
 
 pagination_class = MyPageNumberPagination
 #pagination_class = PageNumberPagination
 
 
 
 def get(self, request, *args, **kwargs):
     return self.list(request, request, *args, **kwargs)
 
 

 
 def post(self, request, *args, **kwargs):
  return self.create(request,  *args, **kwargs)


# Retrive Update and Destroy -PK Reqired

class RUDPostAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
 queryset = Post.objects.all()
 serializer_class  = PostSerializer
 
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]
 
 #permission_classes = [IsAdminUser]
 
 filterset_fields = ['title']
 filter_backends = [DjangoFilterBackend]
 
 pagination_class = MyPageNumberPagination
 
 def get(self, request, *args, **kwargs):
  return self.retrieve(request,  *args, **kwargs)



 
 def put(self, request, *args, **kwargs):
  return self.update(request,  *args, **kwargs)



 
 def delete(self, request, *args, **kwargs):
  return self.destroy(request,  *args, **kwargs)