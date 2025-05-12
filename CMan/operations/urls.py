from django.urls import path

from operations.views import (
    OperationsListView,
    OperationsAddView,
    OperationsEditView,
    OperationsRemoveView,
)

app_name = "operations"


urlpatterns = [
    path("", OperationsListView.as_view(), name="index"),
    path("add/", OperationsAddView.as_view(), name="add"),
    path("edit/", OperationsEditView.as_view(), name="edit"),
    path("remove/", OperationsRemoveView.as_view(), name="remove"),
]
