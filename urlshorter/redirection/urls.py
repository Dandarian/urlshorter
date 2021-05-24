from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<str:short_url>/', views.root, name='root'),
]

# Formats endings, for example .json
urlpatterns = format_suffix_patterns(urlpatterns)
