from django.db import models

# Create your models here.
class MovieModel(models.Model):
    title = models.CharField(max_length=40)
    release_date = models.DateField()
    reviewed_on = models.DateField()
    story = models.TextField()
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    review = models.TextField()
    poster = models.ImageField(upload_to='movies')

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    user = models.CharField(max_length=30)
    comment = models.TextField()
    user_rating = models.DecimalField(max_digits=2,decimal_places=1)
    comment_date = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(MovieModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.user