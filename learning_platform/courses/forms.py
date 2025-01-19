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
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    is_instructor = forms.BooleanField(
        required=False,
        initial=False,
        label='Зарегистрироваться как преподаватель',
        help_text='Отметьте, если вы планируете создавать курсы',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_instructor']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['username'].label = 'Имя пользователя'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок материала'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание материала', 'rows': 6}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Порядковый номер'})
        }

