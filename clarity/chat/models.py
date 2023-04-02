from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class ChatRoom(models.Model):
	type = models.CharField(max_length=10, default='DM')
	member = models.ManyToManyField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return  str(self.name)

class ChatMessage(models.Model):
	chat = models.ForeignKey(ChatRoom, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	message = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message
