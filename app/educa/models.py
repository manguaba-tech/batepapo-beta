from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField('nome do curso', max_length=50)

    class Meta:
        pass

    def __str__(self):
        return self.name

class Subscription(models.Model):
    course = models.ForeignKey(Course, related_name='subscriptions', 
                                on_delete=models.SET_NULL,
                                null=True)
    
    student = models.ForeignKey(User, 
                                related_name='courses', 
                                on_delete=models.SET_NULL,
                                null=True)