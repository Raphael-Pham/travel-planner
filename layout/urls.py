from django.urls import path
from .views import home_view, landing_view, support_view, account_view

urlpatterns = [
    path('', landing_view, name='landing'),
    path('home/', home_view, name='home'),
    path('support/', support_view, name='support'),
    path('account/', account_view, name='account'),
]