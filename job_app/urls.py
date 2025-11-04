from django.urls import path
from .views import (
    ApplicantListCreateView, ApplicantDetailView,
    JobListCreateView, JobDetailView,
    ApplyView, ApplicationListView, ApplicationStatusUpdateView
)

urlpatterns = [
    path('applicants/', ApplicantListCreateView.as_view(), name='applicant-list-create'),
    path('applicants/<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('apply/', ApplyView.as_view(), name='apply'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/', ApplicationStatusUpdateView.as_view(), name='application-status-update'),
]