from django.urls import path

from dockerapp import views

app_name = "docker_app"
urlpatterns = [
    path("", views.AppViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        views.AppViewSet.as_view(
            {"get": "retrieve", "delete": "destroy", "put": "update"}
        ),
    ),

    path("<int:app_id>/run/", views.ContainerViewSet.as_view({"get": "list", "post": "create"})),
]
