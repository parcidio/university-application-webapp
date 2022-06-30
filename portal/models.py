from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from django.forms import CharField, FileField
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django import forms
from ckeditor.fields import RichTextField

#CHOICES
PROGRAMME_LEVEL = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
]
TERTIARY_AUTHORITY = [
    ('NQA', 'Namibia Qualification Authority'),
]
MODE_OF_STUDY = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Online', 'Online'),
]

COURSE_CATEGORY = [
    ('Shortcourse', 'Shortcourse'),
    ('Undergraduate', 'Undergraduate'),
    ('Postgraduate', 'Postgraduate'),
]

BASE_ON_LEVEL = [('Grade-11', 'Grade-11'), ('Grade-12', 'Grade-12'),
                 ('Mature-age', 'Mature age'),
                 ('Other-qualitication', 'Other Qualitication')]

STATUS_OF_APPLICATION = [
    ('In progress', 'In progress'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
    ('Cancelled', 'Cancelled'),
]

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
PERMIT_TYPE = [
    ('Study', 'Study'),
    ('Work', 'Work'),
    ('Diplomatic', 'Diplomatic'),
    ('Tourism', 'Tourism'),
]
CONDITIONAL_ANSWER = [
    ('YES', 'YES'),
    ('NO', 'NO'),
    ('MAYBE', 'MAYBE'),
]
CONDITIONAL_ANSWER_BINARY = [
    ('NO', 'NO'),
    ('YES', 'YES'),
]
TITLE = [
    ('MR', 'MR'),
    ('MS', 'MS'),
    ('MRS', 'MRS'),
    ('DR', 'DR'),
]

MARITAL_STATUS = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorsed', 'Divorsed'),
    ('Separated', 'Separated'),
    ('Widowed', 'Widowed'),
]

RELATIONSHIP_TYPE = [
    ('Parent', 'Parent'),
    ('Spouse', 'Spouse'),
    ('Guardian', 'Guardian'),
]

SPONSORSHIP_TYPE = [
    ('Self Sponsored', 'Self Sponsored'),
    ('Sponsored by a Third-party', 'Sponsored by a Third-party'),
]

NAMIBIAN_REGION = [
    ('Erongo', 'Erongo'),
    ('Hardap', 'Hardap'),
    ('Karas', 'Karas'),
    ('Khomas', 'Khomas'),
    ('Kunene', 'Kunene'),
    ('Kavango East', 'Kavango East'),
    ('Kavango West', 'Kavango West'),
    ('Otjozondjupa', 'Otjozondjupa'),
    ('Oshana', 'Oshana'),
    ('Oshikoto', 'Oshikoto'),
    ('Omusati', 'Omusati'),
    ('Zambezi', 'Zambezi'),
    ('Omaheke', 'Omaheke'),
    ('Ohangwena', 'Ohangwena'),
]

LANGUAGE = [
    ('English', 'English'),
    ('Oshiherero', 'Oshiherero'),
    ('Damara / Nama', 'Damara / Nama'),
    ('AfriKaans', 'AfriKaans'),
    ('Portuguese', 'Portuguese'),
    ('French', 'French'),
    ('Spanish', 'Spanish'),
    ('German', 'German'),
    ('Russian', 'Russian'),
    ('Chinise / Mandarine', 'Chinise / Mandarine'),
    ('Other', 'Other'),
]


#UNIVERSITY TABLES
class Faculty(models.Model):
    dean = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,
                                         blank=True,
                                         null=True)
    updation_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Programme(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=3,
                             choices=PROGRAMME_LEVEL,
                             blank=True,
                             null=True)
    authority = models.CharField(max_length=50,
                                 choices=TERTIARY_AUTHORITY,
                                 blank=True,
                                 null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.authority) + " (" + str(
            self.level) + ")"


class Course(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    course_code = models.CharField(max_length=10, blank=True, null=True)
    level = models.ForeignKey(Programme,
                              on_delete=models.SET_NULL,
                              max_length=100,
                              blank=True,
                              null=True)
    mode_of_study = MultiSelectField(choices=MODE_OF_STUDY,
                                     blank=True,
                                     null=True)
    tuition_fee = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    credits = models.PositiveIntegerField(blank=True, null=True)
    number_years = models.PositiveIntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,
                                         blank=True,
                                         null=True)
    updation_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Secondary_course(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Campus(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    campus_code = models.CharField(max_length=10, blank=True, null=True)
    contact = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    country = CountryField(blank_label='(select country)', default="NA")
    town = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True,
                                         blank=True,
                                         null=True)
    updation_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    lecturer = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 default="unavailable",
                                 blank=True,
                                 null=True)
    faculty = models.ForeignKey(Faculty,
                                on_delete=models.CASCADE,
                                default="unavailable",
                                blank=True,
                                null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    subject_code = models.CharField(max_length=50, blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    credits = models.PositiveIntegerField(blank=True, null=True)
    subject_outline = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.subject_code) + " - " + str(self.name)


#APPLICATION TABLES
class Application(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)
    programme = models.ForeignKey(Programme,
                                  on_delete=models.SET('deleted'),
                                  blank=True,
                                  null=True)
    course_first_choice = models.ForeignKey(Course,
                                            on_delete=models.SET('deleted'),
                                            blank=True,
                                            null=True)
    course_second_choice = models.ForeignKey(Secondary_course,
                                             on_delete=models.SET('deleted'),
                                             blank=True,
                                             null=True)

    category = MultiSelectField(max_length=50,
                                choices=COURSE_CATEGORY,
                                blank=True,
                                null=True)
    prefered_campus = models.ForeignKey(Campus,
                                        on_delete=models.SET('deleted'),
                                        blank=True,
                                        null=True)
    based_on_level = models.CharField(max_length=50,
                                      choices=BASE_ON_LEVEL,
                                      blank=True,
                                      null=True)
    other_level = models.CharField(max_length=100, blank=True, null=True)
    current_step = models.SmallIntegerField(default=0, blank=True, null=True)

    prefered_period = models.CharField(
        max_length=50,
        choices=MODE_OF_STUDY,
        default='Full-time',
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_OF_APPLICATION,
        default=STATUS_OF_APPLICATION[0],
    )
    creation_date = models.DateTimeField(auto_now_add=True,
                                         blank=True,
                                         null=True)
    submition_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return "owner: " + str(self.owner) + " | programme: " + str(
            self.category) + "   " + str(self.status)


class Profile(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    nationality = CountryField(blank_label='(select country)', default="NA")
    namibian_region = models.CharField(choices=NAMIBIAN_REGION,
                                       default=NAMIBIAN_REGION[0],
                                       max_length=50,
                                       null=True)
    title = models.CharField(
        choices=TITLE,
        default=TITLE[0],
        max_length=10,
    )
    gender = models.CharField(
        choices=GENDER,
        default=GENDER[0],
        max_length=10,
    )
    full_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    marital_status = models.CharField(
        choices=MARITAL_STATUS,
        default=MARITAL_STATUS[0],
        max_length=10,
    )
    id_number = models.PositiveIntegerField(blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)
    permit_number = models.PositiveIntegerField(blank=True, null=True)
    permit_type = models.CharField(
        choices=PERMIT_TYPE,
        default=PERMIT_TYPE[0],
        max_length=30,
    )
    permit_expiry_date = models.DateField(blank=True, null=True)
    has_medical_condition = models.CharField(
        choices=CONDITIONAL_ANSWER_BINARY,
        default='NO',
        max_length=20,
    )
    has_medical_needs = models.CharField(
        choices=CONDITIONAL_ANSWER_BINARY,
        default='NO',
        max_length=20,
    )
    medical_condition_description = models.TextField(max_length=500,
                                                     blank=True,
                                                     null=True)

    def __str__(self):
        return str(self.application)


class Contact(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    cellphone_number_1 = models.PositiveIntegerField(blank=True, null=True)
    cellphone_number_2 = models.PositiveIntegerField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    namibia_postal_address = models.CharField(max_length=15,
                                              blank=True,
                                              null=True)
    namibia_residential_address = models.TextField(max_length=100,
                                                   blank=True,
                                                   null=True)
    origin_postal_address = models.CharField(max_length=15,
                                             blank=True,
                                             null=True)
    origin_residential_address = models.TextField(max_length=100,
                                                  blank=True,
                                                  null=True)

    def __str__(self):
        return str(self.application)


class Kin(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    kin_title = models.CharField(
        choices=TITLE,
        default=TITLE[0],
        max_length=10,
    )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    kin_id_number = models.CharField(max_length=50, blank=True, null=True)
    relationship_type = models.CharField(
        choices=RELATIONSHIP_TYPE,
        default=RELATIONSHIP_TYPE[0],
        max_length=15,
    )
    kin_email = models.EmailField(max_length=50, blank=True, null=True)
    kin_cellphone_number = models.PositiveIntegerField(blank=True, null=True)
    kin_telephone = models.PositiveIntegerField(blank=True, null=True)

    kin_residential_address = models.TextField(max_length=100,
                                               blank=True,
                                               null=True)
    kin_postal_address = models.CharField(max_length=15, blank=True, null=True)
    kin_occupation = models.CharField(max_length=50, blank=True, null=True)
    Work_telephone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.application)


class Employer(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    employer_name = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    employer_telephone = models.PositiveIntegerField(blank=True, null=True)
    employer_email = models.EmailField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duties = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.application)


class Outstanding_result(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    has_out_standing_exam = models.CharField(
        choices=CONDITIONAL_ANSWER_BINARY,
        default='NO',
        max_length=20,
    )
    out_standing_exam = models.CharField(max_length=50, blank=True, null=True)
    out_standing_exam_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.application)


class Language(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    school_language = models.CharField(
        choices=LANGUAGE,
        default=LANGUAGE[0],
        max_length=50,
    )
    home_language = models.CharField(
        choices=LANGUAGE,
        default=LANGUAGE[0],
        max_length=50,
    )
    has_english_course = models.CharField(
        choices=CONDITIONAL_ANSWER_BINARY,
        default="NO",
        max_length=20,
    )
    english_course = models.CharField(max_length=50, blank=True, null=True)
    applying_english_course = models.CharField(
        choices=CONDITIONAL_ANSWER_BINARY,
        default="NO",
        max_length=20,
    )

    def __str__(self):
        return str(self.application)


class Post_acadmic_qualification(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    has_past_qualification = models.CharField(
        choices=CONDITIONAL_ANSWER_BINARY,
        default='NO',
        max_length=20,
    )
    institution_name = models.CharField(max_length=50, blank=True, null=True)
    location = CountryField(blank_label='(select country)',
                            default="NA",
                            blank=True,
                            null=True)
    post_qualification = models.CharField(max_length=100,
                                          blank=True,
                                          null=True)
    year_start = models.PositiveBigIntegerField(blank=True, null=True)
    year_end = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.application)


class School_leaving(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    school_name = models.CharField(max_length=100, blank=True, null=True)
    highest_grade = models.CharField(max_length=10, blank=True, null=True)
    exam_year = models.PositiveSmallIntegerField(blank=True, null=True)
    exam_authority = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.application)


class School_leaving_subject(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    school = models.ForeignKey(School_leaving,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    subject_name = models.CharField(max_length=30, blank=True, null=True)
    subject_level = models.CharField(max_length=15, blank=True, null=True)
    symbol = models.CharField(max_length=1, blank=True, null=True)
    point = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.application)


class Sponsor(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       default="unavailable")
    sponsor_name = models.CharField(max_length=100, blank=True, null=True)
    sponsor_signatory_name = models.CharField(max_length=100,
                                              blank=True,
                                              null=True)
    sponsorship_type = models.CharField(
        choices=SPONSORSHIP_TYPE,
        max_length=50,
        default='Self Sponsored',
    )
    sponsor_postal_address = models.CharField(max_length=30,
                                              blank=True,
                                              null=True)
    sponsor_cellphone = models.PositiveIntegerField(blank=True, null=True)
    sponsor_telephone = models.PositiveIntegerField(blank=True, null=True)
    sponsor_email = models.EmailField(max_length=50, blank=True, null=True)
    tuition_fee = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    registration_fee = models.DecimalField(max_digits=10,
                                           decimal_places=2,
                                           blank=True,
                                           null=True)
    student_fund = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       blank=True,
                                       null=True)

    total_fee = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    null=True)

    def __str__(self):
        return str(self.application)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/application_documents/{1}'.format(
        instance.application.owner.username, filename)


class Document(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True)
    medical_documents = models.FileField(upload_to=user_directory_path,
                                         blank=True,
                                         null=True)
    certified_id_copy = models.FileField(upload_to=user_directory_path,
                                         blank=True,
                                         null=True)
    passport_photo = models.FileField(upload_to=user_directory_path,
                                      blank=True,
                                      null=True)
    evidence_of_payment = models.FileField(upload_to=user_directory_path,
                                           blank=True,
                                           null=True)
    foreign_qualification = models.FileField(upload_to=user_directory_path,
                                             blank=True,
                                             null=True)
    foreign_qualification_translation = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    namibia_highest_qualification_copy = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    other_documents = models.FileField(upload_to=user_directory_path,
                                       blank=True,
                                       null=True)

    def __str__(self):
        return str(self.application)


class TermsAndConditions(models.Model):
    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True)
    title = models.CharField(max_length=200, blank=True, null=False)
    general_rule = RichTextField(blank=True, null=False)
    application_form_acknowledgement = models.BooleanField(default=False)

    def __str__(self):
        return str(self.application) + " - " + str(self.title)
