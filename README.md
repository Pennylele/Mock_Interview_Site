# Errors and Solutions

* `Exception Value:	no such table: django_session`
   
   -> `python3 manage.py migrate`

* `django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.`
  
  -> change `SECRET_KEY = os.environ.get('mock_secrete_key')` in the settings.py to a random value 
  ex: `SECRET_KEY = 'askdkajshdkjahd'`

