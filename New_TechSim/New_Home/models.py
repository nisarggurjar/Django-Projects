from django.db import models
from django.contrib.auth.models import User

class Slider(models.Model):
    img = models.FileField(null=True, blank=True)
    l1 = models.CharField(max_length=500, null=True, blank=True)
    l2 = models.CharField(max_length=500, null=True, blank=True)
    l3 = models.CharField(max_length=500, null=True, blank=True)
    p = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.p

class Trainer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    review = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    des = models.CharField(max_length=2000, null=True, blank=True)
    mail = models.CharField(max_length=200, null=True, blank=True)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

class Courses_Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    cat = models.ForeignKey(Courses_Category, related_name="cat",null=True, blank=True, on_delete=models.CASCADE)
    cat2 = models.ForeignKey(Courses_Category, related_name="cat2", null=True, blank=True, on_delete=models.CASCADE)
    t1 = models.ForeignKey(Trainer, related_name="Main", null=True, blank=True, on_delete=models.CASCADE)
    t2 = models.ForeignKey(Trainer, related_name="Secondary", null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.FileField(null=True, blank=True)
    fee = models.CharField(max_length=200, null=True, blank=True)
    review = models.IntegerField( null=True, blank=True)
    short_des = models.CharField(max_length=1000, null=True, blank=True)
    long_des = models.CharField(max_length=2000, null=True, blank=True)
    seo_des = models.CharField(max_length=2000, null=True, blank=True)
    seo_keys = models.CharField(max_length=2000, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    skill = models.CharField(max_length=200, null=True, blank=True)
    students = models.CharField(max_length=200, null=True, blank=True)
    classes = models.CharField(max_length=200, null=True, blank=True)
    l1 = models.CharField(max_length=200, null=True, blank=True)
    l2 = models.CharField(max_length=200, null=True, blank=True)
    l3 = models.CharField(max_length=200, null=True, blank=True)
    l4 = models.CharField(max_length=200, null=True, blank=True)
    l5 = models.CharField(max_length=200, null=True, blank=True)
    l6 = models.CharField(max_length=200, null=True, blank=True)
    l7 = models.CharField(max_length=200, null=True, blank=True)
    l8 = models.CharField(max_length=200, null=True, blank=True)
    l9 = models.CharField(max_length=200, null=True, blank=True)
    l10 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    p = models.CharField(max_length=200, null=True, blank=True)
    S1 = models.CharField(max_length=200, null=True, blank=True)
    S2 = models.CharField(max_length=200, null=True, blank=True)
    S3 = models.CharField(max_length=200, null=True, blank=True)
    S4 = models.CharField(max_length=200, null=True, blank=True)
    S5 = models.CharField(max_length=200, null=True, blank=True)
    S6 = models.CharField(max_length=200, null=True, blank=True)
    S7 = models.CharField(max_length=200, null=True, blank=True)
    S8 = models.CharField(max_length=200, null=True, blank=True)
    S9 = models.CharField(max_length=200, null=True, blank=True)
    S10 = models.CharField(max_length=200, null=True, blank=True)
    S11 = models.CharField(max_length=200, null=True, blank=True)
    S12 = models.CharField(max_length=200, null=True, blank=True)
    S13 = models.CharField(max_length=200, null=True, blank=True)
    S14 = models.CharField(max_length=200, null=True, blank=True)
    S15 = models.CharField(max_length=200, null=True, blank=True)


class Event_Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    usr = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    un = models.CharField(max_length=100, null=True, blank=True)
    ps = models.CharField(max_length=100, null=True, blank=True)

    cat = models.ForeignKey(Event_Category, on_delete=models.CASCADE, null=True, blank=True)
    img = models.FileField(null=True, blank=True)
    logo = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    call = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    map = models.CharField(max_length=2000, null=True, blank=True)
    topic = models.CharField(max_length=200, null=True, blank=True)
    host = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    skill = models.CharField(max_length=200, null=True, blank=True)
    file_url = models.CharField(max_length=500, null=True, blank=True)
    short_des = models.CharField(max_length=1000, null=True, blank=True)
    long_des = models.CharField(max_length=2000, null=True, blank=True)
    seo_des = models.CharField(max_length=2000, null=True, blank=True)
    seo_keys = models.CharField(max_length=2000, null=True, blank=True)
    students = models.CharField(max_length=2000, null=True, blank=True)
    l1 = models.CharField(max_length=200, null=True, blank=True)
    l2 = models.CharField(max_length=200, null=True, blank=True)
    l3 = models.CharField(max_length=200, null=True, blank=True)
    l4 = models.CharField(max_length=200, null=True, blank=True)
    l5 = models.CharField(max_length=200, null=True, blank=True)
    l6 = models.CharField(max_length=200, null=True, blank=True)
    l7 = models.CharField(max_length=200, null=True, blank=True)
    l8 = models.CharField(max_length=200, null=True, blank=True)
    l9 = models.CharField(max_length=200, null=True, blank=True)
    l10 = models.CharField(max_length=200, null=True, blank=True)
    fee = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    c_num = models.CharField(max_length=200, null=True, blank=True)
    n1 = models.CharField(max_length=200, null=True, blank=True)
    d1 = models.CharField(max_length=200, null=True, blank=True)
    w1 = models.CharField(max_length=200, null=True, blank=True)
    s1 = models.FileField(null=True, blank=True)
    n2 = models.CharField(max_length=200, null=True, blank=True)
    d2 = models.CharField(max_length=200, null=True, blank=True)
    w2 = models.CharField(max_length=200, null=True, blank=True)
    s2 = models.FileField(null=True, blank=True)
    n3 = models.CharField(max_length=200, null=True, blank=True)
    d3 = models.CharField(max_length=200, null=True, blank=True)
    w3 = models.CharField(max_length=200, null=True, blank=True)
    s3 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Dates(models.Model):
    Event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True, blank=True)
    certificate = models.BooleanField(default=False)
    start_date = models.DateField(max_length=200, null=True, blank=True)
    end_date = models.DateField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)






