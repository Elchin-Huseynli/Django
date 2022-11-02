from django.urls import path

from . import views

app_name = 'proqramim'
urlpatterns = [
    path('', views.IndexView.as_view(), name='esas'),
    path('<int:pk>/', views.DetailView.as_view(), name='etrafli'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='neticeler'),
    path('<int:question_id>/vote/', views.vote, name='ses'),
]