from django.urls import path

from converter.apps import ConverterConfig
from converter.views import ConverterAPI

app_name = ConverterConfig.name

urlpatterns = [
    path("converter/", ConverterAPI.as_view(), name="converter"),
]