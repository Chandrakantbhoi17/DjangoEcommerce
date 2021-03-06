# Generated by Django 3.2.8 on 2022-02-16 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SellerSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='seller_slider_img')),
                ('url', models.CharField(default='#', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=100)),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Seller.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id1', models.BigAutoField(primary_key=True, serialize=False)),
                ('prod_id2', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('price_not', models.IntegerField(default=999)),
                ('desc', models.TextField()),
                ('gst', models.CharField(choices=[('0', '0'), ('3', '3'), ('5', '5'), ('12', '12'), ('18', '18'), ('28', '28')], default='0', max_length=3)),
                ('img', models.ImageField(default='', null=True, upload_to='products/images')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Seller.subcategory')),
            ],
        ),
    ]
