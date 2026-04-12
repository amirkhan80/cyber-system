from django.shortcuts import render, redirect
from .models import Appointment
from services.models import Service
from django.contrib.auth.decorators import login_required

@login_required
def book_appointment(request):
    services = Service.objects.all()

    if request.method == "POST":
        Appointment.objects.create(
            user=request.user,
            service_id=request.POST['service'],
            date=request.POST['date'],
            time=request.POST['time'],
            description=request.POST.get('description')
        )
        return redirect('my_appointments')

    return render(request, 'book.html', {'services': services})


@login_required
def my_appointments(request):
    data = Appointment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'my_appointments.html', {'data': data})