from django.db import models

class ComputerBrand (models.Model):
    brand_name= models.CharField(max_length=30)
    logo= models.ImageField(null=True, upload_to="uploadimages/")

    def __str__(self):
        return self.brand_name


class ComputerGeneration (models.Model):
    generation= models.CharField(max_length=20, unique=True)
    price_min= models.IntegerField()
    price_max= models.IntegerField()
    RAM= models.IntegerField()
    brands= models.ForeignKey(ComputerBrand,on_delete=models.CASCADE)

    def __str__(self):
        return self.generation


class Computer (models.Model):
    computer_code=models.CharField(max_length=30, unique=True)
    computer= models.ForeignKey(ComputerGeneration, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    unit_rate= models.IntegerField()
    total_price= models.FloatField()

    def __str__(self):
        return self.computer_code
