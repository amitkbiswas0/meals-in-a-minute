# Generated by Django 3.1.4 on 2021-01-04 08:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1024, verbose_name='Title')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('location', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Barisal', 'Barisal'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet'), ('Mymensingh', 'Mymensingh')], max_length=255, verbose_name='Location')),
                ('category', models.CharField(choices=[('bengali_food', 'Homemade Bengali Food'), ('street_food', 'Street Food'), ('sea_food', 'Sea Food'), ('drinks', 'Drinks and Juices'), ('sweets', 'Sweets and Pithas'), ('bakery', 'Cakes and Bakery')], max_length=256, verbose_name='Food Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='ads', verbose_name='Photo')),
                ('available_from', models.DateTimeField(auto_now_add=True, verbose_name='Available from')),
                ('available_till', models.DateTimeField(verbose_name='Available till')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sellerprofile', verbose_name='Seller')),
            ],
            options={
                'verbose_name': 'advertisement',
                'verbose_name_plural': 'advertisements',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miam.advertisement', verbose_name='Advertisement')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.buyerprofile', verbose_name='Buyer')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
