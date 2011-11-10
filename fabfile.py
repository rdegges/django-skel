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


@task
def migrate(app=None):
    """Apply one (or more) migrations. If no app is specified, fabric will
    attempt to run a site-wide migration.

    :param str app: Django app name to migrate.
    """
    if app:
        local('%s migrate %s --noinput --settings=%s' % (env.run, app,
                env.settings))
    else:
        local('%(run)s migrate --noinput --settings=%(settings)s' % env)
