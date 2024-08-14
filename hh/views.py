
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from hh.forms import ResumeForm, VacancyForm
from hh.models import Vacancy, Resume


# Create your views here.

@method_decorator(login_required(login_url='base'), name='dispatch')
class VacancyView(ListView):
    template_name = 'hh/index.html'
    model = Vacancy
    context_object_name = 'vacancies'


@method_decorator(login_required(login_url='base'), name='dispatch')
class VacancyDetailView(DetailView):
    template_name = 'hh/vacancy_detail.html'
    model = Vacancy
    context_object_name = 'vacancy'


@method_decorator(login_required(login_url='base'), name='dispatch')
class ResumeDetailView(DetailView):
    template_name = 'hh/resume_detail.html'
    model = Resume
    context_object_name = 'vacancy'


@method_decorator(login_required(login_url='base'), name='dispatch')
class ResumeCreateView(CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'hh/resume.html'
    context_object_name = 'resumes'

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['resume'] = Resume.objects.get(user=self.request.user)
        except Resume.DoesNotExist:
            context['resume'] = None
        return context

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.user = self.request.user
        resume.save()

        return redirect('resume')


@method_decorator(login_required(login_url='base'), name='dispatch')
def resume_delete(request, pk):
    if request.user.is_staff:
        return redirect('index')
    resume = Resume.objects.get(pk=pk)
    if resume.user.id != request.user.id:
        return redirect('error')
    resume.delete()
    return redirect('resume')


@method_decorator(login_required(login_url='base'), name='dispatch')
class ResumesListView(ListView):
    model = Resume
    template_name = 'hh/resumes.html'
    context_object_name = 'resumes'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index')
        return super().get(request, *args, **kwargs)


@method_decorator(login_required(login_url='base'), name='dispatch')
class VacancyCreateView(CreateView):
    form_class = VacancyForm
    template_name = 'hh/vacancy.html'
    model = Vacancy
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.user = self.request.user
        resume.save()

        return redirect('vacancy')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index')
        return super().get(request, *args, **kwargs)


@method_decorator(login_required(login_url='base'), name='dispatch')
def vacancy_delete(request, pk):
    if not request.user.is_staff:
        return redirect('index')
    vacancy = Vacancy.objects.get(pk=pk)
    if vacancy.user.id != request.user.id:
        return redirect('error')
    vacancy.delete()

    return redirect('vacancy')


@method_decorator(login_required(login_url='base'), name='dispatch')
class VacancyUpdateView(UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'hh/vacancy_update.html'
    success_url = reverse_lazy('vacancy')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index')
        return super().get(request, *args, **kwargs)


@method_decorator(login_required(login_url='base'), name='dispatch')
class ResumeUpdateView(UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'hh/resume_update.html'
    success_url = reverse_lazy('resume')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index')
        return super().get(request, *args, **kwargs)

