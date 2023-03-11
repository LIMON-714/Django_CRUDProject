from django.urls import path
from .views import*
urlpatterns = [
   path('',singup, name= 'singup'),
   path('login/',loginPage, name= 'login'),
   path('home/',home, name= 'home'),
   path('logout/',LogoutPage,name='logout'),
   path('account/',account,name='account'),
   path('update/<int:id>/',update,name='update'),
   path('profile/<int:id>/',profilePage,name='profile'),
   path('delete/<int:id>/',DeleteProfile,name='delete'),
   
]
