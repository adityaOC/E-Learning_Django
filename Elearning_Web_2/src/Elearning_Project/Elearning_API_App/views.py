from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
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
from .models import (
    Course,
    Video,
    CourseRatings,
    )
from . import appConstants

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)


class GetListCourses(ListAPIView):
    """get all courses"""
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer


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

class CourseDetailView(RetrieveAPIView):
    """get single course"""

    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()

    serializer_class = CourseDetailViewSerailizer


class CourseUpdateView(UpdateAPIView):
    """update course, ratings"""
    permission_classes = [IsAuthenticated]
    queryset = CourseRatings.objects.all()
    serializer_class = UpdateRatingsSerializer
    serializer = UpdateRatingsSerializer()
    #course_id = serializer.data.get('id')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        rating_temp = request.POST.get("rating_give_by_user", None)

        if rating_temp and (float(rating_temp)>=0.0 and float(rating_temp)<=5.0):
            instance.total_number = instance.total_number + 1
            instance.sum_of_all_ratings =instance.sum_of_all_ratings + float(rating_temp)
            instance._ratings_tobeshown = instance.sum_of_all_ratings/instance.total_number
            instance.save()

        if rating_temp and (float(rating_temp)>=0.0 and float(rating_temp)<=5.0):
            return Response({'status': 1,'Message':'Success'})
        else:
            return Response({'status': 0,'Error':'Invalid request'})

class getAllVideoView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class HeroBannerAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all().order_by('-course_created_at')[:appConstants.HeroBanner_API_Fetch_Number]
    serializer_class = CourseSerializer
