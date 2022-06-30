from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver


#this funtion will create a secodary course choice whenever a new course is added
@receiver(post_save, sender=Course)
def create_secondary_course(sender, instance, created, **kwargs):
    if created:
        Secondary_course.objects.create(course=instance)


#___APPLICATION FORM SIGNALS____


#this funtion will save a profile whenever an application is created
@receiver(post_save, sender=Application)
def create_application_componets(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(application=instance)
        Contact.objects.create(application=instance)
        Kin.objects.create(application=instance)
        Employer.objects.create(application=instance)
        Outstanding_result.objects.create(application=instance)
        Language.objects.create(application=instance)
        Post_acadmic_qualification.objects.create(application=instance)
        School_leaving.objects.create(application=instance)
        School_leaving_subject.objects.create(application=instance)
        Sponsor.objects.create(application=instance)
        TermsAndConditions.objects.create(application=instance)
        Document.objects.create(application=instance)
