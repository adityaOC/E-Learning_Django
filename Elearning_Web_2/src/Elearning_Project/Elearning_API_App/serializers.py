from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Course,
    Video,
    CourseRatings,
    Rating_Course_User_Bridge,
    UserProfile,
    TeacherProfile,
    )
from rest_framework.response import Response
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
            'course_avegrage_ratings',
            'course_thumbnail_url',

        ]

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name','last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = UserProfile(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()


        return user


class AuthorSerializer(ModelSerializer):
    model = UserProfile
    fields = [

                'id',
                'email',
                'first_name',
                'last_name',
            ]

class CourseDetailViewSerailizer(ModelSerializer):
    course_videos = VideoSerializer(source='Video_Relation', many=True)
    courseAuthor = UserProfileSerializer(source='Author_Course_Relation', many=True)
    class Meta:
        model = Course
        fields= [
            'id',
            'course_name',
            'course_avegrage_ratings',
            'course_videos',
            'course_thumbnail_url',
            'courseAuthor',


        ]


class UpdateRatingsSerializer(ModelSerializer):


    class Meta:
        model = CourseRatings
        fields= [
            'rating_give_by_user',

        ]

class RatingBridgeSerializer(ModelSerializer):

    model = Rating_Course_User_Bridge
    fields= [
        'id',
        'rating_value',



    ]
