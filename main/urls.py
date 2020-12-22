from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('create_course', views.create_course),
    path('process_course', views.process_course),
    path('course/<int:course_id>', views.one_course),
    path('review/<int:course_id>', views.review_course),
    path('process_review', views.process_review),
    path('delete_course/<int:course_id>', views.delete_course),
    path('stats/<int:course_id>', views.game_stats),
    path('like/<int:course_id>', views.like_course),
    path('logout', views.logout),
]