from django.urls import path

from cartriges.views import CartrigesListView, CartrigeDetailView

app_name="cartriges"


urlpatterns = [
    path('', CartrigesListView.as_view(), name="index"),
    path('<slug:cartrige_slug>/', CartrigeDetailView.as_view(), name="detail"),
    ]