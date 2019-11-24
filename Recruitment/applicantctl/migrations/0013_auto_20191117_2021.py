# Generated by Django 2.2.7 on 2019-11-17 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicantctl', '0012_auto_20191117_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Judgment',
            fields=[
                ('key_judgment', models.AutoField(primary_key=True, serialize=False)),
                ('judgment_text', models.CharField(max_length=100, verbose_name='判定内容')),
                ('u_user', models.CharField(max_length=100, verbose_name='更新者')),
                ('u_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.AddField(
            model_name='t_judgment',
            name='judgment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='applicantctl.M_Judgment', verbose_name='判定'),
        ),
    ]
