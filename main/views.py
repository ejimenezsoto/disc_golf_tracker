from django.shortcuts import render, redirect
from .models import User, Course, Review
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'index.html', context)

def registration(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')

    password = request.POST['password']
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print('password:', password)
    print('hashed:', hashed)
    new_user = User.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        email=request.POST['email'],
        password=hashed
    )
    request.session['user_id'] = new_user.id
    return redirect('/dashboard')

def login(request):
    users_with_email = User.objects.filter(email=request.POST['email'])
    if len(users_with_email) > 0:
        first_user = users_with_email[0]
        if bcrypt.checkpw(request.POST['password'].encode(), first_user.password.encode()):
            request.session['user_id'] = first_user.id
            return redirect('/dashboard')
    messages.error(request, "Email invalid/password wrong!")
    print("No users found!")
    return redirect('/')

def dashboard(request):
    creator = User.objects.get(id=request.session['user_id'])
    created_course = Course.objects.filter(created_by_id=creator)

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'courses': Course.objects.all(),
        'user_created_courses': Course.objects.filter(created_by=creator)
    }
    
    return render(request,"dashboard.html", context)

def create_course(request):
    
    return render(request, 'create_course.html')

def process_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/create_course')
    Course.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
        number_of_holes=request.POST['number_of_holes'],
        par=request.POST['par'],
        created_by=User.objects.get(id=request.session['user_id'])
    )
    print(Course.objects.all())
    return redirect('/dashboard')

def one_course(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, "one_course.html", context)

def review_course(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'review_course.html', context)

def process_review(request):
    author = User.objects.get(id=request.session['user_id'])
    course_for = Course.objects.get(id=request.POST['course_id'])
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        author = author,
        course_for = course_for
    )
    return redirect('/dashboard')




def game_stats(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
        'n' : range(Course.objects.get(id=course_id).number_of_holes) 
    }
    return render(request, 'game_stats.html',context)

def delete_course(request, course_id):
    course_to_delete = Course.objects.get(id=course_id)
    course_to_delete.delete()
    return redirect('/dashboard')

def like_course(request, course_id):
    user = User.objects.get(id=request.session['user_id'])
    course = Course.objects.get(id=course_id)
    course.liked_by.add(user)

    return redirect('/dashboard')

def favorites(request):
    context = {
        'courses': Course.objects.filter(liked_by__id=request.session['user_id'])
    }
    return render(request, 'favorites.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')