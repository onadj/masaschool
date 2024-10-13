# masaschool
- python manage.py runserver

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/onadj/masaschool)


-- Explanation of the Model:

1. Category: Categories of quizzes (eg math, English, Irish).

2. Quiz: The main unit that contains questions and tasks. It has a creation date to track.

3. Question: Questions within quizzes. Can have points for each correct solution.

4. Task: Different types of tasks (writing words, numbers, completing sentences, multiple choice). options is used for multiple selection.

5. UserProfile: It is associated with the user and contains points and the number of completed quizzes.

6. UserTaskResult: Saves the results of the tasks that the user has solved, including the user's answer and information about whether it is correct.


