from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from games.models import Game


class Review(models.Model):
    """
    User reviews and ratings for games
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rating from 1 to 10"
    )
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Additional fields
    is_spoiler = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['user', 'game']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.game.title} ({self.rating}/10)"
