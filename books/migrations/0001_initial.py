# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('year', models.CharField(max_length=10)),
                ('pages', models.CharField(max_length=10)),
                ('filesize', models.CharField(max_length=20)),
                ('file_format', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdfs/%Y/%m/%d')),
                ('image', models.FileField(upload_to='images/%Y/%m/%d')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='BookHasAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookHasCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
            options={
                'verbose_name_plural': 'Book has categories',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('books', models.ManyToManyField(through='books.BookHasCategory', to='books.Book')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='bookhascategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='books.BookHasAuthor', to='books.Author'),
        ),
        migrations.AlterUniqueTogether(
            name='bookhascategory',
            unique_together=set([('book', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookhasauthor',
            unique_together=set([('author', 'book')]),
        ),
    ]
