from CMan import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campus/', include("campus.urls", namespace="campus")),
    path('cartriges/', include("cartriges.urls", namespace="cartriges")),
    path('devices/', include("devices.urls", namespace="devices")),
    path('operations/', include("operations.urls", namespace="operations")),
    path('', include("cartriges.urls")), # Временное решение, переадресация пока нет "главной"
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]