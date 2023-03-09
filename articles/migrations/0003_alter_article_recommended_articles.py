# Generated by Django 4.0 on 2021-12-22 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_author_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='recommended_articles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended', to='articles.article'),
        ),
    ]
