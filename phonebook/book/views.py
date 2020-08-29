from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, ContactForm, SearchForm, AddGroup
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import Contact, Group, Membership
from django.db.models import Q
from phonebook import settings
from django.http import HttpResponse
import csv
from datetime import datetime
import re

URL_RENDER = {
    'view_login': 'phonebook/login.html',
    'view_lists_contacts': 'phonebook/lists_contacts.html',
    'view_edit_contact': 'phonebook/edit_contact.html',
    'view_call': 'phonebook/call.html',
}


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        query = or_query
    return query


def view_login(request):
    error = False
    login_form = LoginForm()

    if request.user.is_authenticated():
        return redirect('phonebook_lists_contacts')

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('phonebook_lists_contacts')
            else:
                error = True
    return render(request, 'phonebook/login.html', {'form' : login_form, 'error': error})


def view_logout(request):
    logout(request)
    return redirect(reverse(view_login))


LOGIN_URL = view_login

@login_required(login_url=LOGIN_URL)
def view_lists_contacts(request):
    newcontact_form = ContactForm()
    search_form = SearchForm()
    add_group = AddGroup()
    contacts = Contact.objects.filter(Q(user_id=request.user)).order_by('id')
    group = Group.objects.filter(Q(user_id=request.user)).order_by('id')

    arg = {'search_form':search_form, 'AddGroup': add_group, 'groups': group, 'group': group, 'contacts':contacts, 'newcontact_form':newcontact_form}
    return render(request, 'phonebook/lists_contacts.html', arg)

def add_group(request):
    if request.method == "POST":
        add_group = AddGroup(request.POST)
        if add_group.is_valid():
            query = add_group.cleaned_data["group"]
            group = Group.objects.filter(Q(user_id=request.user, name = query))
            if group:
                return redirect('phonebook_lists_contacts')
            else:
                Group.objects.create(name = query, user_id=request.user)
                return redirect('phonebook_lists_contacts')
    return redirect('phonebook_lists_contacts')




@login_required(login_url=LOGIN_URL)
def view_search_contact(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data["query"]
            return redirect(reverse(view_search_contact_query, kwargs={'query': query}))
    return redirect(reverse(view_lists_contacts))


@login_required(login_url=LOGIN_URL)
def view_search_contact_query(request, query):
    newcontact_form = ContactForm()
    search_form = SearchForm()
    contacts = Contact.objects.filter(
        get_query(query, ['firstname', 'lastname', 'email', 'phone', 'mobile_phone'])).order_by('id')
    return render(request, URL_RENDER['view_lists_contacts'], locals())



def contacts(request):
    if request.method == 'POST':
        newcontact_form = ContactForm()
        search_form = SearchForm()
        add_group = AddGroup()
        group = Group.objects.filter(Q(user_id=request.user)).order_by('id')
        grou = request.POST.get('group_select')
        gro = Group.objects.get(Q(user_id=request.user, name=grou))
        contacts = gro.members.all()
        arg = {'search_form': search_form, 'AddGroup': add_group, 'groups': group, 'group': group, 'contacts': contacts,
               'newcontact_form': newcontact_form}
        return render(request, 'phonebook/lists_contacts.html', arg)
    else:
        return redirect('phonebook_lists_contacts')




@login_required(login_url=LOGIN_URL)
def view_new_contact(request):
    if request.method == 'POST':
        newcontact_form = ContactForm(request.POST)
        if newcontact_form.is_valid():
            firstname, lastname = newcontact_form.cleaned_data["firstname"], newcontact_form.cleaned_data["lastname"]
            email, group = newcontact_form.cleaned_data["email"], request.POST.get('group_select')
            mobile_phone = newcontact_form.cleaned_data["mobile_phone"]
            contact = Contact.objects.create(firstname=firstname, lastname=lastname, email=email,
                              mobile_phone=mobile_phone, user_id=request.user)
            gro = Group.objects.get(Q(user_id=request.user, name=group))
            m = Membership(person= contact, group = gro)
            m.save()

            return redirect(reverse(view_lists_contacts))
    return redirect(reverse(view_lists_contacts))


@login_required(login_url=LOGIN_URL)
def view_delete(request, contact_id):
    contact = Contact.objects.filter(Q(user_id=request.user, id=contact_id))
    if contact:
        contact.delete()
    return redirect(reverse(view_lists_contacts))


@login_required(login_url=LOGIN_URL)
def view_edit_contact(request, contact_id):
    contact = Contact.objects.filter(Q(user_id=request.user, id=contact_id))
    if not contact:
        return redirect(reverse(view_lists_contacts), locals())
    contact = contact[0]
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            firstname, lastname = contact_form.cleaned_data["firstname"], contact_form.cleaned_data["lastname"]
            email, phone = contact_form.cleaned_data["email"], contact_form.cleaned_data["phone"]
            mobile_phone = contact_form.cleaned_data["mobile_phone"]
            contact.firstname, contact.lastname, contact.email = firstname, lastname, email
            contact.phone, contact.mobile_phone = phone, mobile_phone
            contact.save()
            return redirect(reverse(view_lists_contacts))
    else:
        contact_form = ContactForm(initial={
            'firstname': contact.firstname,
            'lastname': contact.lastname,
            'email': contact.email,
            'phone': contact.phone,
            'mobile_phone': contact.mobile_phone,
        })
    return render(request, URL_RENDER['view_edit_contact'], locals())


@login_required(login_url=LOGIN_URL)
def view_call(request, num=0):
    url_click_to_call = str(settings.URL_CLICK_TO_CALL) + str(num)
    return render(request, URL_RENDER['view_call'], locals())


@login_required(login_url=LOGIN_URL)
def exports_contacts(request):
    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment; filename="exports_contacts_%s.csv"' % \
                                      datetime.now().strftime('%Y%m%d_%H%M%S')
    writer = csv.writer(response)
    writer.writerow(['Firstname', 'Lastname', 'Email', 'Phone', 'Mobile phone'])
    contacts = Contact.objects.filter(Q(user_id=request.user)).order_by('id')
    for contact in contacts:
        writer.writerow([contact.firstname, contact.lastname, contact.email, contact.phone, contact.mobile_phone])
    return response

def send(request):
    if request.method == 'POST':
        Id = request.POST.get('sender')
        number = request.POST.get('mobile')
        msg = request.POST.get('message')
        return render(request, 'phonebook/send_sms.html', {'number': number})
    return render(request, 'phonebook/result.html')

def select(request):
    sel = True
    select =  request.session['numbers']
    if request.method == 'POST':
        Id = request.POST.get('sender')
        msg = request.POST.get('message')
        return render(request, 'phonebook/send_sms.html', {'number': select})
    return render(request, 'phonebook/result.html', {'select': sel})


def send_sms(request):
    sel = False
    if request.method == 'POST':
        select = request.POST.getlist('check_list')
        if not select:
            return redirect('send')
        else:
            request.session['numbers'] = select
            return redirect('select')
        return render(request, 'phonebook/result.html', {'select':sel})