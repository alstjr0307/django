# Generated by Django 3.1.5 on 2021-03-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210308_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('F', '해외주식'), ('D', '국내주식'), ('R', '자유게시판')], default='F', max_length=1, verbose_name='게시판'),
        ),
    ]
