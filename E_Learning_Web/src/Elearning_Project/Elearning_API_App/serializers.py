from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Course,Video


class VideoSerializer(ModelSerializer):


    class Meta:
        model = Video
        fields= [
            'id',
            'video_name',
            'video_link',
            'video_description',


        ]

class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields= [
            'id',
            'course_name',
            'course_author',
            'course_Ratings',



        ]


class CourseDetailViewSerailizer(ModelSerializer):
    course_videos = VideoSerializer(source='Video_Relation', many=True)
    class Meta:
        model = Course
        fields= [
            'id',
            'course_name',
            'course_author',
            'course_Ratings',
            'course_videos',


        ]


class UpdateRatingsSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields= [

            'course_Ratings',


        ]
