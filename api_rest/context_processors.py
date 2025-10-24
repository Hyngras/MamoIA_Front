def static_version(request):
    from django.conf import settings
    return {"STATIC_VERSION": getattr(settings, "STATIC_VERSION", "1")}
