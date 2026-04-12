from django.contrib import admin
from django.urls import path
from accounts import views as acc
from appointments import views as app

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', acc.user_login, name='login'),
    path('register/', acc.register, name='register'),
    path('logout/', acc.user_logout, name='logout'),

    path('home/', app.book_appointment, name='home'),
    path('my/', app.my_appointments, name='my_appointments'),
]