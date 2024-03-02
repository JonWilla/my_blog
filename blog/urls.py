

from . import views
from django.urls import path, re_path  # Import re_path for regular expressions
from django.conf import settings  # Import settings
from django.views.static import serve  # Import serve to serve static files


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
# Serve static files
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
