
from django.conf.urls import url
from django.contrib import admin
from New_Home.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home, name="home"),
    url(r'^TechSim/Login/$', Login, name="login"),
    url(r'^TechSim/Logout/$', Logout, name="logout"),
    url(r'^TechSim/Register/$', Register, name="register"),
    url(r'^TechSim/Contact-Us/$', ContactUs, name="contact"),
    url(r'^TechSimPLUS_New_Batches_and_Workshops/$', Event_List, name="all_events"),
    url(r'^(?P<course>[\w-]+)/$', Courses_Details, name="course_details"),
    url(r'^Events/(?P<events>[\w-]+)/$', Events_Details, name="events_details"),


    # Admin Panel Url's
url(r'^TechSim/Admin/Dashboard/$', Admin_Home, name="admin_home"),
url(r'^TechSim/Admin/Banners/$', All_Banners, name="banners"),
url(r'^TechSim/Admin/Add_New_Banner/$', Add_New_Banner, name="Add_New_Banner"),
url(r'^TechSim/Admin/Edit_New_Banner/(?P<b_id>[\w-]+)/(?P<type>[\w-]+)/$', Edit_New_Banner, name="edit_New_Banner"),

url(r'^TechSim/Admin/Courses_Categories/(?P<type>[\w-]+)/(?P<c_id>[\w-]+)/$', All_Courses_Categories, name="courses_categories"),
url(r'^TechSim/Admin/Courses/(?P<type>[\w-]+)/(?P<c_id>[\w-]+)/$', All_Courses, name="courses"),
url(r'^TechSim/Admin/Trainers/(?P<type>[\w-]+)/(?P<t_id>[\w-]+)/$', All_Trainers, name="trainers"),
url(r'^TechSim/Admin/Content/(?P<type>[\w-]+)/(?P<c_id>[\w-]+)/$', All_Content, name="content"),

url(r'^TechSim/Admin/Event_Categories/(?P<type>[\w-]+)/(?P<c_id>[\w-]+)/$', All_Events_Categories, name="events_categories"),
url(r'^TechSim/Admin/Events/(?P<type>[\w-]+)/(?P<c_id>[\w-]+)/$', All_Events, name="events"),
url(r'^TechSim/Admin/Add_Events/$', Add_New_Date, name="add_event_date"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)