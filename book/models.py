from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()


class Publishers(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Books(models.Model):
    GENRE_CHOICES = [('FIC','fiction') , ('HIS','history') , ('SCI','science') , ('ROM','romance')]
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES)
    price = models.DecimalField()
    author = models.ForeignKey(Authors,related_name= 'books', on_delete = models.CASCADE, max_length=50) 
    publisher = models.ForeignKey(Publishers, related_name ='books',on_delete = models.CASCADE ,max_length=50)
