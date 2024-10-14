from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, UserTaskResult, Task, FillInTheBlankTask
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Funkcija za prijavu
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quiz_list')  # Preusmjeri na popis kvizova
        else:
            return render(request, 'education/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'education/login.html')

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()  # Preuzmi sve kvizove
    return render(request, 'education/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    tasks = Task.objects.filter(quiz=quiz)  # Preuzmi zadatke za taj kviz

    if request.method == 'POST':
        user_answers = request.POST.getlist('user_answers')
        results = []
        correct_count = 0

        for task, user_answer in zip(tasks, user_answers):
            is_correct = user_answer.strip().lower() == task.correct_answer.strip().lower()
            results.append({
                'task': task,
                'user_answer': user_answer,
                'is_correct': is_correct,
            })

            if is_correct:
                correct_count += 1

            user_profile = request.user.userprofile
            UserTaskResult.objects.create(
                user_profile=user_profile,
                task=task,
                user_answer=user_answer,
                is_correct=is_correct,
            )

        total_tasks = len(tasks)
        accuracy_percentage = (correct_count / total_tasks) * 100 if total_tasks > 0 else 0

        return render(request, 'education/quiz_results.html', {
            'results': results,
            'quiz': quiz,
            'correct_count': correct_count,
            'total_tasks': total_tasks,
            'accuracy_percentage': accuracy_percentage,
        })

    # Ako nije POST zahtjev, prikazujemo detalje kviza
    return render(request, 'education/quiz_detail.html', {'quiz': quiz, 'tasks': tasks})
    
@login_required
def fill_in_the_blank(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    tasks = FillInTheBlankTask.objects.filter(quiz=quiz)

    # Start the timer only when the user accesses the page (GET request)
    if request.method == 'GET':
        request.session['start_time'] = timezone.now().isoformat()  # Store the start time in the session

    if request.method == 'POST':
        user_answers = request.POST.getlist('user_answers')
        results = []
        correct_count = 0

        # Retrieve start time from session
        start_time = timezone.datetime.fromisoformat(request.session['start_time'])
        end_time = timezone.now()
        time_taken_seconds = (end_time - start_time).total_seconds()  # in seconds

        for task, user_answer in zip(tasks, user_answers):
            is_correct = user_answer.strip().lower() == task.blank_word.lower()
            results.append({
                'task': task,
                'user_answer': user_answer,
                'is_correct': is_correct,
            })

            if is_correct:
                correct_count += 1

            # Save results in UserTaskResult model
            user_profile = request.user.userprofile
            UserTaskResult.objects.create(
                user_profile=user_profile,
                fill_in_the_blank_task=task,
                user_answer=user_answer,
                is_correct=is_correct,
            )

        # Calculate minutes and seconds for the total time taken
        minutes = int(time_taken_seconds // 60)
        seconds = int(time_taken_seconds % 60)
        formatted_time_taken = f"{minutes} minute(s) {seconds} second(s)"

        total_tasks = len(tasks)
        accuracy_percentage = (correct_count / total_tasks * 100) if total_tasks > 0 else 0

        return render(request, 'education/fill_in_results.html', {
            'results': results,
            'quiz': quiz,
            'correct_count': correct_count,
            'total_tasks': total_tasks,
            'accuracy_percentage': accuracy_percentage,
            'time_taken': formatted_time_taken,  # Add formatted time taken
        })

    # For GET request, show the tasks without submitting answers
    return render(request, 'education/fill_in_the_blank.html', {'quiz': quiz, 'tasks': tasks})

@login_required
def fill_in_the_blank_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    results = UserTaskResult.objects.filter(user_profile=request.user.userprofile, fill_in_the_blank_task__quiz=quiz)

    correct_count = sum(1 for result in results if result.is_correct)
    total_tasks = results.count()
    accuracy_percentage = (correct_count / total_tasks * 100) if total_tasks > 0 else 0

    return render(request, 'education/quiz_results.html', {
        'quiz': quiz,
        'results': results,
        'correct_count': correct_count,
        'total_tasks': total_tasks,
        'accuracy_percentage': accuracy_percentage,
    })
