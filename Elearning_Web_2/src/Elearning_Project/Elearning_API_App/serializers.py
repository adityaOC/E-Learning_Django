from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Course,
    Video,
    CourseRatings,
    Rating_Course_User_Bridge,
    UserProfile,
    )

class RatingsSerializer(ModelSerializer):

    class Meta:
        model = CourseRatings
        fields= [
            'rating_give_by_user',

        ]
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
            'course_avegrage_ratings',



        ]


class CourseDetailViewSerailizer(ModelSerializer):
    course_videos = VideoSerializer(source='Video_Relation', many=True)
    course_ratings = RatingsSerializer(source='Course_Ratings_Relation', many=True)
    class Meta:
        model = Course
        fields= [
            'id',
            'course_name',
            'course_author',
            'course_Ratings',
            'course_videos',
            'course_ratings',


        ]


class UpdateRatingsSerializer(ModelSerializer):


    class Meta:
        model = CourseRatings
        fields= [
            'id',
            'rating_give_by_user',



        ]

class RatingBridgeSerializer(ModelSerializer):
    #course = CourseSerializer(source='Course_Ratings_Bridge_Relation', many=True)

    model = Rating_Course_User_Bridge
    fields= [
        'id',
        'rating_value',



    ]
