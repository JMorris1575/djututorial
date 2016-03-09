from django.core.paginator import (
    EmptyPage, PageNotAnInteger, Paginator)
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, View)

from core.utils import UpdateView
from .utils import PageLinksMixin
from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import Startup, Tag, NewsLink


class NewsLinkCreate(CreateView):
    form_class = NewsLinkForm
    model = NewsLink


class NewsLinkDelete(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return self.object.startup.get_absolute_url()

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        startup = newslink.startup
        newslink.delete()
        redirect(startup)


class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        context = {
            'form': self.form_class(
                instance=newslink),
            'newslink': newslink,
        }
        print('Template Name = ', self.template_name)
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        bound_form = self.form_class(
            request.POST, instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': bound_form,
                'newslink': newslink,
            }
            return render(
                request,
                self.template_name,
                context)


class StartupCreate(CreateView, View):
    form_class = StartupForm
    model = Startup


class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list')


class StartupDetail(DetailView):
    model = Startup


class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5 # 5 items per page


class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup


class TagCreate(CreateView, View):
    form_class = TagForm
    model = Tag


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')


class TagDetail(DetailView):
    model = Tag


class TagList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Tag


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag