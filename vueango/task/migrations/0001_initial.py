# Generated by Django 4.0.4 on 2022-05-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'todo'), ('done', 'done')], default='todo', max_length=10)),
            ],
        ),
    ]
