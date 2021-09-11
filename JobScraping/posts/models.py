from django.db import models

# Create your models here.


class internshala(models.Model):
    title = models.TextField()
    validThrough = models.TextField()
    applicantLocationRequirement = models.TextField()
    hiringOrganization = models.TextField()
    employmentType = models.TextField()
    directApply = models.BooleanField()
    jobLocation = models.TextField()
    datePosted = models.TextField()
    responsibilities = models.TextField()
    salaryCurrency = models.TextField()
    baseSalary = models.TextField()
    description = models.TextField()
    organizationURL = models.TextField()
    category = models.TextField()


class iimjobs(models.Model):
    description = models.TextField()
    title = models.TextField()
    industry = models.TextField()
    experienceRequirements = models.TextField()
    skills = models.TextField()
    datePosted = models.TextField()
    validThrough = models.TextField()
    hiringOrganization = models.TextField()
    employmentType = models.TextField()
    qualifications = models.TextField()
    jobLocation = models.TextField()


class talentrack(models.Model):
    datePosted = models.TextField()
    description = models.TextField()
    employmentType = models.TextField()
    industry = models.TextField()
    validThrough = models.TextField()
    baseSalary = models.TextField()
    jobLocation = models.TextField()
    hiringOrganization = models.TextField()
    occupationalCategory = models.TextField()
    title = models.TextField()


class interesting_urls(models.Model):
    BASE = models.TextField()
    URL = models.TextField()


class non_interesting_urls(models.Model):
    BASE = models.TextField()
    URL = models.TextField()
