from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from jsonfield import JSONField
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib import admin



# Create your models here.

class UserProfileManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, first_name,last_name, password=None,):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name= last_name,
            userType = 'ST',

        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name,last_name, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            first_name,
            last_name,
            password,


        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system. this is abstract class"""


    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USER_TYPE_CHOICES = (
        ('ST', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin'),
      )
    userType = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default='ST',
    )

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    #we are setting fname and lname as requred because email is by default reqired.
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        self.first_name + last_name

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        self.first_name

    def __str__(self):
        """What to show when we output an object as a string."""

        return "{}_{}".format(self.email,self.id)

class StudentProfile(UserProfile):

        subscribedCourses =JSONField()

        def subscribeCourse(self,courseID):
            self.subscribedCourses.append(courseID)

        def getAllSubscribedCourses(self):
            return self.subscribedCourses


class TeacherProfile(UserProfile):

        """averageRatings = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)],default = 0.0)"""

        averageRatings = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])



class Course(models.Model):

    course_name = models.CharField(max_length=255)
    course_author =  models.ForeignKey('TeacherProfile', on_delete=models.CASCADE)
    course_Ratings = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])
    course_created_at = models.DateTimeField(auto_now_add=True)
    course_avegrage_ratings = models.FloatField(default= 0.0)


    def __str__(self):
        """What to show when we output an object as a string."""

        return self.course_name


class Video(models.Model):

    video_name =  models.CharField(max_length=255)
    video_link =  models.CharField(max_length=255)
    video_description =  models.CharField(max_length=255)
    video_course =  models.ForeignKey('Course',related_name='Video_Relation', on_delete=models.CASCADE,blank = False)
    video_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.video_name

class CourseRatings(models.Model):

    _ratings_tobeshown = models.FloatField(default=0.0,db_column="ratings_tobeshown")
    rating_give_by_user = models.FloatField(default=0.0,validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])
    sum_of_all_ratings =models.FloatField(null=True, blank=True,default=0.0)
    total_number = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    course =  models.ForeignKey('Course',related_name='Course_Ratings_Relation', on_delete=models.CASCADE,blank = True)

    def __str__(self):
        return "rating_{}".format(self.id)

class Rating_Course_User_Bridge(models.Model):

    course = models.ForeignKey('Course',related_name='Course_Ratings_Bridge_Relation', on_delete=models.CASCADE,blank = True)
    user =  models.ForeignKey('UserProfile',related_name='UserProfile_Ratings_Bridge_Relation', on_delete=models.CASCADE,blank = True)
    rating_value =  models.FloatField()
