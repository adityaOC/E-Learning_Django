from django.conf.urls import url
from . import views
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

"""
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('logout',views.LogoutViewSet,base_name='logout')
router.register('course',views.CourseViewSet,base_name='course')
"""
router = DefaultRouter()
router.register('loginR',views.LoginViewSet,base_name='loginR')
router.register('test/Register',views.UserRegistrationViewSet,base_name='Register')
#test url



urlpatterns = [
    url(r'^getAllCourses/',views.GetListCourses.as_view()),
    url(r'^herobanner/',views.HeroBannerAPIView.as_view()),
    url(r'^courseDetail/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detailCourse'),
    url(r'^ratings/(?P<pk>\d+)/update/',views.RatingUpdateView.as_view()),

    url(r'',include(router.urls)),

    #test urls
    url(r'^test/getAllRatings/',views.getAllRatings.as_view()),
    url(r'^test/Register/',views.UserRegistrationViewSet),
    #search query


    #url(r'^updateCourse/',views.CourseUpdateView.as_view(),name='updateCourse'),
    #url(r'^getAllVideoView/',views.getAllVideoView.as_view()),

    #url(r'^hello-view/',views.HelloApiView.as_view()),
    #url(r'^NewAPI/',views.NewAPI.as_view()),
    #url(r'',include(router.urls))
    ]
