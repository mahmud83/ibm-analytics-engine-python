********
Examples
********

This section shows example code snippets for working with this library.

=============
Prerequisites
=============

**API Key**

The lifecycle of an IBM Analytics Engine cluster is controlled through Cloud Foundry (e.g. create, delete, status operations).  This python library requires an API key to work with the Cloud Foundry APIs.  For more information on IBM Cloud API Keys including how to create and download an API Key, see https://console.bluemix.net/docs/iam/userid_keys.html#userapikey

**Installation**

Ensure you have installed this library.

Install with:

.. code-block:: python

   pip install --upgrade git+https://github.com/snowch/ibm-analytics-engine-python@master

=======
Logging
=======

Log level is controlled with the environment variable ``LOG_LEVEL``.  

You may set it programmatically in your code:

.. code-block:: python

   os.environ["LOG_LEVEL"] = "DEBUG"

Typical valid values are ERROR, WARNING, INFO, DEBUG.  For a full list of values, see: https://docs.python.org/3/library/logging.html#logging-levels

=======================
Finding your space guid
=======================

Many operations in this library require you to specify a space guid.  You can list the spaces guids for your account using this example:

.. literalinclude:: example_scripts/list_orgs_and_spaces.py

Alternatively, if you know your organisation name and space name, you can use the following:

.. literalinclude:: example_scripts/find_space_guid.py

==============
Create Cluster
==============

This example shows how to create a basic spark cluster.

.. literalinclude:: example_scripts/create_cluster.py

The above example creates a LITE cluster.  See :ref:`IBMServicePlanGuid` for the available service plan guids.

==============
Delete Cluster
==============

.. literalinclude:: example_scripts/delete_cluster.py

==============================
Get or Create Credentials
==============================

.. literalinclude:: example_scripts/cluster_credentials.py

To save the returned data to disk, you can do something like:

.. code-block:: python

   with open('./vcap.json', 'w') as vcap_file:
       vcap_file.write(vcap_formatted)

==================
Get Cluster Status
==================

To return the Cloud Foundry status:

.. literalinclude:: example_scripts/cluster_status.py

Alternative option to poll for the Cloud Foundry status until it is 'succeeded' or 'failed':

.. literalinclude:: example_scripts/cluster_status_poll.py

To return the Data Platform API status:

.. literalinclude:: example_scripts/cluster_dp_api_status.py

=============
List Clusters
=============

.. literalinclude:: example_scripts/clusters.py

========================
Jupyter Notebook Gateway
========================

This is an example script for running a docker notebook that connects to the cluster using the JNBG protocol and the credentials in your vcap.json file.

.. literalinclude:: example_scripts/run_docker_notebook.sh

