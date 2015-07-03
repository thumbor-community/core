How to create your own extension?
=================================

The best way to understand how to do it is by example, you can check out Shortener_ (particularly the ``__init__.py`` file).

.. _Shortener: https://github.com/thumbor-community/shortener

What's an extension?
--------------------

An extension is a python module that will be integrated within thumbor, through Thumbor Community's core package.
This module may contain autoloaded thumbor's modules (such as Filters, Storages, ...), tornado handlers, or configuration values.

Define your extension
---------------------

You extension must be registered to Thumbor Community's core. To do so, you'll need create an extension instance as follows:

.. code-block:: python

    from tc_core import Extension, Extensions

    // Extension name (here `my_extension` must match your python module name)
    extension = Extension('my_extension')

    // ... configure your extension

    Extensions.register(extension)

So within this example we have a project containing a python module named ``my_extension`` which will be registered in the core.
To enable it, we will have to edit our Thumbor's configuration to add the newly registered extension to Thumbor:

.. code-block:: ini

    COMMUNITY_EXTENSIONS = [
        'my_extension'
    ]

Setup the extension
-------------------

You've registered your extension and it is now loaded, but what if you'd like to use some of Thumbor's mechanisms to interconnect a bit further?

Add config
~~~~~~~~~~

You can register new configuration options fairly easily as follows:

.. code-block:: python

    from derpconf.config import Config

    Config.define('MY_CONFIG_KEY', 'my_default_value',  'Description for my key.', 'Configuration section')

And voilà! It's done, you can now fill in this value in your config and retrieve it from the config object by calling it:

.. code-block:: python

    my_val = self.context.config.get('MY_CONFIG_KEY')

But this is given you have access to the context object... To do that, check out how to add modules in the section below.

Add modules
~~~~~~~~~~~

Modules are context-aware classes which will be instantiated upon receiving the request.

To register them:

.. code-block:: python

    from tc_core import Extension, Extensions

    extension = Extension('my_extension')

    extension.add_module(
        config_key='MY_MODULE',
        class_name='MyModuleClass'
    )

    Extensions.register(extension)

In the configuration:

.. code-block:: ini

    MY_MODULE = 'my_extension.my_module'

Given you have the following class:

.. code-block:: python

    # File my_extension/my_module.py

    class MyModuleClass(object):

        def __init__(self, context):
            self.context = context

This will instantiate the class named ``MyModuleClass`` within the python module ``my_extension.my_module`` by passing the context to the constructor if need be.

Add handlers
~~~~~~~~~~~~

You may also add tornado handlers that will allow you to create custom controllers to answer the request to thumbor.

.. code-block:: python

    from tc_core import Extension, Extensions
    from my_extension.handlers import MyHandler

    extension = Extension('my_extension')

    extension.add_handler(MyHandler.regex(), MyHandler)

    Extensions.register(extension)

Given you have the following handler:

.. code-block:: python

    # File my_extension/handlers/__init__.py

    from thumbor.handlers import ContextHandler

    class MyHandler(ContextHandler):

        @classmethod
        def regex(cls):
            return r'/my_handler/(?P<url>.+)'

        // ...
