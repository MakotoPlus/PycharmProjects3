# Generated by Django 2.2.7 on 2019-11-16 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicantctl', '0004_m_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_applicant_info',
            name='deparment_1_text',
        ),
        migrations.RemoveField(
            model_name='t_applicant_info',
            name='deparment_2_text',
        ),
        migrations.RemoveField(
            model_name='t_applicant_info',
            name='deparment_3_text',
        ),
        migrations.RemoveField(
            model_name='t_applicant_info',
            name='key_appl_route',
        ),
        migrations.RemoveField(
            model_name='t_applicant_info',
            name='key_history_kbn',
        ),
    ]