# Generated by Django 3.1.4 on 2020-12-16 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='email')),
                ('brandName', models.CharField(max_length=50, verbose_name='brandName')),
                ('login_type', models.CharField(default='brand', max_length=50, verbose_name='login_type')),
                ('owner', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('W', 'Women'), ('M', 'Men'), ('B', 'Both')], max_length=1)),
                ('locationID', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
    ]
