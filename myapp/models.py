from math import fabs
# from django.db import models
import uuid
from django.contrib.gis.db import models



# Create your models here.
# class UploadFiles(models.Model):
#     ID =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     file = models.FileField()

#     def __str__ (self):
#         return str(self.ID)


class Files(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    file= models.FileField()

    def __str__(self):
        return str(self.id)        


# class ULPIN(models.Model):
#     id =models.AutoField(primary_key=True)
#     P_ID=models.CharField(max_length=20)
#     geometry=models.PolygonField()
#     centroid=models.PointField()
#     ULPIN=models.CharField(max_length=20)

class MyPIN(models.Model):
    pid =models.CharField(max_length=20)
    geometry=models.PolygonField()
    centroid=models.PointField()
    upin=models.CharField(max_length=20)


class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    district= models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10,decimal_places=8)
    longitude = models.DecimalField(max_digits=10,decimal_places=8)
    ULPIN = models.CharField(max_length=20) 