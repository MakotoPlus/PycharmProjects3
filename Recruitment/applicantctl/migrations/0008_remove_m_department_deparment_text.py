# Generated by Django 2.2.7 on 2019-11-16 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicantctl', '0007_t_judgment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='m_department',
            name='deparment_text',
        ),
    ]