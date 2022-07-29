from django.urls import path

from .views import CityView, AgencyView, MatterView, UserView

core_patterns = ([
    path('city/', CityView.as_view()),
    path('agency/', AgencyView.as_view()),
    path('matter/', MatterView.as_view()),
    path('user/', UserView.as_view()),
], 'core')
