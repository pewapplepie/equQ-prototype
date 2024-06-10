from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=255)
    # logo = models.ImageField(upload_to='school_logos/')
    logo = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Degree(models.Model):
    DEGREE_LEVELS = [
        ('B', 'Bachelor'),
        ('M', 'Master'),
        ('P', 'PhD'),
        # Add more as needed
    ]

    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='degrees')
    level = models.CharField(max_length=1, choices=DEGREE_LEVELS)
    description = models.TextField()
    curriculum = models.TextField()
    application_deadline = models.DateField()
    apply_link = models.URLField()
    save = models.ManyToManyField(User, related_name='saved_degrees', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_degrees', blank=True)
    view_count = models.IntegerField(default=0)  # Renamed field to avoid conflict

    def __str__(self):
        return f"{self.name} - {self.school.name}"

class DegreeView(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='degree_views')  # Updated related_name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} viewed {self.degree.name} on {self.view_date}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    profile_picture = models.CharField(max_length=225)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    interests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name or self.user.username

# Signals to create or update the user profile automatically
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()