from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView
    )

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from .serializers import (
    CourseSerializer,
    CourseDetailViewSerailizer,
    VideoSerializer,
    UpdateRatingsSerializer,
    )
from rest_framework.filters import (
    SearchFilter,


    )
from .models import Course,Video

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)


class GetListCourses(ListAPIView):
    """get all courses"""
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter]
    filter_fields = ['course_name']
    #http://example.com/api/users?search=russell


    def get_queryset(self, *args, **kwargs):

        #Example : http://127.0.0.1:8000/api/getAllCourses/?q=android
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Course.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(course_name__icontains=query)

                    ).distinct()
        return queryset_list
