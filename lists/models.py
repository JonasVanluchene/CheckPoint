from django.db import models
from django.conf import settings
from games.models import Game


class CustomList(models.Model):
    """
    User-defined custom game lists
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='custom_lists')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        unique_together = ['user', 'name']
    
    def __str__(self):
        return f"{self.user.username} - {self.name}"


class CustomListGame(models.Model):
    """
    Many-to-Many relationship between CustomList and Game with additional metadata
    """
    custom_list = models.ForeignKey(CustomList, on_delete=models.CASCADE, related_name='list_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='in_lists')
    added_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)  # For custom ordering within the list
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ['custom_list', 'game']
        ordering = ['order', 'added_at']
    
    def __str__(self):
        return f"{self.custom_list.name} - {self.game.title}"
