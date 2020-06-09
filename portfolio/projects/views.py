from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project,Message
from django.views.generic import TemplateView,ListView
from projects import forms

# def index(request):
#     return HttpResponse("Hello world")

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "BASIC_INJECTION"
        return context

def projects(request):
    project_list = Project.objects.order_by('title')
    project_dict = {'project_list' : project_list }
    return render(request,'projects.html',context=project_dict)

def contact(request):
    form = forms.ContactForm()
    if(request.method=='POST'):
        form = forms.ContactForm(request.POST)
        if(form.is_valid()):
            # print("Name :"+form.cleaned_data['name'])
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            new_msg = Message(name=name,email=email,text=text)
            new_msg.save()
    return render(request,'contact.html',{'form':form})
