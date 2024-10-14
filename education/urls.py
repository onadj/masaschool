from django.urls import path
from .views import quiz_list, quiz_detail, fill_in_the_blank

urlpatterns = [
    path('quizzes/', quiz_list, name='quiz_list'),  # Popis kvizova
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),  # Detalji kviza
    path('quiz/<int:quiz_id>/fill-in-the-blank/', fill_in_the_blank, name='fill_in_the_blank'),  # Popunjavanje praznina
]
