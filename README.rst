ABC University
========

University social network


The project has Two basic apps:

* Articles (A collaborative blog)
* Question & Answers (A Stack Overflow-like platform)
* Massaging app Between Students
* Notification System To Help Student Being Active. and Also this feature shall be
  link to the Mobile App

Technology Stack
----------------

* Python_ 3.6.x / 3.7.x
* `Django Web Framework`_ 1.11.x / 2.0.x
* PostgreSQL_
* `Redis 3.2`_
* Daphne_
* Caddy_
* Docker_
* docker-compose_
* WhiteNoise_
* `Twitter Bootstrap 4`_
* `jQuery 3`_
* Django-channels_ (for WebSockets)
* Sentry_
* Mailgun_
* Cookiecutter_

.. _Python: https://www.python.org/
.. _`Django Web Framework`: https://www.djangoproject.com/
.. _PostgreSQL: https://www.postgresql.org/
.. _`Redis 3.2`: https://redis.io/documentation
.. _Daphne: https://github.com/django/daphne/
.. _Caddy: https://caddyserver.com/docs
.. _Docker: https://docs.docker.com/
.. _docker-compose: https://docs.docker.com/compose/
.. _WhiteNoise: http://whitenoise.evans.io/en/stable/
.. _`Twitter Bootstrap 4`: https://getbootstrap.com/docs/4.0/getting-started/introduction/
.. _`jQuery 3`: https://api.jquery.com/
.. _Django-channels: https://channels.readthedocs.io/en/latest/
.. _Sentry: https://docs.sentry.io/
.. _Mailgun: https://www.mailgun.com/
.. _Cookiecutter: http://cookiecutter-django.readthedocs.io/en/latest/index.html

Basic Commands
--------------
how To Run
^^^^^^^^^^
python manage.py migrate 

&&

python manage.py runserver 

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
