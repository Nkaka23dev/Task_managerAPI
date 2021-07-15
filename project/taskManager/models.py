from django.db import models

class Project(models.Model):
    projectName=models.CharField(max_length=100)
    DateOfStart=models.DateField()
    projectSize=models.IntegerField()

    def __str__(self):
        return f"{self.projectName}"