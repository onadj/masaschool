from django.urls import path
from .views import home_view, quiz_list, quiz_detail, fill_in_the_blank, multiplication_quiz_view  # Dodajte multiplication_quiz_view ovdje

urlpatterns = [
    path('', home_view, name='home'), 
    path('quizzes/', quiz_list, name='quiz_list'),  
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),  
    path('quiz/<int:quiz_id>/fill-in-the-blank/', fill_in_the_blank, name='fill_in_the_blank'),
    path('multiplication-quiz/', multiplication_quiz_view, name='multiplication_quiz'),  
]
