from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class EventCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=6, unique=True)
    image = models.ImageField(upload_to='event_category/')
    priority = models.IntegerField(unique=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
        #return reverse('event-category-list')
class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    ename = models.CharField(max_length=255, unique=True)
    attendees = models.ManyToManyField(User,related_name='events')
    uid = models.PositiveIntegerField(unique=True)
    location = models.CharField(max_length=255)
    #job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    select_scheduled_status = (
        ('yet to scheduled', 'Yet to Scheduled'),
        ('scheduled', 'Scheduled')
    )
    scheduled_status = models.CharField(max_length=25, choices=select_scheduled_status)
    venue = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    points = models.PositiveIntegerField()
    maximum_attende = models.PositiveIntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('time out', 'Time Out'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=status_choice, max_length=10)
    def __str__(self):
        return self.ename

class membership(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    status=(
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('time out', 'Time Out'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),)
    status_choice=(
        ('waiting', 'Waiting'),
        ('attending', 'Attending'),
        ('completed', 'Completed'),
        ('absent', 'Absent'),
        ('cancelled', 'Cancelled'),
    )
    attended_status=models.CharField(choices=status_choice,max_length=10)
    joining_date=models.DateField(auto_now_add=True)
class Event_join(models.Model):
    name=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    event=models.ManyToManyField(Event)

