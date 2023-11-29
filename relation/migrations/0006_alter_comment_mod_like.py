# Generated by Django 4.1.4 on 2023-11-27 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0005_remove_mod_comments_comment_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='mod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='relation.mod'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField()),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relation.comment')),
            ],
        ),
    ]