# Generated by Django 4.0.4 on 2022-12-15 16:29

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('first_img', models.ImageField(blank=True, null=True, upload_to='images/chambre/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp'])])),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/chambre', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('slug', models.SlugField(blank=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('overnight', models.PositiveIntegerField()),
                ('area', models.PositiveIntegerField()),
                ('beds', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('delete_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='hotels.category')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_img', models.ImageField(blank=True, null=True, upload_to='images/hotel/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp'])])),
                ('slug', models.SlugField(blank=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tel_1', models.CharField(max_length=100)),
                ('tel_2', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(blank=True, max_length=100, null=True)),
                ('star_nbr', models.PositiveIntegerField()),
                ('ville', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/hotel', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('status', models.CharField(choices=[('EAP', 'En attente de paiement'), ('EC', 'En cours'), ('AN', 'Annulée'), ('T', 'Termineé')], default='EAP', max_length=200)),
                ('add_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('delete_at', models.DateTimeField(blank=True, null=True)),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.chambre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_method', models.CharField(choices=[('card', 'Carte de Crédit'), ('momo', 'Mobile Money'), ('paypal', 'Paypal')], default='card', max_length=200)),
                ('transaction_id', models.CharField(max_length=700)),
                ('add_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='images/hotel/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp'])])),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Chambre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='images/chambre', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp'])])),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.chambre')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(default=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.categoryequipment')),
                ('hotel', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
            ],
        ),
        migrations.AddField(
            model_name='chambre',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotels.hotel'),
        ),
    ]
