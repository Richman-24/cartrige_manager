from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campus/', include("buildings.urls", namespace="campus")),
    path('cartriges/', include("cartriges.urls", namespace="cartriges")),
    path('devices/', include("devices.urls", namespace="devices")),
    path('operations/', include("operations.urls", namespace="operations")),
    path('', include("cartriges.urls")), # Временное решение, переадресация пока нет "главной"
]
