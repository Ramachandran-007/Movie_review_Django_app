from django.shortcuts import render
from .forms import MovieForm, CommentForm
from .models import MovieModel, CommentModel
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addmovie/')

    context = {'form':form}
    return render(request,'addmovie.html',context)

def home_view(request):
    data = MovieModel.objects.all()

    context = {'data':data}
    return render(request,'home.html',context)

@login_required(login_url='/login/')
def review_view(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            
    data = MovieModel.objects.get(id = id)
    form = CommentForm(initial={'movie':id,'user':request.user})
    comments = CommentModel.objects.filter(movie = id)

    context = {'data':data,'form':form,'comments':comments}
    return render(request,'review.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')