from django.shortcuts import render
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,


    )
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

from .models import Course,Video
from .serializers import (
    CourseSerializer,
    CourseDetailViewSerailizer,
    VideoSerializer,
    UpdateRatingsSerializer,
    )
# Create your views here.

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


class CourseDetailView(RetrieveAPIView):
    """get single course"""

    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()

    serializer_class = CourseDetailViewSerailizer


class CourseUpdateView(UpdateAPIView):
    """update course, ratings"""
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = UpdateRatingsSerializer
    serializer = CourseSerializer()
    course_id = serializer.data.get('id')
"""
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        average =
        instance.course_ratings_value = request.data.get("course_ratings_value")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
"""

class getAllVideoView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
