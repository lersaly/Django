from django.contrib import admin
from .models import Course, Topic, StudentCourse, TopicRating

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at')
    list_filter = ('creator', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'content')

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at', 'completed')
    list_filter = ('completed', 'enrolled_at')

@admin.register(TopicRating)
class TopicRatingAdmin(admin.ModelAdmin):
    list_display = ('topic', 'student', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')