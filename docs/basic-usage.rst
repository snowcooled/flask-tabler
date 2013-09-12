Basic usage
===========

To get started, the first step is to import and load the extension::

    from flask import Flask
    from flask_bootstrap import Bootstrap

    def create_app():
      app = Flask(__name__)
      Bootstrap(app)

      return app

    # do something with app...

After loading, new templates are available to derive from in your templates.


Templates
---------
.. highlight:: jinja

Creating a new Bootstrap-based template is simple::

    {% extends "bootstrap/base.html" %}
    {% block title %}This is an example page{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-fixed-top">
      <!-- ... -->
    </div>
    {% endblock %}

    {% block content %}
      <h1>Hello, Bootstrap</h1>
    {% endblock %}

Everything you do in child templates is based on blocks. Some blocks (like
``title``, ``navbar`` or ``content``) are "convenience blocks". Strictly
speaking they would not be necessary, but are added to save typing effort.

A very powerful feature is `Jinja2's super()
<http://jinja.pocoo.org/docs/templates/#super-blocks>`_ function. This gives
you the option of amending blocks instead of replacing them.

Available blocks
~~~~~~~~~~~~~~~~

============ =========== =======
Block name   Outer Block Purpose
============ =========== =======
doc                      Outermost block.
html         doc         Contains the complete content of the ``<html>`` tag.
html_attribs doc         Attributes for the HTML tag.
head         doc         Contains the complete content of the ``<head>`` tag.
body         doc         Contains the complete content of the ``<body>`` tag.
body_attribs body        Attributes for the Body Tag.
**title**    head        Contains the complete content of the ``<title>`` tag.
**styles**   head        Contains all CSS style ``<link>`` tags inside head.
metas        head        Contains all ``<meta>`` tags inside head.
**navbar**   body        An empty block directly above *content*.
**content**  body        Convenience block inside the body. Put stuff here.
**scripts**  body        Contains all ``<script>`` tags at the end of the body.
============ =========== =======

Examples
~~~~~~~~

* Adding a custom CSS file::

    {% block styles %}
    {{super()}}
    <link rel="stylesheet"
          href="{{url_for('.static', filename='mystyle.css')}}>
    {% endblock %}

* Custom Javascript loaded *before* Bootstrap's javascript code::

    {% block scripts %}
    <script src="{{url_for('.static', filename='myscripts.js')}}"></script>
    {{super()}}
    {% endblock %}

* Adding a ``lang="en"`` attribute to the ``<html>``-tag::

    {% block html_attribs} lang="en"{% endblock %}

Static resources
----------------

The url-endpoint ``bootstrap.static`` is available for refering to Bootstrap
resources, but usually, this isn't needed. A bit better is using the
``bootstrap_find_resource`` template filter, which will take CDN settings into
account.

Note that this mechanism is slated for overhaul in future versions of
Flask-Bootstrap, so take this into account before investing heavily into it.


Macros
------

Flask-Bootstrap comes with macros to make your life easier. These need to be
imported like in this example::

  {% extends "bootstrap/base.html" %}
  {% import "bootstrap/wtf.html" as wtf %}

This would import the ``wtf.html`` macros with the name-prefix of ``wtf``
(these are discussed below at :ref:`forms`).


Fixes
~~~~~

Cross-browser fixes (specifically for Internet Explorer < 9) are usually
included, but not shipped with Flask-Bootstrap. You can download `html5shiv
<https://raw.github.com/aFarkas/html5shiv/master/dist/html5shiv.js>`_ and
`Respond.js <https://raw.github.com/scottjehl/Respond/master/respond.min.js>`_,
put them in your applications static folder and include them like in this
example::

  {% import "bootstrap/fixes.html" as fixes %}
  {% block head %}
    {{super()}}
    {{fixes.ie8()}}
  {% endblock %}

The macro expects these files to be inside the a folder called 'js' inside your
static folder. You can explicitly give different folder locations::

  {% block head %}
    {{super()}}
    {{fixes.ie8(base=url_for('.static', filename='js/ie8fixes/')}}
  {% endblock %}

Or even name them explicitly::

  {% block head %}
    {{super()}}
    {{fixes.ie8(html5shiv=url_for('.static', filename='ie/html5shiv.js',
                respond=url_for('.static', filename='respond.js'))}}
  {% endblock %}


Google Analytics
~~~~~~~~~~~~~~~~

`Google Analytics <http://www.google.com/analytics/>`_ support is also
available as an extension macro::

  {% import "bootstrap/google.html" as google %}

  {% block scripts %}
  {{super()}}
  {{google.analytics(account="YOUR ACCOUNT CODE")}}
  {% endblock %}

If you want the analytics account to be configurable from the outside, you can
use something like this instead::

  {{google.analytics(account=config['GOOGLE_ANALYTICS_ACCOUNT'])}}

This allows specifying the account as a Flask configuration value.

.. _forms:

Forms
~~~~~

The ``bootstrap/wtf.html`` template contains macros to help you output forms
quickly. Flask-WTF_ is not a dependency of Flask-Bootstrap, however, and must be
installed explicitly. The API of Flask-WTF_ has changed quite a bit over the
last few versions, Flask-Bootstrap is currently developed for Flask-WTF_ version
0.9.2.

The most basic way is using them as an aid to create a form by hand::

  <form class="form form-horizontal" method="post">
    {{ form.hidden_tag() }}
    {{ wtf.form_errors(form, "only") }}

    {{ wtf.horizontal_field(form.field1) }}
    {{ wtf.horizontal_field(form.field2) }}

    <div class="form-actions">
       <button name="action_save" type="submit" class="btn btn-primary">Save changes</button>
    </div>
  </form>

However, often you just want to get a form done quickly and have no need for
intense fine-tuning::

  {{ wtf.quick_form(form) }}

.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/