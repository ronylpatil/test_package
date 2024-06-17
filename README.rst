
.. image:: https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg
   :align: center
   :height: 200
   :alt: logo  


.. image:: https://img.shields.io/pypi/v/dummypackage12624.svg
   :target: https://pypi.org/project/dummypackage12624/

.. image:: https://img.shields.io/pypi/pyversions/dummypackage12624.svg
   :target: https://pypi.org/project/dummypackage12624/

.. image:: https://github.com/ronylpatil/dummypackage12624/actions/workflows/ci_pipeline.yaml/badge.svg
   :target: https://github.com/ronylpatil/dummypackage12624/actions?query=workflow%3Atest

.. image:: https://github.com/ronylpatil/dummypackage12624/actions/workflows/cd_pipeline.yaml/badge.svg
   :target: https://github.com/ronylpatil/dummypackage12624/actions?query=workflow%3Atest


The ``dummypackage12624`` package make it easy to perform whatsApp group chat analysis using python.

A simple code example:

.. code-block:: python

       # import chatInsights class
       from chatInsights import ChatInsights
       
       # create obj of ChatInsights class
       obj = ChatInsights(r'E:/chat.txt')
       obj.active_users()
       obj.active_year()
       obj.active_month()
       obj.active_day()
       obj.word_cloud()


Output:
.. list-table::
   :widths: 33 33 33
   :header-rows: 0

   * - .. image:: doc/en/active_users.png
         :width: 330px
         :height: 190px
     - .. image:: doc/en/active_year.png
         :width: 330px
         :height: 190px
     - .. image:: doc/en/active_month.png
         :width: 330px
         :height: 190px
   * - .. image:: doc/en/active_day.png
         :width: 330px
         :height: 190px
     - .. image:: doc/en/wordcloud.png
         :width: 330px
         :height: 190px
     - 




Features
--------
- User activity stats
- Weekly message stats
- Monthly message stats
- Yearly message stats
- Word Cloud


Documentation
-------------

Updated soon.


Bugs/Requests
-------------

Please use the `GitHub issue tracker <https://github.com/ronylpatil/dummypackage12624/issues>`_ to submit bugs or request features.


Changelog
---------

Consult the `Changelog <add changelog link here>`__ page for fixes and enhancements of each version.


License
-------

Distributed under the terms of the `MIT`_ license.


.. _`MIT`: https://github.com/ronylpatil/dummypackage12624/LICENSE
