from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
class EntryExitTime(models.Model):
    stu=models.ForeignKey(to=Student,on_delete=models.CASCADE)
    EntryTime=models.DateTimeField(auto_created=False)
    ExitTime=models.DateTimeField(auto_created=False)