from django.shortcuts import render, redirect
from dashboard.models import Evaluation
from dashboard.models import Category
from dashboard.models import Objectif
from dashboard.models import Question
from dashboard.models import Answer
from dashboard.models import Plan
from dashboard.models import Profil
from dashboard.models import Rapport
from datetime import datetime
from django.http import HttpResponse,JsonResponse
import openai
import ast
from django.views import View
from django.core.mail import send_mail
import openpyxl
from . import views



# Create your views here.
#{}
openai.api_key="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"

def basic(request):
    return render(request, 'basic.html')

def evaluation(request):
    evaluation= Evaluation.objects.all()
    return render(request, 'evaluation.html',{'evaluation':evaluation})


def addEvaluation(request):
    if request.method=='POST':
        nom= request.POST.get("nom").lower()
        entite= request.POST.get("entite").lower()
        description= request.POST.get("description")
        date= request.POST.get("date")
        #create object of models
        ev= Evaluation() #model name
        ev.nom=nom
        ev.entite=entite
        ev.description=description
        ev.date=date
        ev.save()
        return redirect("evaluation")
    return render(request, 'addEvaluation.html',{})

def supprimer(request,pk):  
    evaluation = Evaluation.objects.get(id=pk) 
    evaluation.delete() 
    return redirect('evaluation')
   
def modifier(request,pk):
       categories= Category.objects.all()
       objectifs= Objectif.objects.all()
       questions= Question.objects.all()
       evaluation = Evaluation.objects.get(id=pk)
       context= {
        'categories':categories,
        'objectifs':objectifs,
        'questions':questions,
        'evaluation':evaluation
       }   
       return render(request, 'modifier.html',context)
    
    
def dashboard(request):
    answers= Answer.objects.all()
    dictionnary= {}
    count =0
    for answer in answers:
        evaluation_id= answer.evaluation.nom
        maturite_dict = ast.literal_eval(answer.maturite) #parse string into dictionnary without using json
        count += sum(1 for value in maturite_dict.values() if value == '4')
        results= round((count/97)*100,2) #round() took 2 numbers after gamma
        dictionnary[evaluation_id]=results
        
    dictionnary_key=list(dictionnary.keys())
    dictionnary_value=list(dictionnary.values())
        
    context={
        'dictionnary_key': dictionnary_key,
        'dictionnary_value':dictionnary_value
        #'evaluation_id':evaluation_id,
    }
    return render(request, 'dashboard.html', context)

    
def answerEvaluation(request,pk):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        category_id = request.POST.get('category_id')
        #select_maturite= request.POST.get('maturite')
        
        question = Question.objects.get(pk=question_id)
        category = Category.objects.get(pk=category_id)
        evaluations = Evaluation.objects.get(id=pk)
        answers= Answer.objects.get(id_answer=pk)
        
        answer_text= {}
        select_maturite= {}
        for qst in category.question_set.all():
            #dictionary with question IDs as keys and the selected radio button values as values.
            #To get acess of specefic question using ID as key-> answer_text[question_id]
            answer_text[qst.id_question]= request.POST.get('answer_{}'.format(qst.id_question))
            select_maturite[qst.id_question]= request.POST.get('maturite_{}'.format(qst.id_question))
        
        answer = Answer.objects.create(
              question=question,
              category=category,        
              answer=answer_text,
              maturite=select_maturite,
              evaluation=evaluations,
            )
        
        return redirect('modifier',pk=pk)
    #return render(request, 'modifier.html')
    
def questionnaire(request):
    return render(request, 'modifier.html')

def home(request):
    return render(request, 'home.html')

def answerchatgpt(request):
    qst = request.POST.get('question') #Get input from user
    response=openai.Completion.create(
    model="text-davinci-002",
    prompt=qst,
    temperature=0.7,
    max_tokens=200,
    n=1,
    stop=["Human:", "AI:"]
    )
    text= response['choices'][0]['text']
    answer={'answer':text} #dictionary
    return render(request, 'answer.html',answer)
 
def avancement(request):
    #moyenne_chapitre
    categories = Category.objects.all()  
    questions= Question.objects.all()
    evaluations= Evaluation.objects.all()
    evaluation_data=[]
    
    for evaluation in evaluations:
     category_average = {}
     for category in categories:
        #answers = Answer.objects.filter(evaluation__nom="DNSSI4", category_id=category)
        answers= Answer.objects.filter(evaluation_id=evaluation, category_id=category)
        sum_poids_maturite=0
        sum_poids=0
        for answer in answers:
         maturite_dict= ast.literal_eval(answer.maturite)
         maturite_values= maturite_dict.values()
          
         for question in questions:
            poid= question.poids
            sum_poids_maturite += sum(poid* int(maturite) for maturite in maturite_values)
            sum_poids += sum(poid for _ in maturite_values)
        moyenne= round(sum_poids_maturite/sum_poids,2) if sum_poids !=0 else 0
        category_average[category.names] = moyenne
     evaluation_data.append({
            'evaluation': evaluation.nom,
            'category_averages': category_average,
        })        
     
     
     #score for each evaluation
    donut_data=[]
    for evaluation in evaluations:
        category_results={}
        for category in categories:
            answers= Answer.objects.filter(evaluation_id=evaluation, category_id=category)
            #filter(evaluation_id=evaluation, category_id=category)
            count_values=0
            count_questions=0
            for answer in answers:
                #evaluation= answer.evaluation.nom
                answer_dict= ast.literal_eval(answer.answer)
                answer_values= answer_dict.values()
                answer_keys= answer_dict.keys()
                count_values+= sum(1 for value in answer_values if value=='oui')
                count_questions+= len(answer_keys)
                results= round((count_values/count_questions)*100,2) if count_questions != 0 else 0
                category_results[category.category_name]= results
        #category_name=list(category_results.keys())
        #category_result=list(category_results.values())
        donut_data.append({
            'evaluation':evaluation.nom,
            'category_results':category_results,
        })

    
    context = {
        #moyenne_chapitre
        'evaluation_data':evaluation_data,
        'evaluations':evaluations,
        #score
        'donut_data':donut_data,
        
    }
    
    return render(request, 'avancement.html', context)



def rapport(request):
    answers = Answer.objects.all().distinct() 
    for answer in answers:
        answer_str= answer.answer #get dictionary from answer field
        answer_dict = ast.literal_eval(answer_str)  # Convert the string to a dictionary
        
        
        category= answer.category
        evaluation= answer.evaluation
        
        for question, response in answer_dict.items():
            if question is not None and response is not None:
               rapport= Rapport(question=question, response=response, category= category.category_name, evaluation=evaluation.nom)
               rapport.save()
        
    return redirect('evaluation')
        
        
def rapportExcel(request):
    data= Rapport.objects.filter(evaluation="dnssi3")
    
    workbook= openpyxl.Workbook()
    worksheet= workbook.active
    
    headers=['Chapitre','Question','Réponse']
    #'Catwgory_ID','Evaluation_ID'
    worksheet.append(headers)
    
    for item in data:
        row=[
            item.category,
            item.question, 
            item.response, 
        ]
        worksheet.append(row)
        
    response= HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=exportData.xlsx'
    
    workbook.save(response)
    return response
    
    
def exportExcel(request):
    return render(request, 'exportExcel.html')


def plan(request):
    plans = Plan.objects.all()
    return render(request, 'plan.html',{'plans':plans})


def ajouterPlan(request):
    if request.method=='POST':
        chapitre= request.POST.get('chapitre').lower()
        action= request.POST.get('action')
        responsable= request.POST.get('responsable')
        dateD= request.POST.get('dateD')
        dateF= request.POST.get('dateF')
        budget= request.POST.get('budget')
        
        plan = Plan()
        plan.chapitre=chapitre
        plan.action=action
        plan.responsable=responsable
        plan.date_debut=dateD
        plan.date_fin=dateF
        plan.budget=budget
        plan.save()
        return redirect("plan")
    
    return render(request, 'ajouterPlan.html')

def supprimerPlan(request,pk):  
    plan = Plan.objects.get(id=pk) 
    plan.delete() 
    return redirect('plan')

def editPlan(request,pk):
    plans = Plan.objects.get(id=pk)
    return render(request, 'editPlan.html',{'plans':plans})

def updatePlan(request,pk):
    plans= Plan.objects.get(id=pk)
    if request.method=='POST':
        plans.chapitre= request.POST['chapitre'].lower()
        plans.action= request.POST['action']
        plans.responsable= request.POST['responsable']
        plans.date_debut= datetime.strptime(request.POST['dateD'], '%Y-%m-%d')
        plans.date_fin= datetime.strptime(request.POST['dateF'], '%Y-%m-%d')
        plans.budget= request.POST['budget']
        plans.save()
        return redirect('plan')
    else:
        return render(request, 'editPlan.html', {'plan': plan})

        
    #return render(request, 'plan.html',{'plans':plans})  


def all_plans(request):
    plans= Plan.objects.all()
    out=[]
    for plan in plans:
        out.append({
            'title': plan.chapitre,
            'id': plan.id,
            'start':plan.date_debut.strftime("%Y-%m-%d "),
            'end': plan.date_fin.strftime("%Y-%m-%d "),
        })
    return JsonResponse(out, safe=False)

#{}
#pour calendrier
def add_plan(request):
    start= request.GET.get("start",None)
    end= request.GET.get("end",None)
    title= request.GET.get("title",None)
    plans= Plan(chapitre=str(title), date_debut=start, date_fin= end)
    plans.save()
    data={}
    return JsonResponse(data)

def email(request):
    if request.method == "POST":
        email_recepteur = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        if email_recepteur and subject and message:
            sender_email = 'najouaelfethi@gmail.com'
            recipient_list = [email_recepteur]

            send_mail(
                subject=subject,
                message=message,
                from_email=sender_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )
        else:
         print("try again")
        
    return render(request, 'email.html')

def profil(request): 
    profil = Profil.objects.get(id=2)
    context = {
        'profil': profil
    }
    return render(request, 'profil.html', context)

    
    




    
    


    

        
        
    


    

    

    
    
   
   
       







            
    
        

    
 




   
       



