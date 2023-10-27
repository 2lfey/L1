from django.urls import path

from . import views

from django.views import generic as generic_views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.VoteView.as_view(), name='vote'),

    path('<int:pk>/vote-again/', generic_views.TemplateView.as_view(template_name='polls/vote_again.html'), name='vote-again'),
]