# Generated by Django 3.1 on 2020-08-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0041_answersclass10_answerscommerce_answersscience'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswersClass10',
        ),
        migrations.DeleteModel(
            name='AnswersCommerce',
        ),
        migrations.DeleteModel(
            name='AnswersScience',
        ),
    ]