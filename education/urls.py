from django.urls import path
from .views import home_view, quiz_list, quiz_detail, fill_in_the_blank, multiplication_quiz_view, exercises, addition_quiz, subtraction_quiz, division_quiz,irish_quiz

urlpatterns = [
    path('', home_view, name='home'), 
    path('quizzes/', quiz_list, name='quiz_list'),  
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),  
    path('quiz/<int:quiz_id>/fill-in-the-blank/', fill_in_the_blank, name='fill_in_the_blank'),
    path('exercises/', exercises, name='exercises'),  # Fixed here
    path('multiplication-quiz/', multiplication_quiz_view, name='multiplication_quiz'),
    path('addition_quiz/', addition_quiz, name='addition_quiz'),  # Fixed here
    path('subtraction_quiz/', subtraction_quiz, name='subtraction_quiz'),  # Fixed here
    path('division_quiz/', division_quiz, name='division_quiz'),
    path('irish_quiz/', irish_quiz, name='irish_quiz'),   # Fixed here
]
