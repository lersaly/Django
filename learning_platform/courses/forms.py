from django import forms
from .models import Course, Topic, TopicRating
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название курса'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание курса',
                'rows': 4
            })
        }

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TopicRatingForm(forms.ModelForm):
    class Meta:
        model = TopicRating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '10'
            })
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок материала'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание материала', 'rows': 6}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Порядковый номер'})
        }

