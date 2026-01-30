from django.shortcuts import render, redirect
from .models import Student, attendance
from datetime import date
def student_list(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            roll_no=request.POST['roll']
              )
        return redirect('students')
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def mark_attendance(request):
    students = Student.objects.all()
    today = date.today()
    if request.method == "POST":
        for student in students:
            attendance.objects.update_or_create(
                student=student,date=today,
                defaults={
                    'present': request.POST.get(str(student.id)) == 'on'
                    })
        return redirect('attendance_list')
    return render(request, 'attendance/mark_attendance.html', {
            'students': students, 'today': today
            })
def attendance_list(request):
    records = attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance/attendance_list.html', {
        'records': records
        })
