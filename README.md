django-jquery-qtip
==================

![Version Badge](https://pypip.in/v/django-jquery-qtip/badge.png)  
![Downloads Badge](https://pypip.in/d/django-jquery-qtip/badge.png)  
![Wheel Status Badge](https://pypip.in/wheel/django-jquery-qtip/badge.png)  
![License Badge](https://pypip.in/license/django-jquery-qtip/badge.png)  

[jQuery qTip](http://qtip2.com) packaged in a django app to speed up new applications and deployment.

> Note that this does not include jQuery or jQuery UI itself, use a package such as [django-jquery](https://pypi.python.org/pypi/django-jquery/) or [django-jquery-ui](https://pypi.python.org/pypi/django-jquery-ui/) to do so.

Installation
------------

Install using `pip`:

    pip install django-jquery-qtip
    
Add to `jquery_qtip` to your `INSTALLED_APPS` in `settings.py`:

    INSTALLED_APPS = (
        ...
        'jquery_qtip',
        ...
    )
    
Run `collectstatic` to bring in the qTip static files.
    
Usage
-----

In your template, load Django's `static` template tag library:

    {% load static %}
    
Then use the `static` template tag to load the qTip files:

    <script type='text/javascript' src='{% static 'js/jquery.qtip.js' %}'></script>
    <link rel='stylesheet' type='text/css' href='{% static 'css/jquery.qtip.css' %}' />
