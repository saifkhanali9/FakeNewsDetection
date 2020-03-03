from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns = [
    path('',views.home, name="home"),
    path('classify', views.classify, name="classify"),
    path('classifyurl', views.classify_url, name="classifyurl"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup, name="signup"),
    path('voting', views.voting_view, name="voting"),
    path('ajax/upvote', views.upvote, name="upvote"),
    path('ajax/downvote', views.downvote, name="downvote"),
]