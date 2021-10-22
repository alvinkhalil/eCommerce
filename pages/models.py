from django.db import models
from django.db.models.fields import TextField
from ckeditor.fields import RichTextField


# Create your models here.
STATUS2 = (
    ("active","Paylaşılıb"),
    ("passive","Paylaşılmayıb")
)

STATUS = (
    ("active","Baxılmayıb"),
    ("passive","Baxılıb")
)

class ContactUsModel(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=100, verbose_name="Mövzu")
    message = models.TextField(verbose_name="Mesaj")
    status = models.CharField(choices=STATUS, max_length=20, default = "active",blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"

class LocationModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Adı")
    location = models.CharField(max_length=1000,verbose_name="Ünvan")
    phone = models.CharField(max_length=200,verbose_name="Telefon")
    email = models.EmailField()
    facebook = models.CharField(max_length=1000,blank=True)
    twitter = models.CharField(max_length=1000,blank=True)
    linkedin = models.CharField(max_length=1000,blank=True)
    youtube = models.CharField(max_length=1000,blank=True)
    instagram = models.CharField(max_length=1000,blank=True)
    status = models.CharField(choices = STATUS2,default="passive",max_length=100)
    main = models.BooleanField(verbose_name='Əsas səhifədə göstərilsin?')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.name

    class Meta:
        verbose_name = "Ünvan"
        verbose_name_plural = "Ünvan və Telefonlar"

class AboutUs(models.Model):
    
    title = models.CharField(verbose_name="Başlıq",max_length=100)
    text = RichTextField(verbose_name="Mətin")
    status = models.CharField(max_length=100,default="passive",choices=STATUS2)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = "Haqqımızda"

class Carousel(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    image = models.ImageField(upload_to = "images/carousel/",verbose_name='Şəkil')
    status = models.CharField(choices=STATUS2, max_length=100,default="passive")
    is_show = models.BooleanField(verbose_name="Yalnız sağda göstərilsin")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Örtük şəkili"
        verbose_name_plural = "Örtük şəkilləri"
