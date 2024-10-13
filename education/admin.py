# admin.py
from django.contrib import admin
from .models import Quiz, Question, Task, Category, FillInTheBlankTask, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'correct_answer')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'task_type', 'prompt', 'correct_answer')

@admin.register(FillInTheBlankTask)
class FillInTheBlankTaskAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'sentence', 'blank_word')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'quizzes_completed')
