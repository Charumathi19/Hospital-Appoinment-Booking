from django.contrib import admin
from django.urls import path
from bewellapp import views
#from blogapp.views import New

urlpatterns = [
    path('/',views.firstpage),
    path('home',views.home),
    path('welcome',views.welcome),
    path('itvedant',views.itvedant),
    path('add',views.add),
    path('combine/<data>',views.combine),
    path('mul/<int:x>/<int:y>',views.mul),
    #path('New',views.New.as_view()),
    path('webpage',views.index),
    path('tem',views.tem),
    path('dtl',views.view_html),
    path('dtldata',views.datadtl),
    path('udash',views.func),
    path('loop',views.loop),
    path('about',views.abe),
    path('',views.index),
    path('post',views.po),
    path('contact',views.contact),
    path('cpost',views.create_post),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('appform',views.appform),
    path('ent',views.ent),
    path('ortho',views.ortho),
    path('cardio',views.cardio),
    path('dentist',views.dentist),
    path('emergency',views.emergency),
    #path('view',views.view),
     #path('test',views.test),
    #path('table',views.table)
]