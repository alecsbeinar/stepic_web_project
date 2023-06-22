from django.db import models, connection
from django.contrib.auth.models import User

class QuestionManager(models.Manager):

    def new(self):
        return self.order_by("-added_at")
    
    def popular(self):
        return self.order_by("-rating")
    

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def __str__(self) -> str:
        return f"Title: {self.title}"


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)

