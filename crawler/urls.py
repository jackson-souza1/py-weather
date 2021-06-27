from django.urls import path
from crawler.views import app
urlpatterns = [
    path(route='metrics', view=app, name='app'),
]