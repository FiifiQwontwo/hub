from django.urls import path
from .views import *

urlpatterns = [

    path('applicant_list_api/', ApplicantViewSet.as_view({'get': 'list', }), name='applicant_api'),
    path('applicant_create/', ApplicantViewSet.as_view({'post': 'create'}), name='new_applicant'),
    path('ids/', IdViewSet.as_view({'get': 'list', }), name='ids_list'),
    path('ls_stages/', StageViewSet.as_view({'get': 'list', }), name='stage_list'),
    path('ls_education/', EducationViewSet.as_view({'get': 'list', }), name='stage_list')
]
