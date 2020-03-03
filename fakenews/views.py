from django.shortcuts import render
from django.shortcuts import redirect
import predict_pickle
from newspaper import Article

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Url
from .models import Vote

from django.http import JsonResponse
from django.core import serializers

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'fakenews/signup.html', {'form': form})

# Create your views here.
def home(request):
    return render(request, 'fakenews/home.html' , {})

def classify(request):
    if request.method== "POST":
        result,features=predict_pickle.classify(request.POST['title'],request.POST['article'])

        print(result)
        print(features[0])

    return render(request, "fakenews/classify.html", {'result' : result, 'wordcount': features[0][0], 'titlecount':features[0][1], 'punccount': features[0][2], 'gunningfog': features[0][4], 'readability':features[0][5]})

def classify_url(request):
    if request.method=="POST":
        newsurl=request.POST['newsurl']
        stored = Url.objects.filter(Url__exact=newsurl)
        if stored:
            stored=stored[0]
            print("already processed")
            return render(request, "fakenews/classify.html", {'articleimage': stored.imgurl ,'articletitle': stored.Title, 'articletext': stored.Text, 'result': stored.Classification})
        article=Article(newsurl)
        article.download()
        article.parse()
        image=article.top_image
        print(article.title)
        print(article.text)
        result, features = predict_pickle.classify(article.title, article.text)
        u1 = Url(Url=newsurl,Title=article.title,Text=article.text,Classification=result,imgurl=image)
        u1.save()
        return render(request, "fakenews/classify.html", {'articleimage':image , 'articletitle': article.title, 'articletext': article.text,'result': result, 'wordcount': features[0][0], 'titlecount':features[0][1], 'punccount': features[0][2], 'gunningfog': features[0][4], 'readability':features[0][5]})
def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    title

@login_required
def voting_view(request):
    urls = Url.objects.all()
    votes = request.user.url_set.all()
    print(votes)
    for r in votes:
        print(r.Url)
    return render(request,"fakenews/voting.html",{'urls':urls,'votes':votes})

def upvote(request):
    id = request.GET.get('id')
    u1 = Url.objects.get(pk=id)
    cur_user= request.user.id
    voted= Vote.objects.filter(url=u1,user=cur_user)
    print(voted)
    if voted:
        if voted[0].Dislike==True:
            u1.Dislikes-=1
            u1.Likes+=1
            u1.save()
            if (u1.Dislikes + u1.Likes) > 0:
                u1.Rating = u1.Likes / (u1.Dislikes + u1.Likes)
                u1.save()
                data = u1.Rating
            else:
                data = 0
            voted[0].Dislike=False
        voted[0].Like=True
        voted[0].save()
        data=u1.Rating
        return JsonResponse(data, safe=False)

    u1.Likes+=1
    u1.save()
    if (u1.Dislikes+u1.Likes) > 0:
        u1.Rating = u1.Likes/(u1.Dislikes+u1.Likes)
        u1.save()
        data = u1.Rating
    else:
        data=0
    v=Vote(url=u1,user=request.user,Like=True)
    v.save()
    return JsonResponse(data,safe=False)
def downvote(request):
    id = request.GET.get('id')
    u1 = Url.objects.get(pk=id)
    cur_user = request.user.id
    voted = Vote.objects.filter(url=u1, user=cur_user)
    print(voted)
    if voted:
        if voted[0].Like == True:
            u1.Likes -= 1
            u1.Dislikes += 1
            u1.save()
            if (u1.Dislikes + u1.Likes) > 0:
                u1.Rating = u1.Likes / (u1.Dislikes + u1.Likes)
                u1.save()
                data = u1.Rating
            else:
                data = 0
            voted[0].Like = False
        voted[0].Dislike = True
        voted[0].save()
        data = u1.Rating
        return JsonResponse(data, safe=False)

    u1.Dislikes += 1
    u1.save()
    if (u1.Dislikes + u1.Likes) > 0:
        u1.Rating = u1.Likes / (u1.Dislikes + u1.Likes)
        u1.save()
        data = u1.Rating
    else:
        data = 0
    v = Vote(url=u1, user=request.user, Dislike=True)
    v.save()
    return JsonResponse(data, safe=False)