from django.db import models
from blog import settings
from ckeditor.fields import RichTextField
from markdown import markdown



class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	pub_date = models.DateTimeField()
	text = RichTextField()
	image = models.ImageField(upload_to = "post_imgs", null=True, blank=True, default= "None")
	slug = models.SlugField(max_length=40, blank=True)
	display = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title

	
	class Meta:
		#default ordering
		ordering = ["pub_date"]

	

	



