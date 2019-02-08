from django.db import models

# Create your models here.
class Author(models.Model):


    author_fname = models.CharField(max_length=50)
    author_lname = models.CharField(max_length=50)
    rating_user = models.FloatField()

    def __str__(self):
        return self.author_fname+ " "+ self.author_lname
class Books(models.Model):

    author_id = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=50)
    category_choices =(('Suspense','Suspense'),('Horror','Horror'),('Fiction','Fiction'))
    category = models.CharField(max_length=50, choices= category_choices)
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    year = models.DateField()
    rating_user = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.title


