from django.urls import path
from website.views import HomeView
from . import views
urlpatterns = [
    path('home', HomeView.as_view()),
    path('home/<solution_id>', views.solution_page, name="solution-pg"),
    # path('voting/', views.vote, name='voting'),
    # path('like/', views.like, name="like"),
    # path('uri', HomeView.as_view(), name="upvote"),
    # path('home', views.home, name="home"),
]
