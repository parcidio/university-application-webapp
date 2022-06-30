from email.mime import application
from multiprocessing import context
from unicodedata import category, name
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from .forms import *
from users.forms import UserUpdateForm, ProfileUpdateForm
#REST-FRAMEWORK
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.files.storage import FileSystemStorage
from pdf2image import convert_from_path


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    users = User.objects.all()
    total_users = users.count()
    total_staff = User.objects.filter(is_staff=True).count()
    other_users = User.objects.filter(is_staff=False).count()
    faculties = Faculty.objects.all()
    applications = Application.objects.all()
    context = {
        'user': request.user,
        'total_users': total_users,
        'total_staff': total_staff,
        'other_users': other_users,
        'faculties': faculties,
        'applications': applications,
    }
    return render(request, 'portal/portal.html', context)


# SHORT COURSE APPLICATION
@login_required(login_url='login')
def applicationFormShortcourse(request):

    # Get the existing appliation objects
    existingApplication = Application.objects.get(
        owner=request.user,
        category__icontains='Short',
        status__icontains='In progress')
    existingProfile = Profile.objects.get(application=existingApplication)
    existingContact = Contact.objects.get(application=existingApplication)
    existingKin = Kin.objects.get(application=existingApplication)
    existingSchool_leaving = School_leaving.objects.get(
        application=existingApplication)
    existingSponsor = Sponsor.objects.get(application=existingApplication)
    existingTermsAndConditions = TermsAndConditions.objects.get(
        application=existingApplication)
    existingDocument = Document.objects.get(application=existingApplication)

    print("existingDocument")
    print(existingDocument.certified_id_copy)

    applicationForm = ApplicationsMainForm(instance=existingApplication)
    profileForm = ProfileApplicationsForm(instance=existingProfile)
    contactForm = ContactApplicationsForm(instance=existingContact)
    kinForm = KinApplicationsForm(instance=existingKin)
    School_leavingForm = School_leavingApplicationsForm(
        instance=existingSchool_leaving)
    Sponsor_form = SponsorApplicationsForm(instance=existingSponsor)
    acknowledgement_form = AcknowledgementForm(
        instance=existingTermsAndConditions)
    document_form = DocumentForm(instance=existingDocument)

    # return JsonResponse({'context': todos})

    # request should be ajax and method should be POST.
    if request.method == 'POST':
        # override existing forms
        # get the form data and point it to the existing application object
        applicationForm = ApplicationsMainForm(request.POST,
                                               instance=existingApplication)
        profileForm = ProfileApplicationsForm(request.POST,
                                              instance=existingProfile)
        contactForm = ContactApplicationsForm(request.POST,
                                              instance=existingContact)
        kinForm = KinApplicationsForm(request.POST, instance=existingKin)
        School_leavingForm = School_leavingApplicationsForm(
            request.POST, instance=existingSchool_leaving)
        Sponsor_form = SponsorApplicationsForm(request.POST,
                                               instance=existingSponsor)
        acknowledgement_form = AcknowledgementForm(
            request.POST, instance=existingTermsAndConditions)
        document_form = DocumentForm(request.POST,
                                     request.FILES,
                                     instance=existingDocument)

        # save the data
        if applicationForm.is_valid:
            print(request.POST)
            applicationForm = applicationForm.save(commit=False)

            applicationForm.owner = request.user
            # applicationForm.current_step = 1
            applicationForm.category = 'Shortcourse'

            if "application_form_acknowledgement" in request.POST:
                applicationForm.status = 'Pending'

            # UPDATE THE EXISTING APPLICATION OBJECT THAT WAS CREATE AT APPLICATION HOME VIEW
            applicationForm.save()
        if profileForm.is_valid:
            profileForm.save()
        if contactForm.is_valid or kinForm.is_valid:
            contactForm.save()
            kinForm.save()

        if School_leavingForm.is_valid or Sponsor_form.is_valid:
            School_leavingForm.save()
            Sponsor_form.save()

        if document_form.is_valid:
            print(
                "+++++++++++++++++++++++   FILES  +++++++++++++++++++++++++++\n"
            )
            print(request.FILES)
            document_form.save()

    context = {
        'user': request.user,
        'applicationForm': applicationForm,
        'profileForm': profileForm,
        'contactForm': contactForm,
        'kinForm': kinForm,
        'School_leavingForm': School_leavingForm,
        'Sponsor_form': Sponsor_form,
        'acknowledgement_form': acknowledgement_form,
        'document_form': document_form,
        'existingDocument': existingDocument,
    }
    print(context)
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == "GET" and is_ajax:
        course = request.GET.get('course', None)
        print(request.GET)
        available_course = list(
            Course.objects.filter(id=course).values('mode_of_study'))
        context['available_course'] = available_course
        print(available_course)
        return render(request, 'portal/form-registration-shortcourse.html',
                      context)

    return render(request, 'portal/form-registration-shortcourse.html',
                  context)


# UNDERGRADUATE COURSE APPLICATION
@login_required(login_url='login')
def applicationFormUndergraduate(request):
    # Get the existing appliation objects
    existingApplication = Application.objects.get(
        owner=request.user,
        category__icontains='Undergraduate',
        status__icontains='In progress')

    existingProfile = Profile.objects.get(application=existingApplication)
    existingContact = Contact.objects.get(application=existingApplication)
    existingKin = Kin.objects.get(application=existingApplication)
    existingEmployer = Employer.objects.get(application=existingApplication)
    existingSchool_leaving = School_leaving.objects.get(
        application=existingApplication)
    existingPost_acadmic_qualification = Post_acadmic_qualification.objects.get(
        application=existingApplication)
    existingOutstanding_result = Outstanding_result.objects.get(
        application=existingApplication)
    existingLanguage = Language.objects.get(application=existingApplication)
    existingSponsor = Sponsor.objects.get(application=existingApplication)
    existingTermsAndConditions = TermsAndConditions.objects.get(
        application=existingApplication)
    existingDocument = Document.objects.get(application=existingApplication)

    print("existingDocument")
    print(existingDocument.certified_id_copy)

    applicationForm = UndergraduateApplicationsMainForm(
        instance=existingApplication)
    profileForm = UndergraduateProfileApplicationsForm(
        instance=existingProfile)
    contactForm = UndergraduateContactApplicationsForm(
        instance=existingContact)
    kinForm = UndergraduateKinApplicationsForm(instance=existingKin)
    employerForm = UndergraduateEmployerApplicationsForm(
        instance=existingEmployer)
    school_leavingForm = UndergraduateSchool_leavingApplicationsForm(
        instance=existingSchool_leaving)
    post_acadmic_qualificationForm = UndergraduatePost_acadmic_qualificationApplicationsForm(
        instance=existingPost_acadmic_qualification)
    outstanding_resultForm = UndergraduateOutstanding_resultApplicationsForm(
        instance=existingOutstanding_result)
    languageForm = UndergraduateLanguageApplicationsForm(
        instance=existingLanguage)
    sponsor_form = UndergraduateSponsorApplicationsForm(
        instance=existingSponsor)
    acknowledgement_form = UndergraduateAcknowledgementForm(
        instance=existingTermsAndConditions)
    document_form = UndergraduateDocumentForm(instance=existingDocument)

    # request should be ajax and method should be POST.
    if request.method == 'POST':
        # override existing forms
        # get the form data and point it to the existing application object
        applicationForm = UndergraduateApplicationsMainForm(
            request.POST, instance=existingApplication)
        profileForm = UndergraduateProfileApplicationsForm(
            request.POST, instance=existingProfile)
        contactForm = UndergraduateContactApplicationsForm(
            request.POST, instance=existingContact)
        kinForm = UndergraduateKinApplicationsForm(request.POST,
                                                   instance=existingKin)
        employerForm = UndergraduateEmployerApplicationsForm(
            request.POST, instance=existingEmployer)
        school_leavingForm = UndergraduateSchool_leavingApplicationsForm(
            request.POST, instance=existingSchool_leaving)
        post_acadmic_qualificationForm = UndergraduatePost_acadmic_qualificationApplicationsForm(
            request.POST, instance=existingPost_acadmic_qualification)
        outstanding_resultForm = UndergraduateOutstanding_resultApplicationsForm(
            request.POST, instance=existingOutstanding_result)
        languageForm = UndergraduateLanguageApplicationsForm(
            request.POST, instance=existingLanguage)
        sponsor_form = UndergraduateSponsorApplicationsForm(
            request.POST, instance=existingSponsor)
        acknowledgement_form = UndergraduateAcknowledgementForm(
            request.POST, instance=existingTermsAndConditions)
        document_form = UndergraduateDocumentForm(request.POST,
                                                  request.FILES,
                                                  instance=existingDocument)

        # save the data
        if applicationForm.is_valid:
            print(request.POST)
            applicationForm = applicationForm.save(commit=False)
            applicationForm.owner = request.user
            applicationForm.category = 'Undergraduate'

            if "application_form_acknowledgement" in request.POST:
                applicationForm.status = 'Pending'
                applicationForm.current_step = 0

            # UPDATE THE EXISTING APPLICATION OBJECT THAT WAS CREATE AT APPLICATION HOME VIEW
            applicationForm.save()

        if profileForm.is_valid:
            profileForm.save()
        if contactForm.is_valid:
            contactForm.save()
        if kinForm.is_valid:
            kinForm.save()
        if employerForm.is_valid():
            employerForm.save()

        if school_leavingForm.is_valid:
            school_leavingForm.save()

        if post_acadmic_qualificationForm.is_valid:
            post_acadmic_qualificationForm.save()

        if outstanding_resultForm.is_valid:
            outstanding_resultForm.save()

        if languageForm.is_valid:
            languageForm.save()

        if sponsor_form.is_valid:
            sponsor_form.save()

        if document_form.is_valid:
            print(
                "+++++++++++++++++++++++   FILES  +++++++++++++++++++++++++++\n"
            )
            print(request.FILES)
            document_form.save()

    context = {
        'user': request.user,
        'applicationForm': applicationForm,
        'profileForm': profileForm,
        'contactForm': contactForm,
        'kinForm': kinForm,
        'employerForm': employerForm,
        'School_leavingForm': school_leavingForm,
        'Post_acadmic_qualificationForm': post_acadmic_qualificationForm,
        'Outstanding_resultForm': outstanding_resultForm,
        'LanguageForm': languageForm,
        'Sponsor_form': sponsor_form,
        'acknowledgement_form': acknowledgement_form,
        'document_form': document_form,
        'existingDocument': existingDocument,
    }

    return render(request, 'portal/form-registration-undergraduate.html',
                  context)


def load_courses(request):
    programme_id = request.GET.get("programme_id")
    course_id = request.GET.get("course_id")

    if programme_id:
        try:
            courses = Course.objects.filter(level=programme_id)
        except:
            courses = Course.objects.all()
        print(list(courses.values('id', 'name')))
        return JsonResponse(list(courses.values('id', 'name')), safe=False)

    if course_id:
        try:
            course = Course.objects.filter(id=course_id)
        except:
            pass
        print(list(course.values('id', 'mode_of_study', 'level')))
        return JsonResponse(list(course.values('id', 'mode_of_study',
                                               'level')),
                            safe=False)


@login_required(login_url='login')
def applicationFormUndergraduateUpdate(request, pk):
    applicationObject = Application.objects.get(id=pk)
    applicationForm = ApplicationsMainForm(instance=applicationObject)

    if request.method == 'POST':
        applicationForm = ApplicationsMainForm(request.POST,
                                               instance=applicationObject)

        if applicationForm.is_valid:
            print("is_valid")
            applicationForm.save()
            return redirect('portal-application-home')

    context = {
        'user': request.user,
        'applicationForm': applicationForm,
    }
    return render(request, 'portal/form-registration-undergraduate.html',
                  context)


@login_required(login_url='login')
def applicationFormPostgraduate(request):
    return render(request, 'portal/form-registration-postgraduate.html',
                  {'user': request.user})


# @login_required(login_url='login')
# def applicationHomeUpdate(request, pk):
#     applicationForm = Application.objects.get(id=pk)
#     form = ApplicationsHomeForm(instance=applicationForm)
#     if request.method == 'POST':

#         if "apply" in request.POST:
#             if form.is_valid:

#     context = {
#         'form': form,
#         'user': request.user,
#     }
#     return render(request, 'portal/applicationForm-home.html', context)


@login_required(login_url='login')
def applicationHome(request):
    form = ApplicationsHomeForm()
    #if existing applications => show existing applications

    existingShortcourseApplications = Application.objects.filter(
        owner=request.user).filter(category__icontains='Short').filter(
            status__icontains='In progress')
    existingUndergraduateApplications = Application.objects.filter(
        owner=request.user).filter(category__icontains='Under').filter(
            status__icontains='In progress').order_by('creation_date')
    existingPostgraduateApplications = Application.objects.filter(
        owner=request.user).filter(category__icontains='Post').filter(
            status__icontains='In progress').order_by('creation_date')

    if request.method == 'POST':

        if "apply" in request.POST:
            form = ApplicationsHomeForm(request.POST)

            if form.is_valid:
                print(request.POST)
                # #if no existing applications => create a new application
                form = form.save(commit=False)
                form.owner = request.user
                # form.current_step = 1
                form.status = 'In Progress'

                if request.POST['category'] == "Shortcourse":
                    existingShortcourseApplications.delete()
                    form.save()
                    return redirect('portal-registration-form-shortcourse')

                elif request.POST['category'] == "Undergraduate":
                    existingUndergraduateApplications.delete()
                    form.save()
                    return redirect('portal-registration-form-undergraduate')

                elif request.POST['category'] == "Postgraduate":
                    existingPostgraduateApplications.delete()
                    form.save()
                    return redirect('portal-registration-form-Postgraduate')

        if "delete_saved" in request.POST:
            saved_form_id = request.POST["saved_form_id"]
            saved_form = Application.objects.get(pk=saved_form_id)
            print(saved_form.id)
            saved_form.delete()

    context = {
        'form': form,
        'user': request.user,
        'existingShortcourseApplications': existingShortcourseApplications,
        'existingUndergraduateApplications': existingUndergraduateApplications,
        'existingPostgraduateApplications': existingPostgraduateApplications,
    }
    return render(request, 'portal/applicationForm-home.html', context)


@login_required(login_url='login')
def userProfile(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            print(request.FILES)
            user_form.save()
            profile_form.save()
            return redirect('portal-user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user': request.user,
        'form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'portal/profile.html', context)


@login_required(login_url='login')
def faculty(request):
    #adding new faculty
    form = FacultyForm()
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/faculty')
    #reading faculties
    faculties_list = Faculty.objects.all()

    context = {'form': form, 'faculties_list': faculties_list}
    return render(request, 'portal/faculty.html', context)


@login_required(login_url='login')
def course(request):
    #adding new course
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/course')
    #reading faculties
    course_list = Course.objects.all()

    context = {'form': form, 'course_list': course_list}
    return render(request, 'portal/course.html', context)


@login_required(login_url='login')
def course_update(request, course_id):
    course = Course.objects.get(pk=course_id)
    #adding new course
    form = CourseForm(request.POST or None, instance=course)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/course')
    context = {'form': form, 'course': course}
    return render(request, 'portal/course_update.html', context)


@login_required(login_url='login')
def course_delete(request, course_id):
    course = Course.objects.get(pk=course_id)
    #delete course
    course.delete()
    return redirect('/course')


@login_required(login_url='login')
def faculty_update(request, faculty_id):
    faculty = Faculty.objects.get(pk=faculty_id)
    #adding new faculty
    form = FacultyForm(request.POST or None, instance=faculty)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/faculty')
    context = {'form': form, 'faculty': faculty}
    return render(request, 'portal/faculty_update.html', context)


@login_required(login_url='login')
def faculty_delete(request, faculty_id):
    faculty = Faculty.objects.get(pk=faculty_id)
    #delete course
    faculty.delete()
    return redirect('/faculty')


@login_required(login_url='login')
def unavailable_page(request):
    return render(request, 'portal/404.html', {'user': request.user})


@login_required(login_url='login')
def users(request):
    #reading users
    users = User.objects.all()
    staff = User.objects.filter(is_staff=True)
    student = User.objects.filter(is_staff=False)
    disabled_users = User.objects.filter(is_active=False)

    context = {
        'user_list': users,
        'staff_list': staff,
        'student_list': student,
        'disabled_users_list': disabled_users,
    }
    return render(request, 'portal/users.html', context)


@login_required(login_url='login')
def campus(request):
    #adding new campus
    form = CampusForm()
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/campus')
    #reading campuses
    campuses = Campus.objects.all()
    context = {'form': form, 'campus_list': campuses}
    return render(request, 'portal/campus.html', context)


@login_required(login_url='login')
def campus_update(request, campus_id):
    campus = Campus.objects.get(pk=campus_id)
    #adding new faculty
    form = CampusForm(request.POST or None, instance=campus)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/campus')
    context = {'form': form, 'campus': campus}
    return render(request, 'portal/campus_update.html', context)


@login_required(login_url='login')
def campus_delete(request, campus_id):
    campus = Campus.objects.get(pk=campus_id)
    #delete course
    campus.delete()
    return redirect('/campus')


@login_required(login_url='login')
def subject(request):
    #adding new campus
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/subject')
    #reading subjects
    subject = Subject.objects.all().order_by('name')
    context = {'form': form, 'subject_list': subject}
    return render(request, 'portal/subject.html', context)


@login_required(login_url='login')
def campus_view(request, campus_id):
    campus = Campus.objects.get(pk=campus_id)
    #adding new faculty
    context = {'campus': campus}
    return render(request, 'portal/campus_view.html', context)


@login_required(login_url='login')
def subject_delete(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    #delete course
    subject.delete()
    return redirect('/subject')


@login_required(login_url='login')
def subject_update(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    #adding new faculty
    form = SubjectForm(request.POST or None, instance=subject)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/subject')
    context = {'form': form, 'subject': subject}
    return render(request, 'portal/subject_update.html', context)


@login_required(login_url='login')
def faq_create(request):
    return render(request, 'portal/faq.html', {'user': request.user})


@login_required(login_url='login')
def terms_conditions_create(request):
    form = TermAndConditionForm()
    if request.method == 'POST':
        form = TermAndConditionForm(request.POST)

        if form.is_valid:
            form.save()

    context = {'user': request.user, 'form': form}
    return render(request, 'portal/terms_and_conditions.html', context)


@login_required(login_url='login')
def application_form(request):
    users = User.objects.all()
    total_users = users.count()
    total_staff = User.objects.filter(is_staff=True).count()
    other_users = User.objects.filter(is_staff=False).count()
    faculties = Faculty.objects.all()
    applications = Application.objects.all()
    context = {
        'user': request.user,
        'total_users': total_users,
        'total_staff': total_staff,
        'other_users': other_users,
        'faculties': faculties,
        'applications': applications,
    }

    return render(request, 'portal/application-forms.html', context)


@login_required(login_url='login')
def application_form_view(request, application_id):

    application = Application.objects.get(pk=application_id)
    profile = Profile.objects.get(application=application_id)
    contact = Contact.objects.get(application=application_id)
    kin = Kin.objects.get(application=application_id)
    employer = Employer.objects.get(application=application_id)
    outstanding_result = Outstanding_result.objects.get(
        application=application_id)
    school_leaving = School_leaving.objects.get(application=application_id)
    language = Language.objects.get(application=application_id)
    sponsor = Sponsor.objects.get(application=application_id)
    document = Document.objects.get(application=application_id)

    context = {
        'user': request.user,
        'application': application,
        'profile': profile,
        'contact': contact,
        'kin': kin,
        'employer': employer,
        'outstanding_result': outstanding_result,
        'school_leaving': school_leaving,
        'language': language,
        'sponsor': sponsor,
        'document': document,
    }

    return render(request, 'portal/application-form-view.html', context)


@login_required(login_url='login')
def application_form_update(request, application_id):
    existingApplication = Application.objects.get(id=application_id)

    existingProfile = Profile.objects.get(application=existingApplication)
    existingContact = Contact.objects.get(application=existingApplication)
    existingKin = Kin.objects.get(application=existingApplication)
    existingEmployer = Employer.objects.get(application=existingApplication)
    existingSchool_leaving = School_leaving.objects.get(
        application=existingApplication)
    existingPost_acadmic_qualification = Post_acadmic_qualification.objects.get(
        application=existingApplication)
    existingOutstanding_result = Outstanding_result.objects.get(
        application=existingApplication)
    existingLanguage = Language.objects.get(application=existingApplication)
    existingSponsor = Sponsor.objects.get(application=existingApplication)
    existingTermsAndConditions = TermsAndConditions.objects.get(
        application=existingApplication)
    existingDocument = Document.objects.get(application=existingApplication)

    # Forms
    applicationForm = UndergraduateApplicationsMainForm(
        instance=existingApplication)
    profileForm = UndergraduateProfileApplicationsForm(
        instance=existingProfile)
    contactForm = UndergraduateContactApplicationsForm(
        instance=existingContact)
    kinForm = UndergraduateKinApplicationsForm(instance=existingKin)
    employerForm = UndergraduateEmployerApplicationsForm(
        instance=existingEmployer)
    school_leavingForm = UndergraduateSchool_leavingApplicationsForm(
        instance=existingSchool_leaving)
    post_acadmic_qualificationForm = UndergraduatePost_acadmic_qualificationApplicationsForm(
        instance=existingPost_acadmic_qualification)
    outstanding_resultForm = UndergraduateOutstanding_resultApplicationsForm(
        instance=existingOutstanding_result)
    languageForm = UndergraduateLanguageApplicationsForm(
        instance=existingLanguage)
    sponsor_form = UndergraduateSponsorApplicationsForm(
        instance=existingSponsor)
    acknowledgement_form = UndergraduateAcknowledgementForm(
        instance=existingTermsAndConditions)
    document_form = UndergraduateDocumentForm(instance=existingDocument)

    # request should be ajax and method should be POST.
    if request.method == 'POST':
        # override existing forms
        # get the form data and point it to the existing application object
        applicationForm = UndergraduateApplicationsMainForm(
            request.POST, instance=existingApplication)
        profileForm = UndergraduateProfileApplicationsForm(
            request.POST, instance=existingProfile)
        contactForm = UndergraduateContactApplicationsForm(
            request.POST, instance=existingContact)
        kinForm = UndergraduateKinApplicationsForm(request.POST,
                                                   instance=existingKin)
        employerForm = UndergraduateEmployerApplicationsForm(
            request.POST, instance=existingEmployer)
        school_leavingForm = UndergraduateSchool_leavingApplicationsForm(
            request.POST, instance=existingSchool_leaving)
        post_acadmic_qualificationForm = UndergraduatePost_acadmic_qualificationApplicationsForm(
            request.POST, instance=existingPost_acadmic_qualification)
        outstanding_resultForm = UndergraduateOutstanding_resultApplicationsForm(
            request.POST, instance=existingOutstanding_result)
        languageForm = UndergraduateLanguageApplicationsForm(
            request.POST, instance=existingLanguage)
        sponsor_form = UndergraduateSponsorApplicationsForm(
            request.POST, instance=existingSponsor)
        acknowledgement_form = UndergraduateAcknowledgementForm(
            request.POST, instance=existingTermsAndConditions)
        document_form = UndergraduateDocumentForm(request.POST,
                                                  request.FILES,
                                                  instance=existingDocument)

        # save the data
        if applicationForm.is_valid:
            print(request.POST)
            applicationForm = applicationForm.save(commit=False)
            applicationForm.owner = request.user
            applicationForm.category = 'Undergraduate'

            if "application_form_acknowledgement" in request.POST:
                applicationForm.status = 'Pending'
                applicationForm.current_step = 0

            # UPDATE THE EXISTING APPLICATION OBJECT THAT WAS CREATE AT APPLICATION HOME VIEW
            applicationForm.save()

        if profileForm.is_valid:
            profileForm.save()
        if contactForm.is_valid:
            contactForm.save()
        if kinForm.is_valid:
            kinForm.save()
        if employerForm.is_valid():
            employerForm.save()

        if school_leavingForm.is_valid:
            school_leavingForm.save()

        if post_acadmic_qualificationForm.is_valid:
            post_acadmic_qualificationForm.save()

        if outstanding_resultForm.is_valid:
            outstanding_resultForm.save()

        if languageForm.is_valid:
            languageForm.save()

        if sponsor_form.is_valid:
            sponsor_form.save()

        if document_form.is_valid:
            print(
                "+++++++++++++++++++++++   FILES  +++++++++++++++++++++++++++\n"
            )
            print(request.FILES)
            document_form.save()

    context = {
        'user': request.user,
        'applicationForm': applicationForm,
        'profileForm': profileForm,
        'contactForm': contactForm,
        'kinForm': kinForm,
        'employerForm': employerForm,
        'School_leavingForm': school_leavingForm,
        'Post_acadmic_qualificationForm': post_acadmic_qualificationForm,
        'Outstanding_resultForm': outstanding_resultForm,
        'LanguageForm': languageForm,
        'Sponsor_form': sponsor_form,
        'acknowledgement_form': acknowledgement_form,
        'document_form': document_form,
        'existingDocument': existingDocument,
    }

    return render(request, 'portal/form-registration-undergraduate.html',
                  context)


images = convert_from_path()


def pdf2img():
    try:
        images = convert_from_path(
            str('C:\Users\User\Desktop\university application webapp\media\Parcidio\application_documents\grade_12_certificate.pdf'
                ))
        for img in images:
            img.save('converted_pdf\output.jpg', 'JPEG')

    except:
        Result = "NO pdf found"
        print("Result", Result)

    else:
        Result = "success"
        print("Result", Result)
