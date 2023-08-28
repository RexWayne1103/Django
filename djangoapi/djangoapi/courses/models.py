from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Members(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)