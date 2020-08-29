from django.forms import ModelForm
from django import forms
from .models import *


class AddNew_Course_Form(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ()
        widgets = {
            'cat': forms.Select(attrs={'class': 'form-control', "required": ''}),
            'cat2': forms.Select(attrs={'class': 'form-control'}),
            't1': forms.Select(attrs={'class': 'form-control', "required": ''}),
            't2': forms.Select(attrs={'class': 'form-control'}),
            'img':forms.FileInput(attrs={'class': 'form-control', "onchange":"readURL(this);"}),
            'url': forms.TextInput(attrs={'placeholder': 'Course Url', "class": "form-control", "required": ''}),
            'name': forms.TextInput(attrs={'placeholder': 'Course Title', "class": "form-control", "required": ''}),
            'fee': forms.TextInput(attrs={'placeholder': 'Course Fee', "class": "form-control", "required": ''}),
            'review': forms.TextInput(attrs={'placeholder': 'Course Review', "class": "form-control", "required": ''}),
            'short_des': forms.Textarea(
                attrs={'placeholder': 'Course Description in Short', "class": "form-control", "required": ''}),
            'long_des': forms.Textarea(attrs={'placeholder': 'Course Description in Long', "class": "form-control", "required": ''}),
            'seo_des': forms.Textarea(attrs={'placeholder': 'Course Description for Seo', "class": "form-control", "required": ''}),
            'seo_keys': forms.Textarea(attrs={'placeholder': 'Course KeyWord for SEO', "class": "form-control", "required": ''}),
            'duration': forms.TextInput(
                attrs={'placeholder': 'Course Duration', "class": "form-control", "required": ''}),
            'skill': forms.TextInput(
                attrs={'placeholder': 'Course Skill Level', "class": "form-control", "required": ''}),
            'students': forms.TextInput(
                attrs={'placeholder': 'Number of Students', "class": "form-control", "required": ''}),
            'classes': forms.TextInput(
                attrs={'placeholder': 'Number of Classes', "class": "form-control", "required": ''}),
            'l1': forms.TextInput(attrs={'placeholder': 'Key Point 1', "class": "form-control"}),
            'l2': forms.TextInput(attrs={'placeholder': 'Key Point 2', "class": "form-control"}),
            'l3': forms.TextInput(attrs={'placeholder': 'Key Point 3', "class": "form-control"}),
            'l4': forms.TextInput(attrs={'placeholder': 'Key Point 4', "class": "form-control"}),
            'l5': forms.TextInput(attrs={'placeholder': 'Key Point 5', "class": "form-control"}),
            'l6': forms.TextInput(attrs={'placeholder': 'Key Point 6', "class": "form-control"}),
            'l7': forms.TextInput(attrs={'placeholder': 'Key Point 7', "class": "form-control"}),
            'l8': forms.TextInput(attrs={'placeholder': 'Key Point 8', "class": "form-control"}),
            'l9': forms.TextInput(attrs={'placeholder': 'Key Point 9', "class": "form-control"}),
            'l10': forms.TextInput(attrs={'placeholder': 'Key Point 10', "class": "form-control"}),

        }


class Add_New_Trainer_Form(forms.ModelForm):
    class Meta:
        model = Trainer
        exclude = ()
        widgets = {
            'img':forms.FileInput(attrs={'class': 'form-control', "onchange":"readURL(this);"}),
            'name': forms.TextInput(attrs={'placeholder': 'Trainer Name', "class": "form-control", "required": ''}),
            'review': forms.TextInput(attrs={'placeholder': 'Trainer Review', "class": "form-control", "required": ''}),
            'position': forms.TextInput(attrs={'placeholder': 'Position', "class": "form-control", "required": ''}),
            'des': forms.Textarea(attrs={'placeholder': 'Description', "class": "form-control", "required": ''}),
            'mail': forms.TextInput(attrs={'placeholder': 'Mail ID', "class": "form-control", "required": ''}),


        }


class AddCourse_Title_Form(forms.ModelForm):
    class Meta:
        model = Title
        exclude = ()
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control', "required": ''}),
            'name': forms.TextInput(attrs={'placeholder': 'Title Name', "class": "form-control"}),
            'p': forms.TextInput(attrs={'placeholder': 'Title Position', "class": "form-control"}),
            'S1': forms.TextInput(attrs={'placeholder': 'Sub Title - 1', "class": "form-control"}),
            'S2': forms.TextInput(attrs={'placeholder': 'Sub Title - 2', "class": "form-control"}),
            'S3': forms.TextInput(attrs={'placeholder': 'Sub Title - 3', "class": "form-control"}),
            'S4': forms.TextInput(attrs={'placeholder': 'Sub Title - 4', "class": "form-control"}),
            'S5': forms.TextInput(attrs={'placeholder': 'Sub Title - 5', "class": "form-control"}),
            'S6': forms.TextInput(attrs={'placeholder': 'Sub Title - 6', "class": "form-control"}),
            'S7': forms.TextInput(attrs={'placeholder': 'Sub Title - 7', "class": "form-control"}),
            'S8': forms.TextInput(attrs={'placeholder': 'Sub Title - 8', "class": "form-control"}),
            'S9': forms.TextInput(attrs={'placeholder': 'Sub Title - 9', "class": "form-control"}),
            'S10': forms.TextInput(attrs={'placeholder': 'Sub Title - 10', "class": "form-control"}),
            'S11': forms.TextInput(attrs={'placeholder': 'Sub Title - 11', "class": "form-control"}),
            'S12': forms.TextInput(attrs={'placeholder': 'Sub Title - 12', "class": "form-control"}),
            'S13': forms.TextInput(attrs={'placeholder': 'Sub Title - 13', "class": "form-control"}),
            'S14': forms.TextInput(attrs={'placeholder': 'Sub Title - 14', "class": "form-control"}),
            'S15': forms.TextInput(attrs={'placeholder': 'Sub Title - 15', "class": "form-control"}),

        }


class AddNew_Event_Form(forms.ModelForm):
    class Meta:
        model = Events #44
        exclude = ("user",)
        widgets = {
            'cat': forms.Select(attrs={'class': 'form-control', "required": ''}),
            'img':forms.FileInput(attrs={'class': 'form-control', "onchange":"readURL(this);"}),
            'logo':forms.FileInput(attrs={'class': 'form-control', "onchange":"readURL1(this);"}),
            'url': forms.TextInput(attrs={'placeholder': 'Event Url', "class": "form-control", "required": ''}),
            'title': forms.TextInput(attrs={'placeholder': 'Event Title', "class": "form-control", "required": ''}),
            'address': forms.TextInput(attrs={'placeholder': 'Event Address', "class": "form-control", "required": ''}),
            'call': forms.TextInput(attrs={'placeholder': 'Contact Number', "class": "form-control", "required": ''}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', "class": "form-control", "required": ''}),
            'topic': forms.TextInput(attrs={'placeholder': 'Event Topic', "class": "form-control", "required": ''}),
            'host': forms.TextInput(attrs={'placeholder': 'Event Host', "class": "form-control", "required": ''}),
            'file': forms.FileInput(attrs={'class': 'form-control', "onchange": "readURL(this);"}),
            'file_url': forms.TextInput(attrs={'placeholder': 'File Url', "class": "form-control", "required": ''}),
            'map': forms.Textarea(attrs={'placeholder': 'Event Map Location', "class": "form-control", "required": ''}),
            'short_des': forms.Textarea(
                attrs={'placeholder': 'Course Description in Short', "class": "form-control", "required": ''}),
            'long_des': forms.Textarea(attrs={'placeholder': 'Course Description in Long', "class": "form-control", "required": ''}),
            'seo_des': forms.Textarea(attrs={'placeholder': 'Course Description for Seo', "class": "form-control", "required": ''}),
            'seo_keys': forms.Textarea(attrs={'placeholder': 'Course KeyWord for SEO', "class": "form-control", "required": ''}),
            'duration': forms.TextInput(
                attrs={'placeholder': 'Course Duration', "class": "form-control", "required": ''}),
            'skill': forms.TextInput(
                attrs={'placeholder': 'Course Skill Level', "class": "form-control", "required": ''}),
            'l1': forms.TextInput(attrs={'placeholder': 'Key Point 1', "class": "form-control"}),
            'l2': forms.TextInput(attrs={'placeholder': 'Key Point 2', "class": "form-control"}),
            'l3': forms.TextInput(attrs={'placeholder': 'Key Point 3', "class": "form-control"}),
            'l4': forms.TextInput(attrs={'placeholder': 'Key Point 4', "class": "form-control"}),
            'l5': forms.TextInput(attrs={'placeholder': 'Key Point 5', "class": "form-control"}),
            'l6': forms.TextInput(attrs={'placeholder': 'Key Point 6', "class": "form-control"}),
            'l7': forms.TextInput(attrs={'placeholder': 'Key Point 7', "class": "form-control"}),
            'l8': forms.TextInput(attrs={'placeholder': 'Key Point 8', "class": "form-control"}),
            'l9': forms.TextInput(attrs={'placeholder': 'Key Point 9', "class": "form-control"}),
            'l10': forms.TextInput(attrs={'placeholder': 'Key Point 10', "class": "form-control"}),
            'fee': forms.TextInput(attrs={'placeholder': 'Event Charge', "class": "form-control"}),
            'time': forms.TextInput(attrs={'placeholder': 'Starting Time', "class": "form-control"}),
            'c_num': forms.TextInput(attrs={'placeholder': 'Starting Certificate Number', "class": "form-control"}),
            'students': forms.TextInput(attrs={'placeholder': 'Registered Students', "class": "form-control"}),

            'n1': forms.TextInput(attrs={'placeholder': 'First Name', "class": "form-control"}),
            'd1': forms.TextInput(attrs={'placeholder': 'Position', "class": "form-control"}),
            'w1': forms.TextInput(attrs={'placeholder': 'Where', "class": "form-control"}),
            's1': forms.FileInput({'class': 'form-control', "onchange":"readURL2(this);"}),

            'n2': forms.TextInput(attrs={'placeholder': 'Second Name', "class": "form-control"}),
            'd2': forms.TextInput(attrs={'placeholder': 'Position', "class": "form-control"}),
            'w2': forms.TextInput(attrs={'placeholder': 'Where', "class": "form-control"}),
            's2': forms.FileInput({'class': 'form-control', "onchange": "readURL3(this);"}),

            'n3': forms.TextInput(attrs={'placeholder': 'Third Name', "class": "form-control"}),
            'd3': forms.TextInput(attrs={'placeholder': 'Position', "class": "form-control"}),
            'w3': forms.TextInput(attrs={'placeholder': 'Where', "class": "form-control"}),
            's3': forms.FileInput({'class': 'form-control', "onchange": "readURL4(this);"}),

            'un': forms.TextInput(attrs={'placeholder': 'Username', "class": "form-control"}),
            'ps': forms.TextInput(attrs={'placeholder': 'Password', "class": "form-control"}),
        }


class Add_New_Dates_Form(forms.ModelForm):
    class Meta:
        model = Dates
        exclude = ("certificate",)
        widgets = {
            'Event':forms.Select(attrs={'class': 'form-control', "required": ''}),
            'start_date': forms.TextInput(attrs={'placeholder': 'Start Date', "class": "form-control", "required": ''}),
            'end_date': forms.TextInput(attrs={'placeholder': 'End Date', "class": "form-control", "required": ''}),
            'date': forms.TextInput(attrs={'placeholder': 'Date', "class": "form-control", "required": ''}),
        }