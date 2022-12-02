from django.db import models
from django.contrib.auth import get_user_model


class App(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    envs = models.JSONField(default=dict)
    command = models.TextField(blank=True, null=True)


class Container(models.Model):

    STATUS_RUNNING = 'Running'
    STATUS_FINISHED = 'Finished'
    STATUS_ERROR_CREATING_THE_CONTAINER = 'Error'
    STATUS_CHOICES = [
        (STATUS_RUNNING, 'Running'),
        (STATUS_RUNNING, 'Finished'),
        (STATUS_ERROR_CREATING_THE_CONTAINER, "Error creating the container"),
    ]

    app = models.ForeignKey(App, on_delete=models.SET_NULL, blank=True, null=True)
    # docker_container_internal_id = models.CharField(max_length=64)
    run_time = models.DateTimeField(auto_now_add=True)
    run_envs = models.JSONField(default=dict, blank=True)
    status = models.CharField(default=STATUS_RUNNING, choices=STATUS_CHOICES, max_length=20)
    logs = models.TextField(null=True, blank=True)
