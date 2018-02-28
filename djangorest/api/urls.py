from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^municipalities/$', CreateMunicipalityView.as_view(), name="create_municipality"),
    url(r'^municipalities/(?P<pk>[0-9]+)/$',
        DetailsMunicipalityView.as_view(), name="details_municipality"),
    url(r'^categories/$', CreateCategoryView.as_view(), name="create_category"),
    url(r'^categories/(?P<pk>[\w\+%_& ]+)/$',
        DetailsCategoryView.as_view(), name="details_category"),
    url(r'^sources/$', CreatePollutantSourceView.as_view(), name="create_source"),
    url(r'^sources/(?P<pk>[0-9]+)/$',
        DetailsPollutantSourceView.as_view(), name="details_source"),
    url(r'^reports/$', CreateReportView.as_view(), name="create_report"),
    url(r'^reports/(?P<pk>[0-9]+)/$',
        DetailsReportView.as_view(), name="details_report"),
    url(r'^district/(?P<district>[\w\+%_& ]+)/$', GetDistrictInformation, name="get_district")
}

urlpatterns = format_suffix_patterns(urlpatterns)