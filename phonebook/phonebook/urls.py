"""phonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from book import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.view_login, name='phonebook_login_page'),
    url(r'^send_sms', views.send_sms, name='send_sms'),
    url(r'^send', views.send, name='send'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^add_group', views.add_group, name='add_group'),
    url(r'^select', views.select, name='select'),
    url(r'^logout/', views.view_logout, name='phonebook_logout'),
    url(r'^lists_contacts/', views.view_lists_contacts, name='phonebook_lists_contacts'),
    url(r'^search_contact/', views.view_search_contact, name='phonebook_search_contact'),
    url(r'^search_contact=(?P<query>\w+)', views.view_search_contact_query, name='phonebook_search_contact_query'),
    url(r'^new_contact/', views.view_new_contact, name='phonebook_new_contact'),
    url(r'^delete/(?P<contact_id>\d+)/$', views.view_delete, name='phonebook_delete'),
    url(r'^edit/(?P<contact_id>\d+)/$', views.view_edit_contact, name='phonebook_edit'),
    url(r'^call/(?P<num>\d+)/$', views.view_call, name='phonebook_call'),
    url(r'^exports_contacts/$', views.exports_contacts, name='phonebook_exports_contacts'),
]
