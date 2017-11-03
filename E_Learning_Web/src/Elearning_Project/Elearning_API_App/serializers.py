from rest_framework.serializers import ModelSerializer

from .models import Course

class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields= [
            'id',
            'course_name',
            'course_author',
            'course_Ratings',




        ]
