"""Management utilities."""


from fabric.api import env, local, task


########## GLOBALS
env.run = 'heroku run python skel/manage.py'
env.settings = 'settings.prod'
########## END GLOBALS


@task
def syncdb():
    """Run a syncdb."""
    local('%(run)s syncdb --noinput --settings=%(settings)s' % env)
