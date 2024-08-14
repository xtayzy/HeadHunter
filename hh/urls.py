from django.urls import path
from hh import views

urlpatterns = [
    path('', views.VacancyView.as_view(), name='index'),
    path('error/', views.TemplateView.as_view(template_name='hh/error.html'), name='error'),
    path('vacancy/<int:pk>', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('resume/', views.ResumeCreateView.as_view(), name='resume'),
    path('resume-delete/<int:pk>', views.resume_delete, name='resume_delete'),
    path('resume-update/<int:pk>', views.ResumeUpdateView.as_view(), name='resume_update'),
    path('resumes/', views.ResumesListView.as_view(), name='resumes'),
    path('resume/<int:pk>', views.ResumeDetailView.as_view(), name='resume_detail'),
    path('vacancy-create/', views.VacancyCreateView.as_view(), name='vacancy'),
    path('vacancy-delete/<int:pk>', views.vacancy_delete, name='vacancy_delete'),
    path('vacancy-update/<int:pk>', views.VacancyUpdateView.as_view(), name='vacancy_update'),
]
