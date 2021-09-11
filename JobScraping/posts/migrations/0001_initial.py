# Generated by Django 3.2.6 on 2021-09-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iimjobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.TextField()),
                ('industry', models.TextField()),
                ('experienceRequirements', models.TextField()),
                ('skills', models.TextField()),
                ('datePosted', models.TextField()),
                ('validThrough', models.TextField()),
                ('hiringOrganization', models.TextField()),
                ('employmentType', models.TextField()),
                ('qualifications', models.TextField()),
                ('jobLocation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='interesting_urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BASE', models.TextField()),
                ('URL', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='internshala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('validThrough', models.TextField()),
                ('applicantLocationRequirement', models.TextField()),
                ('hiringOrganization', models.TextField()),
                ('employmentType', models.TextField()),
                ('directApply', models.BooleanField()),
                ('jobLocation', models.TextField()),
                ('datePosted', models.TextField()),
                ('responsibilities', models.TextField()),
                ('salaryCurrency', models.TextField()),
                ('baseSalary', models.TextField()),
                ('description', models.TextField()),
                ('organizationURL', models.TextField()),
                ('category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='non_interesting_urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BASE', models.TextField()),
                ('URL', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='talentrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePosted', models.TextField()),
                ('description', models.TextField()),
                ('employmentType', models.TextField()),
                ('industry', models.TextField()),
                ('validThrough', models.TextField()),
                ('baseSalary', models.TextField()),
                ('jobLocation', models.TextField()),
                ('hiringOrganization', models.TextField()),
                ('occupationalCategory', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
    ]