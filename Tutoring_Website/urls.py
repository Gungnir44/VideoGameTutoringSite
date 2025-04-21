from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('signup/player/', views.player_signup, name='player_signup'),
    path('signup/coach/', views.coach_signup, name='coach_signup'),
    path('coach/profile/create/', views.create_coach_profile, name='create_coach_profile'),
    path('browse/', views.browse_coaches, name='browse_coaches'),
    path('browse/<str:game>/', views.browse_coaches, name='browse_by_game'),
    path('coach/<int:pk>/', views.coach_detail, name='coach_detail'),
    path('coach/inbox/', views.coach_inbox, name='coach_inbox'),
    path('', views.home, name='home'),
    path('booking/<int:booking_id>/thread/', views.booking_thread, name='booking_thread'),
    path('booking/<int:booking_id>/review/', views.leave_review, name='leave_review'),
    path('dashboard/', views.player_dashboard, name='player_dashboard'),
    path('booking/<int:booking_id>/paid/', views.mark_as_paid, name='mark_as_paid'),
    path('booking/<int:booking_id>/mark_paid/', views.mark_booking_paid, name='mark_booking_paid'),
    path('login/', lambda request: redirect('login', permanent=True)),
]
handler404 = 'Tutoring_Website.views.custom_404'