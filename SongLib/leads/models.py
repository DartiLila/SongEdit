from authuser.models import User
# from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    
    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    NEW = 'new'
    INTERMEDIATE = 'intermediate'
    VETERAN = 'veteran'

    LEVEL_PRIORITY = (
        (NEW, 'New'),
        (INTERMEDIATE, 'Intermediate'),
        (VETERAN, 'Veteran'),
    )

    username = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default = MEDIUM)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    