from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('explore/', views.explore, name="explore"),
    path('info/<str:pk>/', views.info, name="info"),
    path('logout/', views.logoutuser, name='logout'),
    path('listt/', views.listt, name="listt"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    #path('update/<str:pk>', views.update, name='update'),
    path('profile/',views.profile , name="profile"),
    path('redirectt/', views.redirectt, name='redirectt'),
]
