# Generated by Django 4.0.4 on 2022-05-06 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('premium', models.IntegerField(choices=[('FREE', 0), ('PREMIUM', 1)], default=0)),
                ('due_date', models.DateField(null=True)),
            ],
        ),
    ]