from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Course, Teacher
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')


def register(request):
    courses = Course.objects.all()
    std_data = User.objects.all()
    context = {'courses':courses}
    return render(request,'register.html', context=context)






def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            if user.is_staff == 1:
                return redirect('admin')
            else:
                
                return redirect('teacherpage')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'login.html')



def admin(request):
    return render(request,'admin.html')


def addcourse(request):
    if request.method == 'POST':
        course_name = request.POST['cname']
        Course.objects.create(course_name=course_name)
        messages.info(request,'Course added succesfully')
    return redirect('admin')


def register_fn(request):

    if request.method == 'POST':

        f_name = request.POST['fname']
        l_name = request.POST['lname']
        mail = request.POST['email']
        mobile = request.POST['phone']
        u_name = request.POST['uname']
        pass1 = request.POST['pass']
        pass2 = request.POST['cpass']
        select = request.POST['select']
        c_name = Course.objects.get(id=select)

        if pass1 == pass2:

            if User.objects.filter(username=u_name).exists():
                return redirect('register')
            
            else:
                user = User.objects.create_user(first_name = f_name, last_name = l_name,email = mail, password = pass1, username = u_name)
                user.save()
                data = User.objects.get(id = user.id)
                teacherdata = Teacher(phone=mobile,user=data,course=c_name)
                teacherdata.save()
                print('data added successfully')
                return redirect('login')
        else:
            messages.error(request,'Passwords not matching')
            return redirect('register')
    
    else:
        print('error')
        return redirect('register')
                

def teacherpage(request):
    current_user = request.user
    user_id = current_user.id
    teacher_data = Teacher.objects.filter(id=user_id)
    context = {'tdata':teacher_data}
    return render(request,'teacher_page.html',context=context)


def f_update(request, pk):
    if request.method == 'POST':
        faculty_data = Teacher.objects.get(id=pk)
        faculty_data.user.first_name = request.POST['fname']
        faculty_data.user.last_name = request.POST['lname']
        faculty_data.user.email = request.POST['email']
        faculty_data.phone = request.POST['phone']
        faculty_data.user.username = request.POST['uname']
        
        
        image_file = request.FILES.get('image')
        if image_file:
            faculty_data.image = image_file

        select = request.POST['select']
        course = Course.objects.get(id=select)
        faculty_data.course = course
        faculty_data.save()
        faculty_data.user.save()

        if request.user.is_staff:
            return redirect('admin')
        else:
            return redirect('f_profile')

    value = Teacher.objects.get(id=pk)
    courses = Course.objects.all()
    context = {
        "value": value,
        "courses": courses
    }

    return render(request, 'f_update.html', context)




