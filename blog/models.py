from django.db import models
from django.utils import timezone

# The first line defines our model. 
# Post is the name of the model. models.Model means that this is a Django model 
# so that Django knows that is should be saved to the database.
class Post(models.Model):
	# Ok, now we're defining the properties that we're working with.
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title