from django.db import models
from authentication.models import UserDNSSI
# Create your models here.

class Evaluation(models.Model):
    id= models.AutoField(primary_key=True)
    nom= models.CharField(max_length=70)
    entite= models.TextField(max_length=60, null=True) 
    description= models.TextField(max_length=1000) 
    date= models.DateField()
    
class Category(models.Model):
    id_category= models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=100)
    names= models.CharField(max_length=40)

class Objectif(models.Model):
    id_objectif= models.AutoField(primary_key=True)
    objectif_name= models.CharField(max_length=400)  
    id_category= models.ForeignKey(
    'Category',
    on_delete=models.CASCADE,
)

class Question(models.Model):
    id_question= models.AutoField(primary_key=True)
    question= models.CharField(max_length=300)
    id_category= models.ForeignKey(
    'Category',
    on_delete=models.CASCADE,
    )
    poids=models.CharField(max_length=30, null=True)

    
class Answer(models.Model):
    id_answer= models.AutoField(primary_key=True)
    answer= models.CharField(max_length=30) 
    maturite= models.CharField(max_length=30)
    question= models.ForeignKey(                     
    'Question',
    on_delete=models.CASCADE,
)
    category= models.ForeignKey(
    'Category',
    on_delete=models.CASCADE,
)
    evaluation= models.ForeignKey(
    'Evaluation',
    on_delete=models.CASCADE, null=True
)
    commentaire=models.CharField(max_length=1000, null=True)
    file= models.FileField(null=True)

class Plan(models.Model):
    chapitre=models.CharField(max_length=300)
    action=models.CharField(max_length=1000)
    responsable=models.CharField(max_length=200)
    date_debut=models.DateField()
    date_fin=models.DateField()
    budget=models.CharField(max_length=200)
    
class Profil(models.Model):
    user = models.OneToOneField(UserDNSSI, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True)
    entite = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=100, null=True)
    evaluationRecente = models.CharField(max_length=100, null=True)   
    
class Rapport(models.Model):
    category= models.CharField(max_length=100)
    question= models.CharField(max_length=50)
    response= models.CharField(max_length=50)
    maturite= models.CharField(max_length=50)
    evaluation= models.CharField(max_length=100, null=True)
    




    
