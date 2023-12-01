from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Contact
from .test_form import ContactForm # in tutorial this was named contact_form.py ~ contact_form -- fix this later

class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
