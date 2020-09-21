from django.db import models

def store_image(instance, filename):
	return './'.join(['images', filename])

def mp3(instance, filename):
	return './'.join(['musics',filename])


class Album(models.Model):
	singer = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	logo = models.FileField(blank=True, null=True, upload_to=store_image)

	def __str__(self):
		return self.singer + " - " + self.title 



class Song(models.Model):
	title = models.CharField(max_length=50)
	file_type = models.CharField(max_length=50)
	file = models.FileField(blank=True, null=True, upload_to=mp3)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
