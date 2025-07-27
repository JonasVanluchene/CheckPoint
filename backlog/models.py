from django.db import models
from django.conf import settings
from games.models import Game


class UserBacklog(models.Model):
    """
    Relationship between User and Game with status tracking
    """
    STATUS_CHOICES = [
        ('wishlist', 'Wishlist'),
        ('playing', 'Currently Playing'),
        ('on-hold', 'On Hold'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='backlog_entries')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='backlog_entries')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    
    # Dates
    started_on = models.DateField(blank=True, null=True)
    finished_on = models.DateField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Progress tracking
    hours_played = models.DecimalField(max_digits=6, decimal_places=1, default=0, blank=True, null=True)
    progress_percentage = models.IntegerField(default=0, blank=True, null=True)  # 0-100
    
    # Notes
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ['user', 'game']
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.game.title} ({self.status})"
