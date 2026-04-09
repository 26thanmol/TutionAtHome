from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile, Booking


# 🌐 Pages
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


# 📝 REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(username=username, password=password)

        profile = Profile.objects.get(user=user)
        profile.role = role
        profile.save()

        return redirect('/login/')

    return render(request, 'register.html')


# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            profile = Profile.objects.get(user=user)

            if profile.role == "Student":
                return redirect('/student/')
            elif profile.role == "Teacher":
                return redirect('/teacher/')
            elif profile.role == "Parent":
                return redirect('/parent/')

    return render(request, 'login.html')


# 📅 BOOK TUTOR (NEW 🔥)
def book_tutor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        student_class = request.POST.get('class')
        subject = request.POST.get('subject')
        area = request.POST.get('city')

        Booking.objects.create(
            user=request.user,   # 🔥 LINK TO LOGGED USER
            name=name,
            student_class=student_class,
            subject=subject,
            area=area
        )

        return redirect('/student/')  # redirect to dashboard

    return render(request, 'book.html')


# 🎓 DASHBOARDS
def student_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'student_dashboard.html', {
        'bookings': bookings
    })


def teacher_dashboard(request):
    bookings = Booking.objects.filter(assigned_teacher=request.user)

    return render(request, 'teacher_dashboard.html', {
        'bookings': bookings
    })


def parent_dashboard(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'parent_dashboard.html', {'bookings': bookings})