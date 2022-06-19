from django import forms
from django.contrib.auth.models import User
from . import models




#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['roll','cl','mobile','fee','status']

#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['mobile','status']


#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()




#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'isbn', 'author', 'category']


class IssuedBookForm(forms.Form):
    # to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Name and isbn",
                                   to_field_name="isbn", label='Name and Isbn')
    enrollment2 = forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(), empty_label="Name and enrollment",
                                         to_field_name='enrollment', label='Name and enrollment')
