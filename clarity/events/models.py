from django.db import models
from django.urls import reverse
from django .conf import settings
from community.models import Community

class Event(models.Model):
    title = models.CharField(max_length=255) # The title of the Event
    content = models.TextField() # The main content of the Event
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events') # The author of the event
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='community') # The community of the author of the event
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the event was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the event was last updated
    image = models.ImageField(upload_to='events_images/') # A mandatory image for the event
    applied_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='applied_event', null=True, blank=True) # A ManyToMany field that tracks which users have applied to  the event
    place = models.CharField(max_length=200, blank=True, null=True)  # new field for the event place
    is_online = models.BooleanField(default=False)  # new field to indicate if the event is online or not

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk}) # Returns the URL to the detail view of the event
    
class ApplyToEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='apply_to_event') # The user who applied to the event
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event') # The event that the user applied to
    applied = models.BooleanField(default=False)
    applied_at = models.DateTimeField(auto_now_add=True) # The date and time the user applied to the event
