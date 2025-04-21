from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_coach = models.BooleanField(default=False)
    is_player = models.BooleanField(default=True)

GAME_CHOICES = [
    ("lol", "League of Legends"),
    ("marvel", "Marvel Rivals"),
    ("valorant", "Valorant"),
    ("overwatch", "Overwatch"),
    ("fortnite", "Fortnite"),
    ("rocketleague", "Rocket League"),
    ("smash", "Super Smash Bros"),
    ("pokemon", "Pokemon TCG"),
]


class CoachProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    game = models.CharField(max_length=50, choices=GAME_CHOICES)
    rank = models.CharField(max_length=100)
    rate_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField()
    availability = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.get_game_display()}"

class BookingRequest(models.Model):
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_time = models.TimeField()
    message = models.TextField()
    discord_id = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.player.username} for {self.coach.user.username} on {self.session_date}"

class BookingMessage(models.Model):
    booking = models.ForeignKey(BookingRequest, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"

class Review(models.Model):
    booking = models.OneToOneField(BookingRequest, on_delete=models.CASCADE)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE, related_name='reviews')
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} rated {self.coach.user.username} - {self.rating}⭐"

@property
def average_rating(self):
    reviews = self.reviews.all()
    if reviews.exists():
        return round(sum(r.rating for r in reviews) / reviews.count(), 1)
    return None
