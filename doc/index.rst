========================================================
qirest: Quantitative Imaging Profile REST server
========================================================

********
Synopsis
********
The Quantitative Imaging Profile REST server serves data for the
Quantitative Imaging Profile (QiPr_) web application.

:API: https://qiprofile-rest.readthedocs.org/en/latest/api/index.html

:Git: https://github.com/ohsu-qin/qirest


************
Installation
************
1. Install the Python_ pip_ package on your workstation, if necessary.

2. Install MongoDB_, if necessary. Use the default WiredTiger storage engine.

3. Install ``qirest``::

       pip install qirest


*****
Usage
*****

1. Start MongoDB::

       mongod&

2. Run the following command to display the REST server commands and options::

       qirest --help

3. Start the REST server::

       qirest

   Alternatively, the server can be started in development mode with the
   ``--development`` option::

        qirest --development



4. The data model is described in the `REST client`_ documentation.
   The REST API is described in the `Eve Features`_ documentation. For
   example, the following command returns the JSON list of all subjects
   for a server running on the local machine::

       curl -i http://localhost:5000/subject


***********
Development
***********

The project is cloned, tested, documented and released as described in
the `qipipe`_ documentation Development section [#rtd_requirements]_.

A sample database can be created by running the following command in
the local ``qirest`` project directory::

    ./qirest/test/helpers/seed.py

---------

.. rubric:: Footnotes

.. [#rtd_requirements]
  Note that the Read The Docs `qirest` project requirements file must be
    set to `requirements_read_the_docs.txt`. This alternative requirements
    file is a subset of the `requirements.txt` suitable only for documentation
    generation. Specifically, the alternative file works around the following
    problem:

    * A Read The Docs build with `requirements.txt` fails on pymongo because
    of an over-zealous Eve dependency constraint.

.. container:: copyright

.. Targets:

.. _Eve Features: http://python-eve.org/features.html

.. _Knight Cancer Institute: http://www.ohsu.edu/xd/health/services/cancer

.. _MongoDB: https://docs.mongodb.org/manual/

.. _nose: https://nose.readthedocs.org/en/latest/

.. _pip: https://pypi.python.org/pypi/pip

.. _Python: http://www.python.org

.. _qipipe: http://qipipe.readthedocs.org/en/latest/

.. _REST client: http://qirest-client.readthedocs.org/en/latest/

.. _QiPr: https://github.com/ohsu-qin/qiprofile
