from django.urls import path

from capture_email.core.views import Index

app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='home'),
]
