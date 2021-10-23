from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.deletion import CASCADE
from pages.models import STATUS2
from taggit.managers import TaggableManager

# Create your models here.
size = (
    ("color_s","S"),
    ("color_m","M"),
    ("color_l","L"),
    ("color_xl","XL"),
    ("color_xxl","XXL"),
)

color = (
    ("white","Ağ"),
    ("black","Qara"),
    ("yellow","Sarı"),
    ("green","Yaşıl"),
    ("brown","Qəhvəyi"),
    ("blue","Göy"),
    ("red","Qırmızı"),
)

class Product_Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    slug = models.SlugField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Tarix")
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

class Product_Item(models.Model):
    
    category = models.ForeignKey(Product_Category, on_delete=CASCADE)
    name = models.CharField(max_length=100,verbose_name="Ad")
    price = models.FloatField(verbose_name="Qiymət")
    stock = models.IntegerField(verbose_name="Miqdarı")
    size = models.BooleanField(verbose_name="Ölçü S")
    size2 = models.BooleanField(verbose_name="Ölçü M")
    size3 = models.BooleanField(verbose_name="Ölçü L")
    size4 = models.BooleanField(verbose_name="Ölçü X")
    size5 = models.BooleanField(verbose_name="Ölçü XL")
    specifcation = models.TextField(verbose_name="Tanımlama")
    color = models.BooleanField(verbose_name="Rəng Qırmızı")
    color2 = models.BooleanField(verbose_name="Rəng Yaşıl")
    color3 = models.BooleanField(verbose_name="Rəng Sarı")
    color4 = models.BooleanField(verbose_name="Rəng Qara")
    color4 = models.BooleanField(verbose_name="Rəng Ağ")
    color6 = models.BooleanField(verbose_name="Rəng Göy")
    color7 = models.BooleanField(verbose_name="Rəng Qəhvəyi")
    description = RichTextField(verbose_name = "Məlumat")
    image1 = models.ImageField(upload_to = "images/products/",verbose_name="Şəkil")
    image2 = models.ImageField(upload_to = "images/products/",verbose_name="Şəkil",blank=True, null=True)
    image3 = models.ImageField(upload_to = "images/products/",verbose_name="Şəkil",blank=True, null=True)
    image4 = models.ImageField(upload_to = "images/products/",verbose_name="Şəkil",blank=True, null=True)
    image5 = models.ImageField(upload_to = "images/products/",blank=True, null=True,verbose_name="Şəkil")
    status = models.CharField(max_length=100,choices=STATUS2,default = "passive")
    slug = models.SlugField(blank=True, null=True)
    tags = TaggableManager()

    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Əlavə olunma tarixi")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"