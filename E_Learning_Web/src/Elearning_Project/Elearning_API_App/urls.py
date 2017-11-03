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
urlpatterns = [
    url(r'^getAllCourses/',views.GetListCourses.as_view()),
    url(r'^course/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detailCourse'),
    url(r'^course/(?P<pk>\d+)/update/$', views.CourseUpdateView.as_view(), name='updateCourse'),
    url(r'^updateCourse/',views.CourseUpdateView.as_view(),name='updateCourse'),
    #url(r'^hello-view/',views.HelloApiView.as_view()),
    #url(r'^NewAPI/',views.NewAPI.as_view()),
    #url(r'',include(router.urls))
    ]
