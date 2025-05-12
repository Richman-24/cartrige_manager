from django.urls import path

from buildings.views import CampusListView, CampusCabinetView

app_name="campus"


urlpatterns = [
    path('', CampusListView.as_view(), name="index"),
    path('<int:cabinet_pk>/', CampusCabinetView.as_view(), name="cabinet"),

]