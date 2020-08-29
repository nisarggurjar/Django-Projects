from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from datetime import datetime, date
from .forms import *

def Home(request):
    data = Slider.objects.all().order_by("p")
    cat = Courses_Category.objects.all()
    event = Event_Category.objects.all()
    today_date = date.today()
    #Date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    print(event)
    return render(request, "Home/index.html",  {"banners":data, "cats":cat, "events":event, "today":today_date})

def Login(request):
    if request.user.is_authenticated():
        return redirect("admin_home")

    error = False
    if request.method == "POST":
        d = request.POST
        u = d['un']
        p = d['ps']
        user = authenticate(username = u, password = p)
        if user:
            login(request, user)
            return redirect("admin_home")
        error = True
    return render(request, "Home/login.html", {"error":error})

def Logout(request):
    logout(request)
    return redirect("login")

def Register(request):
    return render(request, "Home/register.html")


def ContactUs(request):
    return render(request, "Home/contact.html")


def Courses_Details(request, course):
    # data = Course.objects.get(url = course)    orignally yehh h
    data = Course.objects.all()
    return render(request, "Home/course_details.html", {"i":data})

def Event_List(request):
    events = Events.objects.all()
    today_date = date.today()
    first_event = []
    for i in events:
        for j in i.dates_set.all():
            if j.start_date > today_date:
                first_event.append(j)
                break
    print(first_event)
    return render(request, "Home/events_list.html", {"events":events, "today":today_date, "all":first_event})

def Events_Details(request, events):
    today_date = date.today()
    data = Events.objects.get(url = events)

    return render(request, "Home/event_details.html", {"i":data, "today":today_date})











######   Admin Panle Funcation ##########
def Admin_Home(request):
    return render(request, "Home/Master/index.html")

def All_Banners(request):
    data = Slider.objects.all().order_by('p')
    return render(request, "Home/Master/banners.html", {"banners":data})



def Add_New_Banner(request):
    if request.method == "POST":
        d = request.POST
        img = request.FILES["image"]
        l1 = d['l1']
        l2 = d['l2']
        l3 = d['l3']
        p = d['p']
        Slider.objects.create(img = img, l1 = l1, l2 = l2, l3 = l3, p = p)
        return redirect("banners")

    return render(request, "Home/Master/Add_New_Banner.html")


def Edit_New_Banner(request, b_id, type):
    data = Slider.objects.filter(id = int(b_id)).first()
    if type == "Delete":
        data.delete()
        return redirect("banners")

    if request.method == "POST":
        d = request.POST
        img = None
        try:
            img = request.FILES["image"]
        except:
            pass
        if img:
            data.img = img
        else:
            data.img = data.img
        data.l1 = d['l1']
        data.l2 = d['l2']
        data.l3 = d['l3']
        data.p = d['p']
        data.save()
        return redirect("banners")
    return render(request, "Home/Master/Add_New_Banner.html", {"type" : "Edit", "b":data})

def All_Courses_Categories(request, type, c_id):
    data = Courses_Category.objects.all()
    if type == "Edit":
        data1 = Courses_Category.objects.get(id=c_id)
        if request.method == "POST":
            name = request.POST["name"]
            data1.name = name
            data1.save()
            return redirect("courses_categories", "Main", '0')
        return render(request, "Home/Master/courses_categories.html", {"cats": data, 'cat':data1})

    if type == "Delete":
        data1 = Courses_Category.objects.get(id=c_id)
        data1.delete()
        return redirect("courses_categories", "Main", '0')

    today_date = date.today()
    Date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    if request.method == "POST":
        name = request.POST["name"]
        Courses_Category.objects.create(name = name, date = Date)
        return redirect("courses_categories", "Main", '0')

    return render(request, "Home/Master/courses_categories.html", {"cats":data})


def All_Courses(request, type, c_id):
    if type == "Add":
        form = AddNew_Course_Form()
        if request.method == "POST":
            form = AddNew_Course_Form(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("courses", "Main", 0)
        return render(request,"Home/Master/Add_New_Course.html", {"form":form})

    if type == "Edit":
        data = Course.objects.filter(id = c_id).first()
        form = AddNew_Course_Form(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("courses", "Main", 0)
        return render(request, "Home/Master/Add_New_Course.html", {"form": form})

    if type == "Delete":
        data = Course.objects.filter(id=c_id).first()
        data.delete()
        return redirect("courses", "Main", 0)


    data = Course.objects.all().order_by("-id")
    d = {
        "courses":data,
    }
    return render(request, "Home/Master/courses.html", d)



def All_Trainers(request, type, t_id):

    if type == "Delete":
        data = Trainer.objects.filter(id=t_id).first()
        data.delete()
        return redirect("trainers", "Main", 0)

    if type == "Edit":
        data = Trainer.objects.filter(id=t_id).first()
        form = Add_New_Trainer_Form(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("trainers", "Main", 0)
        return render(request, "Home/Master/add_new_trainer.html", {"form": form})

    if type == "Add":
        form = Add_New_Trainer_Form()
        if request.method == "POST":
            form = Add_New_Trainer_Form(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("trainers", "Main", 0)
        return render(request, "Home/Master/add_new_trainer.html", {"form":form})

    data = Trainer.objects.all()
    return render(request, "Home/Master/all_trainers.html", {"trainers":data})


def All_Content(request, type, c_id):
    if type == "Delete":
        data = Title.objects.get(id = c_id)
        data.delete()
        return redirect("courses", "Main", 0)

    if type == "Edit":
        data = Title.objects.get(id = c_id)
        form = AddCourse_Title_Form(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("courses", "Main", 0)
        return render(request, "Home/Master/add_new_content.html", {"form": form})



    if type == "Add":
        form = AddCourse_Title_Form()
        if request.method == "POST":
            form = AddCourse_Title_Form(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("courses", "Main", 0)
        return render(request, "Home/Master/add_new_content.html", {"form":form})

    cou = Course.objects.filter(id = c_id).first()
    data = Title.objects.filter(course = cou).order_by("p")
    return render(request, "Home/Master/all_content.html", {"titles":data, "c_id":c_id})





def All_Events_Categories(request, type, c_id):
    data = Event_Category.objects.all()
    if type == "Edit":
        data1 = Event_Category.objects.get(id=c_id)
        if request.method == "POST":
            name = request.POST["name"]
            data1.name = name
            data1.save()
            return redirect("events_categories", "Main", '0')
        return render(request, "Home/Master/event_categories.html", {"cats": data, 'cat':data1})

    if type == "Delete":
        data1 = Event_Category.objects.get(id=c_id)
        data1.delete()
        return redirect("events_categories", "Main", '0')

    today_date = date.today()
    Date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    if request.method == "POST":
        name = request.POST["name"]
        Event_Category.objects.create(name = name, date = Date)
        return redirect("events_categories", "Main", '0')

    return render(request, "Home/Master/event_categories.html", {"cats":data})



def All_Events(request, type, c_id):
    if type == "Add":
        form = AddNew_Event_Form()
        if request.method == "POST":
            form = AddNew_Event_Form(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                if data.un and data.ps:
                    ur = User.objects.create_user(data.un, "techsimplus@gmail.com", data.ps)
                    print(ur, "Hello")
                    data.user = ur
                data.save()
                return redirect("events", "Main", 0)
        return render(request,"Home/Master/Add_New_Event.html", {"form":form})

    if type == "Edit":
        data1 = Events.objects.filter(id = c_id).first()
        form = AddNew_Event_Form(request.POST or None, request.FILES or None, instance=data1)
        if form.is_valid():
            data = form.save(commit=False)
            if data.un and data.ps:
                usr1 = User.objects.filter(username = data.un).first()
                if not usr1:
                    ur = User.objects.create_user(data.un, "techsimplus@gmail.com", data.ps)
                    data.usr = ur
            if data1.usr:
                if not data.un and not data.ps:
                    usr1 = User.objects.get(id = data1.usr.id)
                    usr1.delete()
            data.save()
            return redirect("events", "Main", 0)
        return render(request, "Home/Master/Add_New_Event.html", {"form": form})

    if type == "Delete":
        data = Events.objects.filter(id=c_id).first()
        data.delete()
        return redirect("events", "Main", 0)


    data = Events.objects.all().order_by("-id")
    d = {
        "courses":data,
    }
    return render(request, "Home/Master/events.html", d)


def Add_New_Date(request):
    form = Add_New_Dates_Form()
    if request.method == "POST":
        form = Add_New_Dates_Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("events", "Main", 0)
    return render(request, "Home/Master/Add_New_Event_Date.html", {"form":form})