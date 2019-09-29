import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_api_nbu.settings')
application = get_wsgi_application()
