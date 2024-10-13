# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    time_limit = models.IntegerField(default=10)  # U sekundama

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200)
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.text

class Task(models.Model):
    TASK_TYPES = [
        ('word_input', 'Word Input'),
        ('number_input', 'Number Input'),
        ('sentence_fill', 'Fill in the Blank'),
        ('multiple_choice', 'Multiple Choice'),
        ('multiplication', 'Multiplication'),  # Dodano za zadatke množenja
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    prompt = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200)
    options = models.JSONField(blank=True, null=True)  # Koristi se za višekratne izbore

    def __str__(self):
        return self.prompt

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    quizzes_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class UserTaskResult(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.task.prompt} - {'Correct' if self.is_correct else 'Incorrect'}"

class FillInTheBlankTask(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=500)
    blank_word = models.CharField(max_length=200)  # Riječ koja će biti izostavljena
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.sentence.replace(self.blank_word, '____')

    def get_sentence_with_blank(self):
        return self.sentence.replace(self.blank_word, '____')
