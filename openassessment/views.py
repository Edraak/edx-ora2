"""Django views implementing the XBlock workbench.
This code is in the Workbench layer.
"""

import logging
import mimetypes
import os

from django.conf import settings

from django.http import HttpResponse, Http404


log = logging.getLogger(__name__)


def package_resource(_request, block_type, resource):
    """
    Wrapper for `pkg_resources` that tries to access a resource and, if it
    is not found, raises an Http404 error.
    """
    mimetype, _ = mimetypes.guess_type(resource)
    with open(os.path.join(settings.BASE_DIR, 'openassessment/xblock', resource)) as fp:
        return HttpResponse(fp, content_type=mimetype)
