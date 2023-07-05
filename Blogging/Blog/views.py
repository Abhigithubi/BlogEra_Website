import form as form
from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import User
from django.shortcuts import render, redirect
from Blog import models
from Blog.forms import RegForm
from .models import blog
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, "home.html")

"""def home(request):
    context = {
          'blogs': blog.objects.all()
        }
    return render(request, 'home.html', context)"""

class BlogListView(ListView):
    model = blog
    template_name = 'home.html'
    context_object_name = 'blogs'
    ordering = ["-date_of_blog"]

class BlogDetailView(DetailView):
    model = blog
    template_name = 'details.html'

class BlogCreateView(CreateView):
    model = blog
    fields = ['title', 'content']
    template_name = 'blog_form.html'

"""def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except:
                pass
    else:
        form = RegForm()

    return render(request, "signup.html", {"for": form})

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj_user=models.Customer.objects.filter(username=username, password=password)
        if obj_user:
            request.session['Customer']= username
            return redirect('yes')
        error="Incorrect username or password"
    return render(request, 'login.html', locals())

def yes(request):
    if 'Customer' in request.session:
        store = request.session['Customer']
        return render(request, "home.html", {'key': store})
    else:
        return render(request, 'login.html')"""


    #if request.method=="POST":
       # username=request.POST.get('username')
        #contact=request.POST.get('contact')
        #password = request.POST.get('password')
        #email=request.POST.get('email')
        #user_list=models.signup.objects.filter(username=username)
        #error_name=[]
        #if user_list:
         #   error_name='This user is already available'
          #  return render(request,'signup.html', {'error_name':error_name})
        #else:
         #   user_name=models.signup.objects.create(username=username, contact=contact, password=password, email=email)
          #  user_name.save()
        #return redirect('login')
    #return render(request,'signup.html')
