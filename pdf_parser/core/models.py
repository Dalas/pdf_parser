from django.db import models


ACTIVE = 'ACTIVE'
BROKEN = 'BROKEN'
LIVENESS_CHECK_FAILED = 'LIVENESS_CHECK_FAILED'

STATUSES = (
    ('ACTIVE', 'Alive'),
    ('BROKEN', 'Broken'),
    ('LIVENESS_CHECK_FAILED', 'Liveness Check Failed'),
)


class Document(models.Model):

    name = models.TextField(unique=False, null=False, blank=False)
    urls_count = models.IntegerField(unique=False)

    links = models.ManyToManyField('Link', related_name='documents')


class Link(models.Model):

    url = models.URLField(max_length=2048, blank=False, unique=True)
    status = models.CharField(max_length=64, choices=STATUSES, blank=False)

    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'documents_count': self.documents.count()
        }
