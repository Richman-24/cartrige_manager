from django.urls import path

from operations.views import (
    OperationsListView,
    OperationsAddView,
    OperationsRemoveView,
)

app_name = "operations"


urlpatterns = [
    path("", OperationsListView.as_view(), name="index"),
    path("add/", OperationsAddView.as_view(), name="add"),
    path("add/<int:inv_number>", OperationsAddView.as_view(), name="add_from_device"),
    path("add/<slug:cartrige_slug>", OperationsAddView.as_view(), name="add_from_cartrige"),
    path("<int:operation_id>/remove/", OperationsRemoveView.as_view(), name="remove"),
]
