from django.shortcuts import render
import os
import openai

# Create your views here.
#{}
openai.api_key="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"

def home(request):
    return render(request, 'home.html')

def answer(request):
    qst = request.POST.get('question') #Get input from user
    response=openai.Completion.create(
    model="text-davinci-002", #model
    prompt=qst,
    temperature=0.7, #to control randomness of responses
    max_tokens=200, #control max length of responses
    n=1,
    stop=None
    )
    text= response['choices'][0]['text']
    answer={'answer':text} #dictionary
    return render(request, 'navheader.html',answer)


