from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Lab(models.Model):
    STATUS = (("Active", "Active")
        , ("Under Maintenance", "Under Maintenance"))
    name = models.CharField(max_length=80)
    building = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    PCsNumber = models.PositiveSmallIntegerField()
    ChairsNumber = models.PositiveSmallIntegerField()
    status = models.CharField(choices=STATUS, max_length=20)


    def clean(self):
        if self.building <= 0 or self.floor <= 0 or self.PCsNumber <= 0 or self.ChairsNumber <= 0:
            raise ValidationError("Please Enter Value Greater Than Zero")


class Pc(models.Model):
    STATUS = (("Active", "Active")
        , ("Under Maintenance", "Under Maintenance"))
    pcId = models.PositiveIntegerField()
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    status = models.CharField(choices= STATUS, max_length=20)

    class Meta:
        unique_together = ('pcId', 'lab')


class Report(models.Model):
    PROBLEM_TYPE = (("Software", "Software"),
        ("Hardware", "Hardware"))
    reportId = models.PositiveSmallIntegerField(unique=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    pcNumber = models.ForeignKey(Pc, on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    problemType = models.CharField(choices=PROBLEM_TYPE, max_length=20)
    description = models.TextField()

    class Meta:
        unique_together = ('reportId', 'lab')
