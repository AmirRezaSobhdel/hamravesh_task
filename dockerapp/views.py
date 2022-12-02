from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from dockerapp import docker_utils
from dockerapp.docker_utils import run_app
from dockerapp.models import App, Container
from dockerapp.serializers import AppSerializer, ContainerSerializer
from dockerapp.tasks import run_docker_container


class AppViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ContainerViewSet(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def get_app(self) -> App:
        return get_object_or_404(
            App.objects,
            id=self.kwargs["app_id"],
            owner=self.request.user.id,
        )

    def get_queryset(self):
        return Container.objects.filter(app=self.get_app()).all()

    serializer_class = ContainerSerializer

    def create(self, request, *args, **kwargs):
        app = self.get_app()
        run_docker_container.delay(app.id)
        return Response('container creation is now in progress', status=status.HTTP_201_CREATED)






