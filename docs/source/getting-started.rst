Getting Started
===============

So you're ready to start your next Django project! Let me be your guide. Over
the next few minutes we'll be taking a magical journey together >:)


Creating a New Project
----------------------

To create your new project, run the following command, substituting ``woot``
for whatever you'd like to name your new project::

    $ django-admin.py startproject --template=https://github.com/rdegges/django-skel/zipball/master woot
    $ cd woot
    $ ls
    docs/  fabfile.py  gunicorn.py.ini  manage.py  Procfile  README.md  reqs/ requirements.txt  woot/  wsgi.py

The next thing you'll probably want to do is remove my project docs::

    $ rm -rf docs README.md

That way you don't get the documentation you're reading right now in your new
project.

Lastly, create a Git repository for your new project, and commit everything::

    $ git init
    Initialized empty Git repository in /home/rdegges/Code/ex/woot/.git/
    $ git add .; git ci -m 'First commit using django-skel!'
    ...
