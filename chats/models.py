from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.
class SoftDeleteAndTimeAbstract(SoftDeletableModel, TimeStampedModel):
	pass

class Thread(SoftDeleteAndTimeAbstract):
	eid = models.CharField(max_length=100, unique=True)

class ChatMessage(SoftDeleteAndTimeAbstract):
	room = models.ForeignKey(Thread, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField()

	def to_data(self):
		return dict(
			id = self.id,
			sender = self.user,
			date = self.created.isoformat(),
			text = self.text)


