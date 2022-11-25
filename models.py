from django.db import models


class ToDoList(models.Model):
    activity_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    #status = models.CharField(max_length=10)

    def __str__(self):
        return self.activity_name+' '+self.description


