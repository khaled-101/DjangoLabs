from django.urls import path , include
from .viewset import SchoolViewSet , ClassroomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("schools", SchoolViewSet)
router.register("classrooms", ClassroomViewSet)

urlpatterns = [
    path("" , include(router.urls))
]
