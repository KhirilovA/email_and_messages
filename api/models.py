from django.db import models
from django.utils import timezone

from api.validators import validate_email, validate_message

class Message(models.Model):
	email = models.TextField(validators=[validate_email])
	message = models.TextField(validators=[validate_message])
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if self.pk:
			self.updated = timezone.now()
		return super().save(*args, **kwargs)