# Generated by Django 3.2.9 on 2022-01-11 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('hood_name', models.CharField(max_length=60)),
                ('hood_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('hood_location', models.CharField(max_length=120)),
                ('occupants_count', models.IntegerField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('hood', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('business_email', models.EmailField(max_length=254)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('business_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hood', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood', to='hood.neighbourhood')),
            ],
        ),
    ]
