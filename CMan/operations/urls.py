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
    path("<int:operation_id>/remove/", OperationsRemoveView.as_view(), name="remove"),
]
