from django import forms
from .models import Submissions,Course,Cname,RegUsers
# import self as self
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class CreateCourseForm(forms.ModelForm):
    code=forms.CharField(max_length=10)
    course_name=forms.CharField(max_length = 30)
    secret_code = forms.CharField(max_length=30)
    
    class Meta():
        model=Cname
        fields=('code','course_name','secret_code')


class CourseForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    # code=forms.CharField(max_length=100)
    code = forms.ModelChoiceField(queryset=Cname.objects.all())
    question=forms.CharField(widget=forms.Textarea, required=False)
    question_file=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    deadline_date=forms.DateField(widget=forms.SelectDateWidget)
    deadline_time=forms.TimeField()
    max_marks=forms.IntegerField()
    
    class Meta():
        model=Course
        fields=('name','code','question','deadline_date','deadline_time','max_marks','question_file')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CourseForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date1 = RegUsers.objects.filter(course=cleaned_data['code'], user=self.user).exists()
        x = 0
        print(date1)
        if date1 == False:
            raise forms.ValidationError('User cannot create assignment for this course. First register for the course.')
        return cleaned_data

class SubmissionForm(forms.ModelForm):
    class Meta():
        fields=('answer',)
        model=Submissions

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['answer']='Upload your file'

class RegisterForm(forms.ModelForm):
    secret_code = forms.CharField(max_length=30)

    class Meta():
        fields=()
        model=RegUsers

class GradingForm(forms.ModelForm):
    feedback=forms.CharField(widget=forms.Textarea, required=False)
    marks=forms.IntegerField()

    class Meta():
        fields=('marks','feedback')
        model=Submissions

    def clean(self):
        cleaned_data = super().clean()

        if (cleaned_data['marks'] > self.instance.course.max_marks) or (cleaned_data['marks'] < 0):
            raise forms.ValidationError('Marks should be between 0 and %s.' % str(self.instance.course.max_marks))
        return cleaned_data


