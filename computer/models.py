from django.db import models
from django.urls import reverse

class ComputerBrand (models.Model):
    brand_name= models.CharField(max_length=30)
    logo= models.ImageField(null=True, upload_to="uploadimages/")

    def __str__(self):
        return self.brand_name
        # to check self --> id
        # return f'ID:{self.id}, {self.brand_name}'
    
    # You can use this get_absolute_url(self) function, instead of using success_url in CreateView and UpdateView IN views.py
    
    # def get_absolute_url(self):
    #     return reverse("chub:brand-list", kwargs={"pk": self.pk})
    

class ComputerGeneration (models.Model):
    generation= models.CharField(max_length=20, unique=True)
    price_min= models.IntegerField()
    price_max= models.IntegerField()
    RAM= models.IntegerField()
    brands= models.ForeignKey(ComputerBrand,on_delete=models.CASCADE)

    def __str__(self):
        return self.generation
        # to check self--> id
        # return f'ID:{self.id}, {self.generation}'


class Computer (models.Model):
    computer_code=models.CharField(max_length=30, unique=True)
    computer= models.ForeignKey(ComputerGeneration, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    unit_rate= models.IntegerField()
    total_price= models.FloatField()

    def __str__(self):
        return f'selfID:{self.id}--> computer code:{self.computer_code}'
