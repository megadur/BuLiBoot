# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import ContactForm
from BuLiApp.forms import UserForm

class Util():
    def universal_get(self, view, request, *args, **kwargs):
        context = view.get_context_data(**kwargs)
        if("spieltag" in request.GET.keys()):
            spieltag = int(request.GET["spieltag"])
        else:
            spieltag=3
        context["spieltag"]=spieltag
        return view.render_to_response(context)

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message. You are on the home screen.')
        return context
    def get(self, request, *args, **kwargs):
        return Util().universal_get(self, request)

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
        return context
    def get(self, request, *args, **kwargs):
        messages.success(self.request, 'Erfolgreich gespeichert!')
        return Util().universal_get(self, request)

class NewsView(TemplateView):
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

class ImpressumView(TemplateView):
    template_name = 'impress.html'

    def get_context_data(self, **kwargs):
        context = super(ImpressumView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

class UserFormView(FormView):
    template_name = 'user/user.html'
    form_class = UserForm


class FormView(FormView):
    template_name = 'demo/form.html'
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = 'demo/form_horizontal.html'
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = 'demo/form_inline.html'
    form_class = ContactForm


class PaginationView(TemplateView):
    template_name = 'demo/pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(10000):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context

class TestPageView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super(TestPageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message. You are on the home screen.')
        return context
    def get(self, request, *args, **kwargs):
        return Util().universal_get(self, request)
