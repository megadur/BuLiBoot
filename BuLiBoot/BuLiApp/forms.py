# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


RADIO_CHOICES = (
    ('1', 'Radio 1'),
    ('2', 'Radio 2'),
)

MEDIA_CHOICES = (
    ('Audio', (
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
    )
    ),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD'),
    )
    ),
    ('unknown', 'Unknown'),
)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='Maximum 100 chars.')
    message = forms.CharField()
    sender = forms.EmailField()
    secret = forms.CharField(initial=42, widget=forms.HiddenInput)
    cc_myself = forms.BooleanField(required=False, help_text='You will get a copy in your mailbox.')
    select1 = forms.ChoiceField(choices=RADIO_CHOICES)
    select2 = forms.MultipleChoiceField(
        choices=RADIO_CHOICES,
        help_text='Check as many as you like.',
    )
    select3 = forms.ChoiceField(choices=MEDIA_CHOICES)
    select4 = forms.MultipleChoiceField(
        choices=MEDIA_CHOICES,
        help_text='Check as many as you like.',
    )
    category1 = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    category2 = forms.MultipleChoiceField(
        choices=RADIO_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        help_text='Check as many as you like.',
    )
    category3 = forms.ChoiceField(widget=forms.RadioSelect, choices=MEDIA_CHOICES)
    category4 = forms.MultipleChoiceField(
        choices=MEDIA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        help_text='Check as many as you like.',
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

class UserForm(forms.Form):
    anzeige_name = forms.CharField(max_length=10, help_text='Maximum 10 chars.')
    voller_name= forms.CharField(max_length=25, help_text='Maximum 15 chars.')
    email= forms.EmailField()
    Altes_Passwort = forms.CharField(initial=42, widget=forms.PasswordInput,help_text='Nur zum Ändern eingeben.',)
    Neues_Passwort = forms.CharField(initial=42, widget=forms.PasswordInput)
    Neues_Passwort_Wiederholen = forms.CharField(initial=42, widget=forms.PasswordInput)
    spam = forms.BooleanField(required=False, help_text='Benachrichtige mich über Änderungen.')
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

class PasswordForm(forms.Form):
    AltesPasswort = forms.CharField(initial=42, widget=forms.PasswordInput)
    NeuesPasswort = forms.CharField(initial=42, widget=forms.PasswordInput)
    NeuesPasswortWiederholen = forms.CharField(initial=42, widget=forms.PasswordInput)
    cc_myself = forms.BooleanField(required=False, help_text='Benachrichtige mich..')
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data
