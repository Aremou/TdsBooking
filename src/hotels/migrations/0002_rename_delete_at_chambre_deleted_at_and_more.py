# Generated by Django 4.0.4 on 2022-12-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chambre',
            old_name='delete_at',
            new_name='deleted_at',
        ),
        migrations.RenameField(
            model_name='chambre',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='payement',
            old_name='add_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='add_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='delete_at',
            new_name='deleted_at',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='chambre',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='payement',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='is_delete',
        ),
        migrations.AddField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categoryequipment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chambre',
            name='equipments',
            field=models.ManyToManyField(to='hotels.equipment'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='hotel_id',
            field=models.IntegerField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='equipments',
            field=models.ManyToManyField(to='hotels.equipment'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image_chambre',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image_chambre',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image_hotel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image_hotel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payement',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
