from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
    path('services/', views.services),
    path('contact/', views.contact),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('student/', views.student_dashboard),
    path('teacher/', views.teacher_dashboard),
    path('parent/', views.parent_dashboard),
    path('book/', views.book_tutor, name='book_tutor'),
]