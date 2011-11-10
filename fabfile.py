"""Management utilities."""


from fabric.api import local, task
from fabric.context_managers import lcd


########## GLOBALS
PROJECT_ROOT = 'skel'
########## END GLOBALS


@task
def syncdb():
    """Run a syncdb."""
    with lcd('skel'):
        local('django-admin.py syncdb --noinput')
