from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .viewset import SchoolViewSet , ClassroomViewSet
from .views import SchoolListView , ClassroomListView

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'classrooms', ClassroomViewSet)

urlpatterns = [
    path('', include(router.urls)),         # This creates endpoints like /schools/ and /schools/<pk>/
    path("schools-html/", SchoolListView.as_view(), name="school_list"),  # For HTML page listing schools
    path("classrooms-html/", ClassroomListView.as_view(), name="classroom_list"),
]
