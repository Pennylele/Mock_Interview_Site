from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	PROGRAMMING_LANGUAGES_CHOICES = [
		('PY', 'Python'),
		('JA', 'Java'),
		('JS', 'JavaScript'),
		('C/C++', 'C/C++'),
		('RB', 'Ruby'),
		('GO', 'Go'),
	]
	user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	programming_language = models.CharField(default='Python', max_length=30, choices=PROGRAMMING_LANGUAGES_CHOICES)

	def __str__(self):
		return f'{self.user.username} profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
