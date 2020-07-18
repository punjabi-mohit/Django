from django.shortcuts import render,get_object_or_404
from .models import Notes
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Notes
from .forms import NotesForm
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.


# class NotesListView(ListView):
#         template="notes/notes_list.html"
#         model=Notes

#         def get_context_data(self,*args,**kwargs):
#                 notes_list=Notes.objects.filter(owner=User)

def show_notes(request):
        note=Notes.objects.filter(owner=request.user)
        context={'object_list':note}
        return render(request,'notes/notes_list.html',context)






def create_note(request):
        form=NotesForm(request.POST or None)
        context={'form':form}
        if form.is_valid():
                lb=form.cleaned_data.get('label')
                bd=form.cleaned_data.get('body')
                t=Notes(owner=request.user,label=lb,body=bd)
                t.save()
                return redirect("home")
        else:
                form=NotesForm()
        return render(request,'notes/addnote1.html',context)


