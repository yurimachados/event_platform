from django.db import models
from django.contrib.auth.models import User
from .company_model import Company

from django.core.validators import MinValueValidator, MaxValueValidator

class Event(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/event_images/', null=True, blank=True)
    cover = models.ImageField(upload_to='images/event_covers/', null=True, blank=True)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()

    def average_rating(self):
        total_ratings = self.ratings.count()
        if total_ratings == 0:
            return None
        total_score = sum(rating.score for rating in self.ratings.all())
        return total_score / total_ratings

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d/%m')}"
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['date']

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.event.title}'
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['comment_date']

class Rating(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user.username} rated {self.score}'
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ['score']