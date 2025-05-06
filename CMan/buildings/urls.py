from django.urls import path

from buildings.views import CampusListView

app_name="campus"


urlpatterns = [
    path('', CampusListView.as_view(), name="index"),
]