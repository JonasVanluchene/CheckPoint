from django.db import models
from django.conf import settings
from games.models import Game


class Tag(models.Model):
    """
    Tags for games - can be global or user-specific
    """
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='custom_tags',
        null=True, 
        blank=True,
        help_text="If null, this is a global tag. If set, it's a user-specific tag."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['name', 'user']
        ordering = ['name']
    
    def __str__(self):
        if self.user:
            return f"{self.name} (User: {self.user.username})"
        return f"{self.name} (Global)"


class GameTag(models.Model):
    """
    Many-to-Many relationship between Game and Tag
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tagged_games')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='added_tags')
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['game', 'tag']
        ordering = ['tag__name']
    
    def __str__(self):
        return f"{self.game.title} - {self.tag.name}"
