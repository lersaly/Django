from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_courses', verbose_name="Создатель курса")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        topic_ratings = TopicRating.objects.filter(topic__course=self)
        if topic_ratings.exists():
            return topic_ratings.aggregate(models.Avg('rating'))['rating__avg']
        return 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['-created_at']

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200, verbose_name="Название темы")
    content = models.TextField(verbose_name="Содержание темы")
    order = models.IntegerField(verbose_name="Порядковый номер")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class StudentCourse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_courses')
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,
        related_name='enrolled_students'
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['student', 'course']

class TopicRating(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='ratings')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_ratings')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Оценка понятности темы (1 - совсем непонятно; 10 - идеально понятно)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['topic', 'student']

    def __str__(self):
        return f"{self.topic.title} - {self.student.username} - {self.rating}"