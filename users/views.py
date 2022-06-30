from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("name:", request.user)
            return redirect('portal-dashboard')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        password = request.POST['password1']

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #login user
            user = authenticate(request,
                                username=user.username,
                                password=password)

            if user is not None:
                login(request, user)
                return redirect('portal-dashboard')

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def terms_conditions(request):
    return render(request, 'users/termsConditions.html')
