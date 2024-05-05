from django.urls import path
from .import views

urlpatterns=[
   # path('add_question/',views.add_que),
    path('exam/',views.quiz_disp,name='quiz_disp'),
    path('result/',views.results_disp),
    path('signup/', views.signup, name='signup'),
    path('login/', views.u_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home', views.home, name='home'),
]


