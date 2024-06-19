from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import EventSerializer
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import EventCategory,membership,Event_join,Event
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from .serializers import EventCategorySerializer
from .forms import Eventform,Eventlistform

# Create your views here.

'''class EventCategoryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = EventCategory
    fields = ['name', 'code', 'image', 'priority', 'status']
    template_name = 'create_event_category.html'
    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)'''
"""class EventCategoryCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)"""


"""class EventAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [AllowAny]  # Adjust the permissions according to your requirements

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""
class EventCategoryListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = EventCategory
    permission_classes = [IsAdminUser]
    template_name = 'event_category.html'
    context_object_name = 'event_category'
class EventCreateview(LoginRequiredMixin,CreateView):
    login_url='login'
    models=Event
    form_class=Eventform
    permission_classes = [IsAuthenticated]
    template_name='create_event.html'
    success_url = reverse_lazy('event-list')
class Event_list(LoginRequiredMixin,ListView):
    login_url='signup'
    #permission_classes = [IsAuthenticated]
    template_name='Event_list.html'
    context_object_name='combined_list'
    success_url = reverse_lazy('event-list')
    def get_queryset(self):
        queryset1=Event.objects.all()
        combined_list={
            "events":list(queryset1)
        }
        print(combined_list)
        return combined_list
    
    


def home(request):
    # Your view logic here
    return render(request, 'index.html')
class Event_join(LoginRequiredMixin,ListView):
    login_url='login'
    model=membership
    template_name='event_join.html'
    context_object_name='member'
    success_url=reverse_lazy('event-list')

def join(request,ename):
    event = get_object_or_404(Event, ename=ename)
    registered=request.user.events.filter(ename=ename).exists()
    context={'event':event,'registered':registered}
    print(registered)
    if request.method=='POST':
        event.attendees.add(request.user)
        print(event)
        emailmsg(request,event)
    
        return HttpResponse("User successfully joined the event.")
        
    return render(request,'join.html',context=context)


def call():
    s=Event.objects.get(pk=pk)
    t=User.objects.get(name=ename)
    for item1, item2 in s,t:
        Event_join.objects.create(
            name=item2,
            event=item1
        )
    return render(request,'joinform.html')
def account(request,pk):
    account=get_object_or_404(User,pk=pk)

    return render(request,'account.html',context={'account':account})

from django.core.mail import send_mail
def emailmsg(request,event):
    subject = 'Registeration comfirm'
    message = 'Thank you for registering for the event: {}'.format(event.ename)
    useremail=[request.user.email]
    from_email = 'santhosh9965791286@gmail.com'
    recipient_list = useremail
    print(recipient_list)
    print(message)
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('successfully sent emailmessage')

    

