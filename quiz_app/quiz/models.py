from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    options = models.JSONField()  # Store options as JSON
    correct_option = models.IntegerField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField()
    is_correct = models.BooleanField()

    def __str__(self):
        return f'Answer to {self.question}'


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return f'Result for {self.user} in {self.quiz}'

