from django.http import JsonResponse
from django.views.generic.base import View

from core.models import Link, Document


class LinksView(View):

    def get(self, links_id):
        return JsonResponse(
            list(
                map(
                    lambda x: x.serialize(),
                    Link.objects.all()
                )
            ),
            safe=False
        )
