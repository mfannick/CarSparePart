from django.db import models

# Create your models here.

class SpareParts(models.Model):
    nameChoose=(('Head lights','Head lights'),
        ('Brake lights','Brake lights'),
        ('Tail lights','Tail lights'),
        ('Tail gate','Tail gate'),
        ('Mirrors','Mirrors'),
        ('Hoods','Hoods'),
        ('Window','Window'),
        ('Door','Door'),
        ('Tire','Tire'),
        ('Petrol tank','Petrol tank'),
        ('Roof','Roof'),
        ('Steering wheel','Steering wheel'),
        ('Engine','Engine'),
        
    )
    namePart=models.CharField(max_length=40,choices=nameChoose)
    price=models.IntegerField()
    locationChoose=(
        ('Gatsata','Gatsata'),
        ('Nyamirambo','Nyamirambo'),
        ('Remera','Remera'),
        ('Nyabugogo','Nyabugogo'),
        )
    locationPart=models.CharField(max_length=40,choices=locationChoose)
    ImagePart=models.ImageField(upload_to='spareparts/')
    Phone=models.IntegerField()

    def __str__(self):
        return self.namePart


class CarCategory(models.Model):
    categoryName=(
        ('Toyota','Toyota'),
        ('Cross country','Cross country'),
        ('Vox wagen','Vox wagen'),
        ('Suzuki','Suzuki'),
        ('Mahindra','Mahindra'),
        ('Honda','Honda'),
        ('Hyunda','Hyunda'),
        ('Volvo','Volvo'),
        ('Daihatsu','Daihatsu'),
        
    )
    categoryPart=models.CharField(max_length=40,choices=categoryName)
    spareParts = models.ManyToManyField(SpareParts)

    def __str__(self):
        return self.categoryPart