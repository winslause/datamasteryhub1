from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('data_scrapping/', views.data_scrapping, name='data_scrapping'),
    path('survey/', views.survey, name='survey'),
    path('ml/', views.ml, name='ml'),
    path('economics/', views.economics, name='economics'),
    path('data_analysis/', views.data_analysis, name='data_analysis'),
    path('data_cleaning/', views.data_cleaning, name='data_cleaning'),
    path('finance/', views.finance, name='finance'),
    path('business_analytics/', views.business_analytics, name='business_analytics'),
    path('data_insights/', views.data_insights, name='data_insights'),
    path('business_forecasting/', views.business_forecasting, name='business_forecasting'),
    path('predictive_analysis/', views.predictive_analysis, name='predictive_analysis'),
    path('data_visualization/', views.data_visualization, name='data_visualization'),
    path('login/', views.login_page, name='login'),
    path('exams/', views.exams, name='exams'),
    path('assignment/', views.assignment, name='assignment'),
    path('technical_writing/', views.technical_writing, name='technical_writing'),

]