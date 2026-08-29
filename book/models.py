from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __repr__(self):
        return f'first name :{self.first_name}, last name: {self.last_name}'


class Publishers(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __repr__(self):
            return f"publisher's name :{self.name}, city name: {self.city}"


class Books(models.Model):
    GENRE_CHOICES = [('FIC','fiction') , ('HIS','history') , ('SCI','science') , ('ROM','romance')]
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    publication_date = models.DateField(null=True)
    author = models.ForeignKey(Authors,related_name= 'books', on_delete = models.CASCADE, max_length=50) 
    publisher = models.ForeignKey(Publishers, related_name ='books',on_delete = models.CASCADE ,max_length=50)

    def __repr__(self):
            return f'title :{self.title}'
