from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from . import models


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return models.Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'polls/results.html'


class VoteView(generic.View):
    def post(self, request: HttpRequest, *args, **kwargs):
        question_id = kwargs['question_id']

        question = get_object_or_404(models.Question, pk=question_id)

        try:
            choice = models.Choice.objects.get(pk=request.POST['choice'])
        except:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': 'вы не сделали выбор'
            })
        else:
            choices = question.choice_set.all()

            if request.user.vote_set.filter(choice_id__in=choices).exists():
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': 'вы уже голосовали!'
                })

            models.Vote.objects.create(user=request.user, choice=choice)

            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
