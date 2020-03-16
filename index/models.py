from django.db import models


class GmtModel(models.Model):
    gmt_update = models.DateTimeField(auto_now=True)
    gmt_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.
class Activity(GmtModel):
    name = models.CharField(max_length=128)
    hold_date = models.DateField(null=False)
    form = models.CharField(max_length=64)

    def __str__(self):
        return "Activity{name={}, hold_date={}, form={}}".format(self.name, self.hold_date, self.form)
