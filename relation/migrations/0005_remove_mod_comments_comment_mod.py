# Generated by Django 4.1.4 on 2023-11-27 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0004_remove_comment_mod_mod_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='mod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relation.mod'),
        ),
    ]
