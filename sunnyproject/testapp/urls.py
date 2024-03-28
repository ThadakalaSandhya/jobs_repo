from django.urls import path
from . import views
urlpatterns=[
             path('exams/',views.exams_view),
             path('attendance/',views.attendace_view),
             path('fees/',views.fees_view),
          ]