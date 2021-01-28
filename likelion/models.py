from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=10)
    user_name=models.CharField(max_length=30)
    user_grade=models.IntegerField()
    user_pn=models.CharField(max_length=11)
    user_major=models.CharField(max_length=30)
    user_q1=models.TextField()
    user_q2=models.TextField()
    user_q3=models.TextField()
    user_q4=models.TextField()
    