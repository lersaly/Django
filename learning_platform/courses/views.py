from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Course, Topic, StudentCourse, TopicRating
from .forms import CourseForm, TopicForm, TopicRatingForm
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.db.models import Q
from .models import UserProfile

@login_required
def course_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if user_profile.is_instructor:
        created_courses = Course.objects.filter(creator=request.user)
        return render(request, 'courses/course_list.html', {
            'created_courses': created_courses,
        })
    else:
        enrolled_courses = Course.objects.filter(enrolled_students__student=request.user)
        available_courses = Course.objects.exclude(
            Q(enrolled_students__student=request.user) | Q(creator=request.user)
        )
        return render(request, 'courses/course_list.html', {
            'enrolled_courses': enrolled_courses,
            'available_courses': available_courses
        })

@login_required
def course_create(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if not user_profile.is_instructor:
        messages.error(request, 'Только преподаватели могут создавать курсы')
        return redirect('course_list')
        
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            messages.success(request, 'Курс успешно создан!')
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    topics = course.topics.all().order_by('order')
    is_enrolled = StudentCourse.objects.filter(student=request.user, course=course).exists()
    is_creator = course.creator == request.user
    
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'topics': topics,
        'is_enrolled': is_enrolled,
        'is_creator': is_creator
    })

@login_required
def topic_rate(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if not StudentCourse.objects.filter(student=request.user, course=topic.course).exists():
        messages.error(request, 'Вы должны быть записаны на курс, чтобы оценивать темы')
        return redirect('course_detail', pk=topic.course.pk)
    
    if topic.course.creator == request.user:
        messages.error(request, 'Автор курса не может оценивать свои темы')
        return redirect('course_detail', pk=topic.course.pk)

    existing_rating = TopicRating.objects.filter(topic=topic, student=request.user).first()

    if request.method == 'POST':
        form = TopicRatingForm(request.POST, instance=existing_rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.topic = topic
            rating.student = request.user
            rating.save()
            messages.success(request, 'Оценка успешно сохранена!')
            return redirect('course_detail', pk=topic.course.pk)
    else:
        form = TopicRatingForm(instance=existing_rating)
    
    return render(request, 'courses/topic_rate.html', {
        'form': form,
        'topic': topic
    })

@login_required
def course_enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if not StudentCourse.objects.filter(student=request.user, course=course).exists():
        StudentCourse.objects.create(student=request.user, course=course)
        messages.success(request, f'Вы успешно записались на курс "{course.title}"!')
    return redirect('course_detail', pk=pk)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            UserProfile.objects.create(
                user=user,
                is_instructor=form.cleaned_data['is_instructor']
            )
            
            login(request, user)
            messages.success(request, 'Регистрация успешно завершена!')
            return redirect('course_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})




@login_required
def topic_create(request, course_id):
    course = get_object_or_404(Course, id=course_id, creator=request.user)
    
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.course = course
            topic.save()
            messages.success(request, 'Материал успешно добавлен!')
            return redirect('course_detail', pk=course.id)
    else:
        form = TopicForm()
    
    return render(request, 'courses/topic_form.html', {
        'form': form,
        'course': course
    })

@login_required
def course_unenroll(request, pk):
    enrollment = get_object_or_404(StudentCourse, student=request.user, course_id=pk)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Вы успешно отписались от курса')
    return redirect('course_list')

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk, creator=request.user)
    course_title = course.title
    if request.method == 'POST':
        course.delete()
        messages.success(request, f'Курс "{course_title}" успешно удален')
    return redirect('course_list')

