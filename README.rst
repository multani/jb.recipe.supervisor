Introduction
============

This recipe installs and configure `supervisor`_ according to a configuration
file.

How to use?
===========

You can use by configuration your ``buildout.cfg`` configuration file like
this::

    [buildout]
    parts = supervisor

    [supervisor]
    recipe = jb.recipe.supervisor
    configuration-file = supervisor-sample.conf

You can download a sample configuration file at
https://github.com/multani/jb.recipe.supervisor/raw/master/supervisord-sample.conf

Running Buildout with this configuration file will generate:

* a `supervisor`_ configuration file using the template from the
  ``configuration-file`` settings as shown above;
* ``bin/supervisord``, which is a script to run the `supervisor`_ daemon,
  according to the content of the configuration file above ;
* ``bin/supervisorctl``, which is a script to run the `supervisor`_ client,
  according to the content of the configuration file above.

Additional settings
===================

By default, the configuration file will end in
``parts/PART_NAME/supervisord.conf``, but you can change it by setting the
``output-dir`` in your configuration file::

    [buildout]
    parts = supervisor

    [supervisor]
    recipe = jb.recipe.supervisor
    configuration-file = supervisor-sample.conf
    output-dir = /foo/bar
    # The configuration will end in /foo/bar/supervisord.conf

The configuration file is processed by `collective.recipe.template`_. It means
you can use Buildout variables inside your template, such as
``${buildout:parts-directory}``, ``${_buildout_section_name_}``, or any valid
settings. See
http://pypi.python.org/pypi/zc.buildout/1.5.2#variable-substitutions for more
informations.


Related projects
================

`collective.recipe.supervisor`_ is a similar project, but with a different
approach. I liked to be able to configure `supervisor`_ from Buildout but I
found the syntax used by `collective.recipe.supervisor`_ to be confusing and
really ad-hoc.


.. _supervisor: http://supervisord.org
.. _collective.recipe.template: http://pypi.python.org/pypi/collective.recipe.template
.. _collective.recipe.supervisor: http://pypi.python.org/pypi/collective.recipe.supervisor


