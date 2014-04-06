import os
import sys
path = '/srv/www/Appliedshop'
if path not in sys.path:
        sys.path.insert(0, '/srv/www/Appliedshop')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Appliedshop.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

