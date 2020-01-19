from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseNotFound
from django.views.generic.base import View

from core.models import Document


class DocumentView(View):

    def get(self, request, document_id):
        try:
            # links = Link.objects.filter(documents__id=1)
            document = Document.objects.get(pk=document_id)
        except ObjectDoesNotExist as e:
            return HttpResponseNotFound()

        return JsonResponse(
            list(
                map(
                    lambda x: dict(x),
                    document.links.all().values()
                )
            ),
            safe=False
        )