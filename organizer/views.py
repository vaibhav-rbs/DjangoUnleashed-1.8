from django.shortcuts import (
    get_object_or_404, render)
from django.views.generic import View

from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import Startup, Tag
from .utils import ObjectCreateMixin


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink.startup)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup})


def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()})


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})
