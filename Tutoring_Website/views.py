from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import PlayerSignUpForm, CoachSignUpForm, BookingMessageForm, ReviewForm
from django.contrib.auth import login
from .models import CoachProfile, GAME_CHOICES
from django.shortcuts import get_object_or_404
from .forms import BookingRequestForm
from .models import BookingRequest
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

def player_signup(request):
    if request.method == 'POST':
        form = PlayerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = PlayerSignUpForm()
    return render(request, 'signup.html', {'form': form, 'role': 'Player'})

def coach_signup(request):
    if request.method == 'POST':
        form = CoachSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CoachSignUpForm()
    return render(request, 'signup.html', {'form': form, 'role': 'Coach'})

from .forms import CoachProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def create_coach_profile(request):
    if request.method == 'POST':
        form = CoachProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  # Change this later
    else:
        form = CoachProfileForm()
    return render(request, 'create_coach_profile.html', {'form': form})

def browse_coaches(request, game=None):
    if game:
        coaches = CoachProfile.objects.filter(game=game)
    else:
        coaches = CoachProfile.objects.all()
    return render(request, 'browse_coaches.html', {
        'coaches': coaches,
        'games': GAME_CHOICES,
    })

def coach_detail(request, pk):
    coach = get_object_or_404(CoachProfile, pk=pk)
    return render(request, 'coach_detail.html', {'coach': coach})

@login_required
def coach_detail(request, pk):
    coach = get_object_or_404(CoachProfile, pk=pk)

    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.coach = coach
            booking.player = request.user
            booking.save()
            return redirect('browse_by_game', game=coach.game)
    else:
        form = BookingRequestForm()

    return render(request, 'coach_detail.html', {
        'coach': coach,
        'form': form
    })

@login_required
def coach_inbox(request):
    if not request.user.is_coach:
        return redirect('browse_coaches')  # redirect non-coaches

    bookings = BookingRequest.objects.filter(coach__user=request.user).order_by('-submitted_at')

    return render(request, 'coach_inbox.html', {
        'bookings': bookings
    })

@login_required
def home(request):
    return render(request, 'home.html', {
        'is_coach': request.user.is_coach,
        'is_player': request.user.is_player,
    })

@login_required
def booking_thread(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    # Only allow the coach or player to view the thread
    if request.user != booking.coach.user and request.user != booking.player:
        return redirect('home')

    if request.method == 'POST':
        form = BookingMessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.booking = booking
            msg.sender = request.user
            msg.save()
            return redirect('booking_thread', booking_id=booking_id)
    else:
        form = BookingMessageForm()

    return render(request, 'booking_thread.html', {
        'booking': booking,
        'form': form,
        'messages': booking.messages.order_by('timestamp')
    })

@login_required
def leave_review(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    # Only the player on this booking can review, and only once
    if request.user != booking.player or hasattr(booking, 'review'):
        return redirect('home')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.player = request.user
            review.coach = booking.coach
            review.save()
            return redirect('coach_detail', pk=booking.coach.id)
    else:
        form = ReviewForm()

    return render(request, 'leave_review.html', {'form': form, 'booking': booking})

@login_required
def player_dashboard(request):
    if not request.user.is_player:
        return redirect('home')

    bookings = BookingRequest.objects.filter(player=request.user).order_by('-submitted_at')

    return render(request, 'player_dashboard.html', {
        'bookings': bookings
    })

@login_required
def mark_as_paid(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    if request.user == booking.player or request.user.is_superuser:
        booking.paid = True
        booking.save()
        messages.success(request, 'Booking Paid Successfully! 🎉')

    return redirect('player_dashboard')

@csrf_exempt
def mark_booking_paid(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(BookingRequest, id=booking_id)
        booking.paid = True
        booking.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def custom_404(request, exception):
    return render(request, '404.html', status=404)