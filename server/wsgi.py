import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
# from vmprof import DjangoVMPROF


# vmprof = DjangoVMPROF("localhost", 8000, "token")

# app = vmprof(get_wsgi_application())
app = get_wsgi_application()