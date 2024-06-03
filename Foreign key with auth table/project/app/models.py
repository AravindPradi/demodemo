from django.db import models
from django.contrib.auth import get_user_model
usr = get_user_model()



class Course(models.Model):
    course_name = models.CharField(max_length=100)


class Teacher(models.Model):
    user = models.ForeignKey(usr,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)
    join_date = models.DateField(auto_now=True)