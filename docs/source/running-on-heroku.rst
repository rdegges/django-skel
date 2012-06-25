Running on Heroku
=================

Normally, deploying a Django site would make you want to flip your desk:

.. image:: _static/flip.png

Luckily for us, `Heroku <http://www.heroku.com/>`_ has made the process a
complete joy! If you're aren't familiar with Heroku--they are the **best**
web host, and you will love them if you don't already.

``django-skel`` ships with a production ready Heroku configuration module, and
this section will walk you through creating your Heroku app, and getting your
site running in production.

While this section is quite long, don't be intimidated! It's only long because
I'm explaining everything along the way--the reality of it is that deploying
your site this way really only consists of a couple commands.

If you'd like to read some official documentation on the topic, check out
`Heroku's Django documentation <https://devcenter.heroku.com/articles/django>`_.
