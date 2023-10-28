import datetime

from django.db import models
from django.utils import timezone

from users.models import User


class Question(models.Model):
    poster = models.ImageField(upload_to='posters', null=True)
    description = models.CharField(max_length=2000, null=True)
    summary = models.CharField(max_length=300, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self):
        return Vote.count_choice(choice=self)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    @staticmethod
    def count():
        return Vote.objects.count()
    
    @staticmethod
    def count_choice(choice):
        return Vote.objects.filter(choice=choice).count()

    def __str__(self):
        return f'{self.user} - {self.choice}'