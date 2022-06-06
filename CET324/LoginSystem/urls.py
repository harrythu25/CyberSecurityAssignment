from django.urls import path
from . import views


urlpatterns = [    
     path('', views.home),
    path('home/', views.home),
    path('streams/', views.streams),
    path('IndividualStream/<int:sport_id>/', views.IndividualStream, name="IndividualStream"),
    path('user/', views.user),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('categories/', views.categories, name="categories"),



]
