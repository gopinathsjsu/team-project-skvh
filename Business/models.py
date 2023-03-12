from django.db import models
import datetime

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
    

class Class(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    strength = models.IntegerField(default=20)
    instructor = models.ForeignKey(
        'Business.Instructor', on_delete=models.CASCADE)
    time = models.DateTimeField()
    location = models.ForeignKey(
        'Gym.Location', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def spots_left(self):
        enrolled_count = Enrolled.objects.filter(enrolled_class=self).count()
        return max(self.strength - enrolled_count, 0)