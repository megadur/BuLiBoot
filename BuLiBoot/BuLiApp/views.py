# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

class BestenlisteView(TemplateView):
    template_name = 'bl/bestenliste.html'

    def get_context_data(self, **kwargs):
        context = super(BestenlisteView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

class SpieltagView(TemplateView):
    template_name = 'st/st.html'

    def get_context_data(self, **kwargs):
        context = super(SpieltagView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

class NewsView(TemplateView):
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

class FormView(FormView):
    template_name = 'demo/form.html'
    form_class = ContactForm
