from django.db import models


class Game(models.Model):
    """
    Game model representing individual games
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Additional useful fields
    developer = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    metacritic_score = models.IntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
