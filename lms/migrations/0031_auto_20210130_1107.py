# Generated by Django 3.1.4 on 2021-01-30 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0030_auto_20210130_1100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('quiz', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='studentquestion',
            unique_together={('quiz', 'question')},
        ),
    ]
