from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campus/', include("buildings.urls", namespace="campus")),
    path('cartriges/', include("cartriges.urls", namespace="cartriges")),
    path('devices/', include("devices.urls", namespace="devices")),
    #path('support/', include("supports.urls", namespace="support")),
    path('', include("cartriges.urls", namespace="cartriges")),
]
