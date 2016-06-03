Introduction
============

Some utilities to import a Plone 4 site to Plone 5

Inside the blueprints folder you will find some useful transmogrifier blueprints
to help with your migrations.

Inside the pipelines folder you will find a browser view and an example import.cfg
file with an example (working) importing pipeline.

Installation
------------

Before using this product, install `collective.jsonify`_ in your old Plone 4 site.
In short, you need to add it to your buildout and then add 3 External Methods
through the ZMI as explained in the `documentation`_.

Then, add this product to your buildout. Until new versions of three helper products are
released, you need to add them in their develop mode, modifying your buildout.cfg file
as follows::

    [buildout]
    extensions =
        ...
        mr.developer

    auto-checkout =
        ...
        ftw.blueprints
        ftw.inflator
        collective.jsonmigrator
        quintagroup.transmogrifier


    [sources]
    ...
    ftw.blueprints = git git@github.com:erral/ftw.blueprints
    ftw.inflator = git git@github.com:erral/ftw.inflator
    collective.jsonmigrator = git git@github.com:erral/collective.jsonmigrator branch=unified
    quintagroup.transmogrifier = git git@github.com:collective/quintagroup.transmogrifier branch=plone5

Then run your buildout.


Migration procedure
-------------------

Start your Plone instance and create a Plone site with the same id as the original
one in Plone 4.

Install cs.p5migrator, which will install its dependencies. Install also any other
product that you need to run your site, specially the ones that install content-types
that you will be importing from Plone 4, otherwise this product will not be able to
import these content-types.

If your site is multilingual, install also the Multilingual Support, select the
languages of your site and let Plone to create the Language Root Folders.


Run the transmogrifier pipeline
-------------------------------

When your Plone site is ready:

#. Open a new tab with the URL http://ploneurl/@@mr.migrator

#. Select there the **Import generic Plone 4 content** pipeline

#. Adjust in the **Catalogsource** tab the URL of the original Plone 4 site.

#. Adjust in the **Clean_path** tab the id of the Plone site ('codesyntax' in the provided example)

#. Hit run to run the import pipeline. Check your instance's log file to see the progress





.. _`collective.jsonify`: https://github.com/collective/collective.jsonify
.. _`documentation` : https://collectivejsonify.readthedocs.org/en/latest/#how-to-install-it
