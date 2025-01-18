from django import template
from django.db.models import Avg
from courses.models import TopicRating

register = template.Library()

@register.filter
def has_rated(user, topic):
    return TopicRating.objects.filter(student=user, topic=topic).exists()

@register.filter
def get_rating(user, topic):
    rating = TopicRating.objects.filter(student=user, topic=topic).first()
    return rating.rating if rating else None

@register.filter
def avg_rating(ratings):
    return ratings.aggregate(Avg('rating'))['rating__avg']

@register.filter
def divided_by(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0
    
@register.filter
def filter_user_rating(ratings, user):
    user_rating = ratings.filter(student=user).first()
    return user_rating.rating if user_rating else None