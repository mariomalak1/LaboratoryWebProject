from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.http import Http404
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

    def __str__(self):
        return self.name

    def clean(self):
        try:
            if int(self.building) <= 0 or int(self.floor) <= 0 or int(self.PCsNumber) <= 0 or int(self.ChairsNumber) <= 0:
                raise ValidationError("Please Enter Value Greater Than Zero")
        except:
            raise ValidationError("Please Enter Value")

class Pc(models.Model):
    STATUS = (("Active", "Active")
        , ("Under Maintenance", "Under Maintenance"))
    pcId = models.PositiveIntegerField()
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    status = models.CharField(choices= STATUS, max_length=20)

    class Meta:
        unique_together = ('pcId', 'lab')

    def __str__(self):
        return str(self.pcId) + " | " + str(self.lab.name)

class Report(models.Model):
    PROBLEM_TYPE = (("Software", "Software"),
        ("Hardware", "Hardware"))
    # reportId = models.PositiveSmallIntegerField(unique=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    pcNumber = models.ForeignKey(Pc, on_delete=models.CASCADE)
    date = models.DateField()
    problemType = models.CharField(choices=PROBLEM_TYPE, max_length=20)
    description = models.TextField()

    # class Meta:
    #     unique_together = ('reportId', 'lab')


@receiver(post_save, sender=Lab)
def create_pc_objects(sender, instance, created, **kwargs):
    if created:
        # Create PC objects based on PCsNumber field in Lab
        for i in range(instance.PCsNumber):
            pc = Pc.objects.create(pcId=i+1, lab=instance, status='Active')

@receiver(pre_save, sender = Lab)
def update_pc_objects(sender, instance, **kwargs):
    try:
        original_lab = Lab.objects.get(pk=instance.id)  # Get the original lab object before the update
        original_pc_count = original_lab.PCsNumber
        new_pc_count = instance.PCsNumber

        if original_pc_count < new_pc_count:
            # Add PCs for the increased count
            for i in range(original_pc_count + 1, new_pc_count + 1):
                Pc.objects.create(pcId=i, lab=instance, status='Active')
        elif original_pc_count > new_pc_count:
            # Delete excess PCs for the decreased count
            Pc.objects.filter(pcId__gt=new_pc_count, lab=instance).delete()
    except:
        pass

