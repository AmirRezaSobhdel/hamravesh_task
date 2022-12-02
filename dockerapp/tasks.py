from celery import shared_task

from docker.errors import ImageNotFound, APIError

from dockerapp.docker_utils import run_app
from dockerapp.models import App, Container


@shared_task
def run_docker_container(app_id):
    app = App.objects.get(id=app_id)

    container = Container()
    container.app = app
    container.run_envs = app.envs
    container.status = Container.STATUS_RUNNING
    container.save()
    try:
        logs = run_app(app)
        container.logs = logs
        container.status = Container.STATUS_FINISHED
    except (ImageNotFound, APIError) as e:
        container.status = Container.STATUS_ERROR_CREATING_THE_CONTAINER
        print(e)
    finally:
        container.save()

    # todo: notify user then
