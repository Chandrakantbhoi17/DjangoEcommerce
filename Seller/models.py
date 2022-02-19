

from django.db import models

class SellerSlider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='seller_slider_img')
	url = models.CharField(max_length=200, default = "#", null=True)
	def save(self,*args, **kwargs):
		super().save(*args, **kwargs)
		img=IMAGE.open(self.image.path)
		if img.height > 1024 or img.width >1024:
			outputsize=(1024,1024)
			img.thumbnail(outputsize)
			img.save(self.image.path)

class Category(models.Model):
	category_name=models.CharField(max_length=100)
	def __str__(self) -> str:
		return str(self.category_name)


class SubCategory(models.Model):
	category_name=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
	sub_category_name=models.CharField(max_length=100)
	def __str__(self):
		return self.sub_category_name

	

class Product(models.Model):
	prod_id1=models.BigAutoField(primary_key=True)
	prod_id2=models.CharField(max_length=100,default='')
	
	GST_CHOICES = (("0",'0'),("3",'3'),("5",'5'),("12",'12'),("18",'18'),("28",'28'))
	subcategory=models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)
	price=models.IntegerField(default=0)
	price_not=models.IntegerField(default=999)
	desc=models.TextField()
	gst=models.CharField(default='0',max_length=3,choices=GST_CHOICES)
	img=models.ImageField(upload_to='products/images',default='',null=True)
	





		