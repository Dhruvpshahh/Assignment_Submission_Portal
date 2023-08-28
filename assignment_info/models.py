from django.db import models
from django.conf import settings
from django.urls import reverse

class Cname(models.Model):
    code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=30,default='Course Name')
    secret_code = models.CharField(max_length=30,default='Secret Code')

    def __str__(self):
        return self.code

class RegUsers(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    course=models.ForeignKey(Cname,on_delete=models.CASCADE,default=1,related_name='reg_users')

    def get_absolute_url(self):
        return reverse('assignments:list')

    def __str__(self):
        return "{}-{}".format(self.user.username,self.course.code)


class Course(models.Model):
    name=models.CharField(max_length=30,blank=False)
    code=models.ForeignKey(Cname,on_delete=models.CASCADE,default=1,related_name='course_code')
    question=models.TextField(blank=False)
    question_file=models.FileField(blank=True,null=True)
    deadline_date=models.DateField(null=True)
    deadline_time =models.TimeField(null=True)
    max_marks=models.IntegerField(default=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'code'], name='unique_course_name')
        ]

    def __str__(self):
        return "{}-{}".format(self.code,self.name)



class Submissions(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=1,related_name='submission')
    answer=models.FileField(upload_to='assignments')
    submitted_at=models.DateTimeField(auto_now=True,blank=False)
    marks=models.IntegerField(default=-1)
    feedback=models.TextField(blank=True,default='No feedback')
    checked_by = models.CharField(max_length=30,blank=True,default='Not checked yet')


    def get_absolute_url(self):
        return reverse('assignments:list')

    def __str__(self):
        return "{}-{}".format(self.user.username,self.user.first_name+' '+self.user.last_name)
