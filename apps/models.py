from django.db import models

# Create your models here.
from django.db import models

class DataModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Unit(models.Model):
    name = models.CharField(max_length=255)

class WebSales(models.Model):
    url = models.URLField(max_length=500)

class MusicEvent(models.Model):
    version = models.CharField(max_length=100)
    uid = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    show_unit = models.ForeignKey(Unit, related_name="show_unit", on_delete=models.CASCADE)
    description_filter_html = models.TextField()
    discount_info = models.TextField()
    image_url = models.URLField(max_length=500)
    master_unit = models.ForeignKey(Unit, related_name="master_unit", on_delete=models.CASCADE)
    sub_unit = models.ForeignKey(Unit, related_name="sub_unit", null=True, blank=True, on_delete=models.CASCADE)
    support_unit = models.ForeignKey(Unit, related_name="support_unit", null=True, blank=True, on_delete=models.CASCADE)
    other_unit = models.ForeignKey(Unit, related_name="other_unit", null=True, blank=True, on_delete=models.CASCADE)
    web_sales = models.ForeignKey(WebSales, on_delete=models.CASCADE)
    source_web_promote = models.URLField(max_length=500, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    edit_modify_date = models.DateTimeField()
    source_web_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hit_rate = models.IntegerField()
    show_info = models.TextField()
    time = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    locationName = models.CharField(max_length=100)
    on_sales = models.BooleanField()
    price = models.CharField(max_length=255)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title