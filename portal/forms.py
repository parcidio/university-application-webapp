import datetime
from tkinter import Widget
from turtle import onclick, width
from django import forms
from django.forms import ChoiceField, ModelForm
from .models import *
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User


class FacultyForm(ModelForm):

    class Meta:
        model = Faculty
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['dean'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'dean'
        }),
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name'
        })


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['faculty'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'dean'
        }),
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name'
        }),
        self.fields['level'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name'
        }),
        self.fields['number_years'].widget.attrs.update({
            'class': 'form-control ',
            'placeholder':
            'minimum number of years required to complete the course',
            'min': '0',
        }),
        self.fields['tuition_fee'].widget.attrs.update({
            'class':
            'form-control',
            'placeholder':
            'tuition fee'
        }), self.fields['credits'].widget.attrs.update({
            'class':
            'form-control',
            'placeholder':
            'totaol number of credits'
        }),
        self.fields['course_code'].widget.attrs.update({
            'class':
            'form-control',
            'placeholder':
            'course code'
        }),


class CampusForm(ModelForm):

    class Meta:
        model = Campus
        fields = '__all__'
        widgets = {'country': CountrySelectWidget()}

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name'
        }), self.fields['campus_code'].widget.attrs.update({
            'class':
            'form-control text-uppercase',
            'placeholder':
            'campus code'
        }),
        self.fields['town'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'town'
        }),
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'address'
        }),
        self.fields['contact'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'contact'
        }),
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name'
        }),
        self.fields['country'].widget.attrs.update({
            'class':
            'form-control country-select-flag',
        })


class SubjectForm(ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name'
        }),
        self.fields['faculty'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'faculty'
        }),
        self.fields['subject_code'].widget.attrs.update({
            'class':
            'form-control',
            'placeholder':
            'subject code',
        }),
        self.fields['lecturer'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'lecturer'
        }),
        self.fields['level'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'level',
            'min': '1',
            'max': '10'
        }),
        self.fields['credits'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'credits',
            'min': '1',
        }),
        # self.fields['subject_outline'].widget.attrs.update({
        #     'class':
        #     'form-control',
        #     'placeholder':
        #     'subject outline'
        # })


# SHORTCOURSE FORMS
class ApplicationsHomeForm(ModelForm):

    class Meta:
        model = Application
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'type': 'Radio'
        }),


class ApplicationsMainForm(ModelForm):

    class Meta:
        model = Application
        fields = [
            'prefered_period', 'course_first_choice', 'prefered_campus',
            'current_step'
        ]
        widgets = {
            'prefered_period':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False,
            }, )
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['course_first_choice'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }),
        self.fields['prefered_campus'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False
        }),
        self.fields['current_step'].widget.attrs.update({
            'class': 'form-control d-none save_changes',
            'required': False
        }),


class ProfileApplicationsForm(ModelForm):
    # date_of_birth = forms.DateField(widget=forms.DateInput(format='%d%m%Y'),
    #                                 input_formats=['%d/%m/%Y'])

    class Meta:

        model = Profile
        fields = [
            'title', 'gender', 'full_name', 'surname', 'date_of_birth',
            'marital_status', 'nationality', 'id_number', 'passport_number',
            'passport_expiry_date', 'permit_type', 'permit_number',
            'permit_expiry_date', 'has_medical_condition', 'has_medical_needs',
            'medical_condition_description'
        ]
        widgets = {
            'has_medical_condition':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False
            }),
            'has_medical_needs':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }),
        self.fields['gender'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First names save_changes',
            'readonly': True,
        }), self.fields['surname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last name save_changes',
            'readonly': True,
        }),
        self.fields['date_of_birth'].widget.attrs.update({
            'class':
            'form-control js-datepicker save_changes',
            'placeholder':
            'YYYY-MM-DD',
        }),
        self.fields['marital_status'].widget.attrs.update({
            'class':
            'form-control',
        }),
        self.fields['nationality'].widget.attrs.update({
            'class':
            'form-control country-select-flag save_changes',
        }),
        self.fields['id_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeholder':
            'Namibian ID number',
        }), self.fields['passport_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['passport_expiry_date'].widget.attrs.update({
            'class':
            'form-control save_changes js-datepicker',
            'placeholder':
            'YYYY-MM-DD',
        }), self.fields['permit_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }),
        self.fields['permit_type'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }),
        self.fields['permit_expiry_date'].widget.attrs.update({
            'class':
            'form-control js-datepicker save_changes',
            'placeholder':
            'YYYY-MM-DD',
        }),
        self.fields['has_medical_condition'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }),
        self.fields['has_medical_needs'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['medical_condition_description'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4,
            'required':
            False,
        }),


class ContactApplicationsForm(ModelForm):

    class Meta:

        model = Contact
        fields = [
            'cellphone_number_1',
            'cellphone_number_2',
            'namibia_postal_address',
            'namibia_residential_address',
            'origin_postal_address',
            'origin_residential_address',
            'telephone',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['cellphone_number_1'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }),
        self.fields['cellphone_number_2'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }), self.fields['namibia_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['namibia_residential_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4
        }), self.fields['origin_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['origin_residential_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4
        }), self.fields['telephone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }), self.fields['email'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'example@mail.com'
        }),


class KinApplicationsForm(ModelForm):

    class Meta:

        model = Kin
        fields = [
            'first_name',
            'last_name',
            'kin_id_number',
            'relationship_type',
            'kin_email',
            'kin_cellphone_number',
            'kin_telephone',
            'kin_residential_address',
            'kin_postal_address',
            'kin_title',
            'kin_occupation',
            'Work_telephone',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['kin_title'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['first_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'name'
        }), self.fields['last_name'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'surname'
        }), self.fields['kin_id_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'id number/ passport'
        }), self.fields['relationship_type'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }), self.fields['kin_email'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'example@mail.com'
        }), self.fields['kin_cellphone_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }), self.fields['kin_telephone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }), self.fields['kin_residential_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4
        }), self.fields['kin_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
        }),
        self.fields['kin_occupation'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'Accountant'
        }), self.fields['Work_telephone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }),


class School_leavingApplicationsForm(ModelForm):

    class Meta:

        model = School_leaving
        fields = [
            'school_name',
            'highest_grade',
            'exam_year',
            'exam_authority',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['school_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name'
        }),
        self.fields['highest_grade'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'Grade 12',
        }),
        self.fields['exam_year'].widget.attrs.update({
            'class': 'form-control datepicker save_changes',
            'placeHolder': 'YYYY'
        }),
        self.fields['exam_authority'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name'
        }),


class SponsorApplicationsForm(ModelForm):

    class Meta:

        model = Sponsor
        fields = [
            'sponsor_name',
            'sponsor_signatory_name',
            'sponsor_postal_address',
            'sponsor_cellphone',
            'sponsor_telephone',
            'sponsor_email',
            'tuition_fee',
            'sponsorship_type',
            'registration_fee',
            'student_fund',
            'total_fee',
        ]
        widgets = {
            'sponsorship_type':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['sponsor_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name'
        }),
        self.fields['sponsor_signatory_name'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'Signatory Name'
        }), self.fields['sponsor_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'address'
        }), self.fields['sponsor_cellphone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }),
        self.fields['sponsor_telephone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000'
        }),
        self.fields['sponsor_email'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'example@mail.com'
        }),
        self.fields['tuition_fee'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00'
        }),
        self.fields['registration_fee'].widget.attrs.update({
            'class':
            'field-decoration form-control currency save_changes',
            'placeHolder':
            '0.00'
        }),
        self.fields['student_fund'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00'
        }),
        self.fields['total_fee'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00',
        }),


class TermAndConditionForm(ModelForm):

    class Meta:

        model = TermsAndConditions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['general_rule'].widget.attrs.update({
            'class': 'form-control',
            'placeHolder': 'terms and condition save_changes',
            'rows': 2
        }),
        self.fields['title'].widget.attrs.update({
            'class':
            'form-control',
            'placeHolder':
            'terms and condition save_changes'
        }),


class AcknowledgementForm(ModelForm):

    class Meta:

        model = TermsAndConditions
        fields = ['application_form_acknowledgement']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['application_form_acknowledgement'].widget.attrs.update({
            'class':
            'form-check-input save_changes',
        }),


class DocumentForm(ModelForm):

    class Meta:

        model = Document
        fields = [
            'medical_documents', 'certified_id_copy', 'passport_photo',
            'evidence_of_payment', 'foreign_qualification',
            'foreign_qualification_translation',
            'namibia_highest_qualification_copy', 'other_documents'
        ]
        widgets = {
            'certified_id_copy':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'medical_documents':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'passport_photo':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'evidence_of_payment':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'foreign_qualification':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'foreign_qualification_translation':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'namibia_highest_qualification_copy':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'other_documents':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
        }


#UNDERGRADUATE COURSE
class UndergraduateApplicationsHomeForm(ModelForm):

    class Meta:
        model = Application
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'type': 'Radio',
            'required': False,
        }),


class UndergraduateApplicationsMainForm(ModelForm):

    class Meta:
        model = Application
        fields = [
            'programme',
            'prefered_period',
            'course_first_choice',
            # 'course_second_choice',
            'other_level',
            'prefered_campus',
            'current_step',
            'based_on_level',
        ]
        widgets = {
            'prefered_period':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False,
            }, )
        }

    def __init__(self, *args, **kwargs):

        super(ModelForm, self).__init__(*args, **kwargs)

        # self.fields['course_first_choice'].queryset = Course.objects.none()
        # self.fields[
        #     'course_second_choice'].queryset = Secondary_course.objects.none()

        if 'programme' in self.data:
            try:
                programme_id = int(self.data.get('programme'))
                self.fields[
                    'course_first_choice'].queryset = Course.objects.filter(
                        level=programme_id).order_by('name')
                # self.fields[
                #     'course_second_choice'].queryset = Course.objects.filter(
                #         level=programme_id).order_by('name')

            except (ValueError, TypeError):
                self.fields[
                    'course_first_choice'].queryset = Course.objects.all()

                # self.fields[
                # 'course_second_choice'].queryset = Course.objects.all()
                # invalid input from the client; ignore and fallback to empty City queryset
        else:
            self.fields['course_first_choice'].queryset = Course.objects.all()
            # self.fields['course_second_choice'].queryset = Course.objects.all()

        self.fields['programme'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }),
        self.fields['course_first_choice'].widget.attrs.update({
            'class':
            'form-control save_changes',
            "data-live-search":
            True,
            'required':
            False,
        }),
        # self.fields['course_second_choice'].widget.attrs.update({
        #     'class':
        #     'form-control save_changes',
        #     "data-live-search":
        #     True,
        # }),
        self.fields['other_level'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'required':
            False,
            "placeholder":
            "Bachelor in ..., level ...",
        }),
        self.fields['prefered_campus'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False
        }),
        self.fields['current_step'].widget.attrs.update({
            'class': 'form-control d-none',
            'required': False
        }),
        self.fields['based_on_level'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False
        }),


class UndergraduateProfileApplicationsForm(ModelForm):

    class Meta:

        model = Profile
        fields = [
            'title', 'gender', 'full_name', 'surname', 'date_of_birth',
            'marital_status', 'nationality', 'namibian_region', 'id_number',
            'passport_number', 'passport_expiry_date', 'permit_type',
            'permit_number', 'permit_expiry_date', 'has_medical_condition',
            'has_medical_needs', 'medical_condition_description'
        ]
        widgets = {
            'has_medical_condition':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False
            }),
            'has_medical_needs':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }),
        self.fields['gender'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }), self.fields['full_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeholder': 'First names',
            'readonly': True,
            'required': False,
        }), self.fields['surname'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeholder': 'Last name',
            'readonly': True,
            'required': False,
        }),
        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'form-control js-datepicker save_changes',
            'placeholder': 'YYYY-MM-DD',
            'required': False,
        }),
        self.fields['marital_status'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }),
        self.fields['nationality'].widget.attrs.update({
            'class': 'form-control country-select-flag save_changes',
            'required': False,
        }),
        self.fields['namibian_region'].widget.attrs.update({
            'class': 'form-control country-select-flag save_changes',
            'required': False,
        }),
        self.fields['id_number'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeholder': 'Namibian ID number',
            'required': False,
        }), self.fields['passport_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'required':
            False,
        }),
        self.fields['passport_expiry_date'].widget.attrs.update({
            'class':
            'form-control js-datepicker save_changes',
            'placeholder':
            'YYYY-MM-DD',
            'required':
            False,
        }), self.fields['permit_number'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }),
        self.fields['permit_type'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }),
        self.fields['permit_expiry_date'].widget.attrs.update({
            'class':
            'form-control js-datepicker save_changes',
            'placeholder':
            'YYYY-MM-DD',
            'required':
            False,
        }),
        self.fields['medical_condition_description'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4,
            'required':
            False,
        }),


class UndergraduateContactApplicationsForm(ModelForm):

    class Meta:

        model = Contact
        fields = [
            'cellphone_number_1',
            'cellphone_number_2',
            'namibia_postal_address',
            'namibia_residential_address',
            'origin_postal_address',
            'origin_residential_address',
            'telephone',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['cellphone_number_1'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000',
            'required':
            False,
        }),
        self.fields['cellphone_number_2'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000',
            'required':
            False,
        }), self.fields['namibia_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'required':
            False,
        }), self.fields['namibia_residential_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4,
            'required':
            False,
        }), self.fields['origin_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'required':
            False,
        }), self.fields['origin_residential_address'].widget.attrs.update({
            'class':
            'form-control',
            'rows':
            4,
            'required':
            False,
        }), self.fields['telephone'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': '000-000-0000',
            'required': False,
        }), self.fields['email'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'example@mail.com',
            'required': False,
        }),


class UndergraduateKinApplicationsForm(ModelForm):

    class Meta:

        model = Kin
        fields = [
            'first_name',
            'last_name',
            'kin_id_number',
            'relationship_type',
            'kin_email',
            'kin_cellphone_number',
            'kin_telephone',
            'kin_residential_address',
            'kin_postal_address',
            'kin_title',
            'kin_occupation',
            'Work_telephone',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['kin_title'].widget.attrs.update({
            'class': 'form-control save_changes',
            'required': False,
        }), self.fields['first_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'name',
            'required': False,
        }), self.fields['last_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'surname',
            'required': False,
        }), self.fields['kin_id_number'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'id number/ passport',
            'required': False,
        }), self.fields['relationship_type'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'required':
            False,
        }), self.fields['kin_email'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'example@mail.com',
            'required': False,
        }), self.fields['kin_cellphone_number'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000',
            'required':
            False,
        }), self.fields['kin_telephone'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': '000-000-0000',
            'required': False,
        }), self.fields['kin_residential_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'rows':
            4,
            'required':
            False,
        }), self.fields['kin_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'required':
            False,
        }),
        self.fields['kin_occupation'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Accountant',
            'required': False,
        }), self.fields['Work_telephone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000',
            'required':
            False,
        }),


class UndergraduateEmployerApplicationsForm(ModelForm):

    class Meta:

        model = Employer
        fields = [
            'employer_name',
            'occupation',
            'employer_telephone',
            'employer_email',
            'start_date',
            'end_date',
            'duties',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['employer_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Employer Name',
            'required': False,
        }),
        self.fields['occupation'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'occupation',
            'required': False,
        }),
        self.fields['employer_telephone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-000',
            'required':
            False,
        }),
        self.fields['employer_email'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'employer@employer.com',
            'required': False,
        }),
        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control js-datepicker save_changes',
            'placeHolder': 'YYYY-MM-DD',
            'required': False,
        }),
        self.fields['end_date'].widget.attrs.update({
            'class': 'form-control js-datepicker save_changes',
            'placeHolder': 'YYYY-MM-DD',
            'required': False,
        }),
        self.fields['duties'].widget.attrs.update({
            'class': 'form-control save_changes',
            'rows': 4,
            'required': False,
        }),


class UndergraduateSchool_leavingApplicationsForm(ModelForm):

    class Meta:

        model = School_leaving
        fields = [
            'school_name',
            'highest_grade',
            'exam_year',
            'exam_authority',
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['school_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name',
            'required': False,
        }),
        self.fields['highest_grade'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Grade 12',
            'required': False,
        }),
        self.fields['exam_year'].widget.attrs.update({
            'class': 'form-control datepicker save_changes',
            'placeHolder': 'YYYY',
            'required': False,
        }),
        self.fields['exam_authority'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name',
            'required': False,
        }),


class UndergraduatePost_acadmic_qualificationApplicationsForm(ModelForm):

    class Meta:

        model = Post_acadmic_qualification
        fields = [
            'has_past_qualification', 'institution_name', 'location',
            'post_qualification', 'year_start', 'year_end'
        ]
        widgets = {
            'has_past_qualification':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['institution_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name',
            'required': False,
        }),
        self.fields['location'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'location',
            'required': False,
        }),
        self.fields['post_qualification'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'course/level',
            'required':
            False,
        }),
        self.fields['year_start'].widget.attrs.update({
            'class': 'form-control datepicker save_changes',
            'placeHolder': 'Start',
            'required': False,
        }),
        self.fields['year_end'].widget.attrs.update({
            'class': 'form-control datepicker save_changes',
            'placeHolder': 'End',
            'required': False,
        }),


class UndergraduateOutstanding_resultApplicationsForm(ModelForm):

    class Meta:

        model = Outstanding_result
        fields = [
            'has_out_standing_exam', 'out_standing_exam',
            'out_standing_exam_date'
        ]
        widgets = {
            'has_out_standing_exam':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['out_standing_exam'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name',
            'required': False,
        }),
        self.fields['out_standing_exam_date'].widget.attrs.update({
            'class':
            'form-control js-datepicker save_changes',
            'placeHolder':
            'YYYY-MM-DD',
            'required':
            False,
        }),


class UndergraduateLanguageApplicationsForm(ModelForm):

    class Meta:

        model = Language
        fields = [
            'school_language',
            'home_language',
            'has_english_course',
            'english_course',
            'applying_english_course',
        ]
        widgets = {
            'has_english_course':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False,
            }),
            'applying_english_course':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['school_language'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'Name'
        }),
        self.fields['home_language'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'YYYY-MM-DD',
        }),
        self.fields['english_course'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'Course',
        }),


class UndergraduateSponsorApplicationsForm(ModelForm):

    class Meta:

        model = Sponsor
        fields = [
            'sponsor_name',
            'sponsor_signatory_name',
            'sponsor_postal_address',
            'sponsor_cellphone',
            'sponsor_telephone',
            'sponsor_email',
            'tuition_fee',
            'sponsorship_type',
            'registration_fee',
            'student_fund',
            'total_fee',
        ]
        widgets = {
            'sponsorship_type':
            forms.RadioSelect(attrs={
                'class': 'form-check-input save_changes',
                'required': False
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['sponsor_name'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'Name',
            'required': False,
        }),
        self.fields['sponsor_signatory_name'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'Signatory Name',
            'required':
            False,
        }), self.fields['sponsor_postal_address'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            'address',
            'required':
            False,
        }), self.fields['sponsor_cellphone'].widget.attrs.update({
            'class':
            'form-control save_changes',
            'placeHolder':
            '000-000-0000',
            'required':
            False,
        }),
        self.fields['sponsor_telephone'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': '000-000-0000',
            'required': False,
        }),
        self.fields['sponsor_email'].widget.attrs.update({
            'class': 'form-control save_changes',
            'placeHolder': 'example@mail.com',
            'required': False,
        }),
        self.fields['tuition_fee'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00',
            'required': False,
        }),
        self.fields['registration_fee'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00',
            'required': False,
        }),
        self.fields['student_fund'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00',
            'required': False,
        }),
        self.fields['total_fee'].widget.attrs.update({
            'class': 'field-decoration form-control currency save_changes',
            'placeHolder': '0.00',
            'required': False,
        }),


class UndergraduateTermAndConditionForm(ModelForm):

    class Meta:

        model = TermsAndConditions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['general_rule'].widget.attrs.update({
            'class': 'form-control',
            'placeHolder': 'terms and condition',
            'rows': 2,
            'required': False,
        }),
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeHolder': 'terms and condition',
            'required': False,
        }),


class UndergraduateAcknowledgementForm(ModelForm):

    class Meta:

        model = TermsAndConditions
        fields = ['application_form_acknowledgement']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['application_form_acknowledgement'].widget.attrs.update({
            'class':
            'form-check-input save_changes',
            'required':
            False,
        }),


class UndergraduateDocumentForm(ModelForm):

    class Meta:

        model = Document
        fields = [
            'medical_documents', 'certified_id_copy', 'passport_photo',
            'evidence_of_payment', 'foreign_qualification',
            'foreign_qualification_translation',
            'namibia_highest_qualification_copy', 'other_documents'
        ]
        widgets = {
            'certified_id_copy':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'medical_documents':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-buttons save_changes',
                'required': False,
            }, ),
            'passport_photo':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'evidence_of_payment':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'foreign_qualification':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'foreign_qualification_translation':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'namibia_highest_qualification_copy':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
            'other_documents':
            forms.FileInput(attrs={
                'class':
                'input-input file-input choose-file-button save_changes',
                'required': False,
            }, ),
        }
