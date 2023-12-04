from django.db.models import (Model,
                              CharField,
                              IntegerField,
                              ForeignKey,
                              CASCADE,
                              DecimalField,
                              FileField,
                              Index)


class ModelA(Model):
    file = FileField(upload_to="uploads/%Y/%m/%d/")
    name = CharField(max_length=20, blank=True)
    roll = IntegerField(blank=True)
    city = CharField(max_length=20, blank=True)

    class Meta:
        indexes = [Index(fields=['roll'])]


class ModelB(Model):
    percentage = DecimalField(max_digits=5, decimal_places=2, blank=True)
    subject = CharField(max_length=20, blank=True)
    sport = CharField(max_length=20, blank=True)
    name = ForeignKey(ModelA, on_delete=CASCADE, related_name='nested', blank=True)
