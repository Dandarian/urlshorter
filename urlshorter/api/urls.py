from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('links/', views.LinkList.as_view()),
    path('links/<int:pk>/', views.LinkDetail.as_view()),
    re_path('^links/(?P<long_url>.+)/$', views.LinkList.as_view()),
    re_path('^links/(?P<short_url>.+)/$', views.LinkList.as_view()),
]

# Formats endings, for example .json
urlpatterns = format_suffix_patterns(urlpatterns)
