from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

from .views import v1


def results(request):
    response = "You're looking at the results of question"
    return HttpResponse(response)


urlpatterns = [
    url(r'^links$', v1.LinksView.as_view()),
    url(r'^documents$', v1.DocumentsView.as_view()),
    url(r'^documents/(?P<document_id>\d+)/links$', v1.DocumentView.as_view()),
]
