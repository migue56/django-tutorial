====
Polls
====


Polls is a simple app to docut Web-based polls.
For each question, visitors can choose betwwen a fixed numer od answer.

Detailed documentacion is in the "docs" direcotry.


Quick Start
--------------

1. Add "pools" to your INSTALLED_APP settigns loke this::

  INSTALLED_APPS = [
     ...
       'polls'
  ]

2. Include the polls URL conf on your projecto urls.py

  path('polls/', include('polls.urls'))

3. Run `python manage.py migrate` to create the polls models


4. Start the development server and visit  http://127.0.0.1:8000/admin/  to create a polls(you'll need the Admin app enabled ).


5. Visit http://127.0.0.1:8000/polls/ to participate in the polls.
