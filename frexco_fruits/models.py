from django.db import models
from uuid import uuid4

# Create your models here.

class Region(models.Model):
  id_region = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)


class Fruit(models.Model):
  id_fruit = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=255)
  region = models.ForeignKey(Region, related_name="region_fruit", on_delete=models.SET_NULL, null=True, blank=True)