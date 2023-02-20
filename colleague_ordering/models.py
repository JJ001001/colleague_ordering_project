from django.db import models

# Create your models here. for connection to the db

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title #returns positon title, not number

class Colleague(models.Model):
    firstname = models.CharField(max_length=100)
    sirname = models.CharField(max_length=100)
    colleagueID = models.CharField(max_length=8)
    jobfamily = models.ForeignKey(Position, on_delete=models.CASCADE) #TODO not sure what this means?
    status = models.CharField(max_length=100)

class Equipment(models.Model):
    itemID = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    #add more models/tables here

    #to execute changes and apply new models to db, use below commands
    #python manage.py makemigrations colleague_ordering
    #python manage.py sqlmigrate colleague_ordering 0001
    #python manage.py migrate
