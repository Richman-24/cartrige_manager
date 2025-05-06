from django.urls import path

from cartriges.views import CartrigesListView, CartrigeDetailView#cartriges_detail_view

app_name="cartriges"


urlpatterns = [
    path('', CartrigesListView.as_view(), name="index"),
    #path('<slug:cartrige_slug>', cartriges_detail_view, name="detail"),
    path('<slug:cartrige_slug>', CartrigeDetailView.as_view(), name="detail"),


]