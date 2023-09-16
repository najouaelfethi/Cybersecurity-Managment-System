from django.urls import path
from . import views

urlpatterns=[
    path('basic', views.basic, name='basic'),
    path('addEvaluation', views.addEvaluation, name='addEvaluation'),
    path('supprimer/<int:pk>/', views.supprimer, name='supprimer'),
    path('supprimerPlan/<int:pk>/', views.supprimerPlan, name='supprimerPlan'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('answerEvaluation/<int:pk>/', views.answerEvaluation, name='answerEvaluation'),  
    path('modifier/<int:pk>/evaluation', views.modifier, name='modifier'),
    path('evaluation', views.evaluation, name='evaluation'),
    path('avancement', views.avancement, name='avancement'),
    path('rapport', views.rapport, name='rapport'),
    path('exportExcel', views.exportExcel, name='exportExcel'),
    path('plan', views.plan, name='plan'),
    path('editPlan/<int:pk>/', views.editPlan, name='editPlan'),
    path('updatePlan/<int:pk>/', views.updatePlan, name='updatePlan'),
    path('ajouterPlan', views.ajouterPlan, name='ajouterPlan'),
    path('all_plans/', views.all_plans, name='all_plans'),
    path('add_plan/', views.add_plan, name='add_plan'),
    path('email', views.email, name='email'),
    path('answerchatgpt', views.answerchatgpt, name='answerchatgpt'),
    path('profil', views.profil, name='profil'),
    path('rapportExcel', views.rapportExcel, name='rapportExcel'),
    path('questionnaire', views.questionnaire, name='questionnaire'),

] 