"""Management utilities."""


from os.path import abspath

from fabric.api import env, local, task
from fabric.context_managers import lcd


########## GLOBALS
env.root = abspath('skel')
env.admin = 'django-admin.py'
########## END GLOBALS


@task
def syncdb():
    """Run a syncdb."""
    with lcd(env.root):
        local('%(admin)s help' % env)
        local('%(admin)s syncdb --noinput' % env)
