from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import CoachProfile, BookingRequest, BookingMessage, Review

class PlayerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_player = True
        user.is_coach = False
        if commit:
            user.save()
        return user

class CoachSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_player = False
        user.is_coach = True
        if commit:
            user.save()
        return user


class CoachProfileForm(forms.ModelForm):
    class Meta:
        model = CoachProfile
        fields = ['game', 'rank', 'rate_per_hour', 'bio', 'availability']


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['session_date', 'session_time', 'message', 'discord_id']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
            'session_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class BookingMessageForm(forms.ModelForm):
    class Meta:
        model = BookingMessage
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your message...'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

