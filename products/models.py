from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('Category', verbose_name='parent' , blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True , upload_to="categories/")
    is_enable = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to="products/")
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category' , verbose_name='categories' , blank=True )

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductsFile(models.Model):
    product = models.ForeignKey('Product' , verbose_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(blank=True, upload_to="files/%Y/%m/%d/")
    is_enable = models.BooleanField(default=True)

    class Meta:
        db_table = 'file'
        verbose_name = 'File'
        verbose_name_plural = 'Files'

