from django.db import models


class Presenter:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = 'Presenter'


class Listener:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = 'Listener'
