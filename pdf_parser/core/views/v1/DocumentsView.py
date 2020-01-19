from django.db import transaction
from django.views.generic.base import View
from django.http import HttpResponseBadRequest, JsonResponse

from core.utils.pdf_parser import get_urls_from_file
from core.utils.url_checker import check_urls
from core.models import Link, Document


class DocumentsView(View):

    def get(self, request):
        return JsonResponse(
            list(
                map(
                    lambda x: dict(x),
                    Document.objects.all().values()
                )
            ),
            safe=False
        )

    @transaction.atomic
    def post(self, request):
        if 'document' not in request.FILES:
            return HttpResponseBadRequest('Missed required arg')

        # TODO: content-type and other checks required

        urls = get_urls_from_file(request.FILES['document'])

        existed_links = Link.objects.filter(url__in=urls)
        new_urls = set(urls) - set(map(lambda x: x.url, existed_links))
        new_urls = check_urls(new_urls)

        new_links = []
        for url, status in new_urls:
            link = Link(url=url, status=status)
            link.save()
            new_links.append(link)

        links = list(existed_links) + new_links

        new_document = Document(
            name=request.FILES['document'].name,
            urls_count=len(links)
        )

        new_document.save()
        new_document.links.add(*links)
        return JsonResponse({})
