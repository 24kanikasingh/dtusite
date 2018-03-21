# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Teacher
from .forms import RateForm


def index(request):
    latest_teacher_list = Teacher.objects.all()
    context = {'latest_teacher_list': latest_teacher_list}
    return render(request, 'computer/computer_faculty.htm', context)

def detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
##    if request.method == "POST":
##        submit(request,teacher_id)
    return render(request, 'computer/details.htm', {'teacher': teacher})

def results(request, teacher_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % teacher_id)

def vote(request, teacher_id):
    #return HttpResponse("You're voting on question %s." % teacher_id)
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'computer/form.htm', {'teacher': teacher})

def submit(request,teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
##    #if request.user.is_superuser:
##        #return render(request,"home.html") 
##    if ('yes').checked  in request.POST:
##        teacher.votes=teacher.votes+1
##        #return render(request, 'computer/details.htm', {'teacher': teacher}) 
##        return views.detail(request,teacher_id)
##        #elif 'choix2'  in request.POST:
##            #return HttpResponse("hedha ltemps")
##        #elif 'choix3'  in request.POST:
##            #return views.index(request)
##    else :
##        return HttpResponse("You have not chosenn ay choice")
##    #else:
##        #return views.index(request)
    h_type = request.POST.get('q1')
    if h_type == 'yes':
        teacher.votes=teacher.votes+1

def get_form(request,teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    noq=3
    t=0.0
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            h_type = request.POST.get('att')
            if h_type == 'yes':
               t=t+1.0
            s_type = request.POST.get('syll')
            if s_type == 'yes':
               t=t+1.0   
            t_type = request.POST.get('time')
            if t_type == 'a':
               t=t+1.0  
            elif t_type == 's':    
                t=t+0.5
            te_type = request.POST.get('teach_aids')
            if te_type == 'a':
               t=t+1.0  
            elif te_type == 's':    
                t=t+0.5
            a_type = request.POST.get('avail')
            if a_type == 'yes':
               t=t+1.0
            teacher.votes=(teacher.votes+(t*100/noq))/2
            teacher.save()   
            # redirect to a new URL:
            #return HttpResponseRedirect('/computer/'+teacher_id)
            return render(request, 'computer/details.htm', {'teacher': teacher})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RateForm()

    return render(request, 'computer/form.htm', {'form': form,'teacher':teacher})        
