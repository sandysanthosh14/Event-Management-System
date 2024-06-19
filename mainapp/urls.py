from django.contrib import admin
from django.conf import settings
from django.urls import path,include
#from .views import EventCategoryListView,EventCategoryCreateView
from .views import EventCategoryListView ,EventCreateview, Event_list, home,join,account,emailmsg
from .import views
from django.conf.urls.static import static
urlpatterns = [
    path('category-list/', EventCategoryListView.as_view(), name='event-category-list'),
    #path('create-category/',EventCategoryCreateView.as_view(), name='create-event-category'),
    #path('EventAPIView/',EventAPIView.as_view(), name='your-model-list-create'),
    #path('EventAPIView/<int:pk>/',EventAPIView.as_view(), name='your-model-retrieve-update-destroy'),
    path('create-event/',EventCreateview.as_view(), name='event-create'),
    path('event-list/',Event_list.as_view(), name='event-list'),
    path('',views.home, name='index'),
    path('join/<str:ename>/',views.join, name='join'),
    path('myaccount/<int:pk>',views.account, name='account'),
    path('sentemail/',views.emailmsg, name='emailsent')
    
    
]