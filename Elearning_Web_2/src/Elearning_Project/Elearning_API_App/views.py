from django.shortcuts import render
from django.db.models import Q
from django.db.models import Sum
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
    UserProfileSerializer,
    VideoSerializer,
    UpdateRatingsSerializer,
    RatingBridgeSerializer,
    AuthorSerializer,


    )
from rest_framework.filters import (
    SearchFilter,


    )
from .models import (
    Course,
    Video,
    CourseRatings,
    Rating_Course_User_Bridge,
    StudentProfile,
    UserProfile,
    TeacherProfile,
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
    #serializer_class = ItemsSerializer


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

    #permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()

    serializer_class = CourseDetailViewSerailizer


class RatingUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Rating_Course_User_Bridge.objects.all()
    serializer_class = UpdateRatingsSerializer
    serializer = UpdateRatingsSerializer()

    def updateCourserRatings(self,courseID):
        #ItemPrice.objects.aggregate(Sum('price'))
        total_ratings = Rating_Course_User_Bridge.objects.filter(course_id=courseID).count()
        sum_of_all_ratings = Rating_Course_User_Bridge.objects.aggregate(Sum('rating_value'))
        return Response({'total_ratings': total_ratings,'sum_of_all_ratings':sum_of_all_ratings})

        course_avegrage_ratings = sum_of_all_ratings/total_ratings

        course_filter = Course.objects.filter(id=courseID).count()
        if course_filter > 0:
            course = Course.objects.get(id=courseID)
            course.course_avegrage_ratings = course_avegrage_ratings
            course.save()

    def update(self, request, *args, **kwargs):

        course_primaryKey = kwargs['pk']
        current_user_id = request.user.id


        instance_count=Rating_Course_User_Bridge.objects.filter(course_id=course_primaryKey,user_id = current_user_id).count()

        #return Response({'course_primaryKey': course_primaryKey,'current_user_id':current_user_id})
        if instance_count > 0:#if record already exist
             #return Response({'message': "record already exist"})
             instance = Rating_Course_User_Bridge.objects.get(course_id=course_primaryKey,user_id = current_user_id)

             #instance.rating_value = request.POST.get("rating_give_by_user", None)
             instance.rating_value = request.data['rating_give_by_user'];
             instance.save()

             total_ratings = Rating_Course_User_Bridge.objects.filter(course_id=course_primaryKey).count()
             sum_of_all_ratings= Rating_Course_User_Bridge.objects.filter(course_id=course_primaryKey).aggregate(Sum('rating_value'))

             course_avegrage_ratings = sum_of_all_ratings['rating_value__sum']/total_ratings
             course_filter = Course.objects.filter(id=course_primaryKey).count()

             if course_filter > 0:

                 course = Course.objects.get(id=course_primaryKey)
                 course.course_avegrage_ratings = course_avegrage_ratings
                 course.save()

             return Response({'status': 1,'Message':"Rating updated"})
        else:#if record does not exist then create it
             #return Response({'message': "create record else"})
             course = Course.objects.get(pk=course_primaryKey)
             course_count = Course.objects.filter(pk=course_primaryKey).count()

             user_count = UserProfile.objects.filter(pk=current_user_id).count()
             user = UserProfile.objects.get(pk=current_user_id)


             rating_Value = request.data['rating_give_by_user'];
             rating = Rating_Course_User_Bridge.objects.create(course=course,user=user,rating_value=rating_Value)

             #update course models
             total_ratings = Rating_Course_User_Bridge.objects.filter(course_id=course_primaryKey).count()
             sum_of_all_ratings= Rating_Course_User_Bridge.objects.filter(course_id=course_primaryKey).aggregate(Sum('rating_value'))

             course_avegrage_ratings = sum_of_all_ratings['rating_value__sum']/total_ratings
             course_filter = Course.objects.filter(id=course_primaryKey).count()
             if course_filter > 0:
                  course = Course.objects.get(id=course_primaryKey)
                  course.course_avegrage_ratings = course_avegrage_ratings
                  course.save()

             return Response({'status': 1,'rating.id':rating.id,'Message':"ratings created!"})
        #instance.save()




class getAllVideoView(ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class HeroBannerAPIView(ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Course.objects.all().order_by('-course_created_at')[:appConstants.HeroBanner_API_Fetch_Number]
    serializer_class = CourseSerializer


class getAllRatings(ListAPIView):
        queryset = Rating_Course_User_Bridge.objects.all()
        serializer_class = RatingBridgeSerializer


class UserRegistrationViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class getAllTeachers(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
