from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.
class SoftDeleteAndTimeAbstract(SoftDeletableModel, TimeStampedModel):
	pass

class ChatRoom(SoftDeleteAndTimeAbstract):
	eid = models.CharField(max_length=100, unique=True)

class ChatMessage(SoftDeleteAndTimeAbstract):
	room = models.ForeignKey(ChatRoom)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	text = models.TextField()

	def to_data(self):
		return dict(
			id = self.id,
			sender = self.user,
			date = self.created.isoformat(),
			text = self.text)


