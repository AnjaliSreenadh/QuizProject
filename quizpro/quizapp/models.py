from django.db import models
# Create your models here.

class Question(models.Model):
	que=models.CharField(max_length=200)
	opt1=models.CharField(max_length=100)
	opt2=models.CharField(max_length=100)
	opt3=models.CharField(max_length=100)
	opt4=models.CharField(max_length=100)
	corr_ans=models.CharField(max_length=100)
	mark=models.IntegerField(default=0)


class User(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)
	is_staff = models.BooleanField(default=True)

	def __str__(self):
		return self.username