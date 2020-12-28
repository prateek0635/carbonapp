from django.urls import path,include
from carbonapp import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('completeprofile',views.comp_prof, name='comp_prof'),
    path('postpic',views.postpic, name='postpic'),
]
