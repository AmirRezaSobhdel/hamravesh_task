from rest_framework import serializers

from dockerapp.models import App, Container


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = ["id", "name", "image", "envs", "command"]
        read_only_fields = ["id"]


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ["id", "run_time", "run_envs", "status", "logs"]
        read_only_fields = ["id", "run_time", "run_envs", "status", "logs"]
