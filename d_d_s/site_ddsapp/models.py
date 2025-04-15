from django.db import models

# Create your models here.

class Status(models.Model):
    """Модель статуса """   
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Статус'
    

class Type(models.Model):
    """Модель типа движения денежных средств."""

    name = models.CharField(max_length=100, unique=True)    

    def __str__(self):
            return self.name
        
    class Meta:
        verbose_name = 'Тип'

class Category(models.Model):
     """Модель категориию"""
     type = models.ForeignKey(Type, on_delete=models.CASCADE,related_name='categories')
     name = models.CharField(max_length=250, unique=True)

     def __str__(self):
          return f"{self.type}: {self.name}"
     
     class Meta:
      verbose_name = 'Категория'       
      verbose_name_plural = 'Категории'

class Subcategory(models.Model):
    """Модель подкатегории."""

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f"{self.category}: {self.name}"
    
    class Meta:
        verbose_name = 'Под-категория'
        verbose_name_plural = 'Под-категории'

       

class Record_dds(models.Model):
    data_create = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    summa = models.DecimalField(max_digits=12, decimal_places=2)  
    comment = models.CharField(max_length=1500, blank=True, null=True) 

    def __str__(self):
        return f"{self.data_create} | {self.status} | {self.summa} RUB"
    
    class Meta:
        verbose_name = 'Денежная операция'
        verbose_name_plural = 'Денежные операции'


   