import docker

from dockerapp.models import App

client = docker.from_env()


def run_app(app: App):
    container = client.containers.run(app.image, app.command, environment=dict(app.envs), detach=True)
    return container.logs()

