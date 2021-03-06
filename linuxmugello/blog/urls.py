from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    
    path('', views.index, name='index'),
   
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('menu/', views.menu, name='menu'),
    
    path('newss/', views.newss, name='newss'),
    
    path('news_one/', views.news_one, name='news_one'),
    
    path('slide/', views.slide, name='slide'),

]