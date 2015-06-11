Installing Thumbor Community Core
=================================

1. Install thumbor (see `Thumbor repository`_)
2. Clone this repository
3. If you've set a virtualenv up for thumbor, activate it.
4. Install the Thumbor Community Core:
::
    $ cd thumbor-community/core
    $ pip install .

5. Install the extensions you wish to load.
6. Register the extensions to load within Thumbor's configuration file:
::
    COMMUNITY_EXTENSIONS = [
        'my_extension',
        ...
    ]

7. Launch thumbor with the Thumbor Community custom application:
::
    $ thumbor --conf=my_configuration_file -a thumbor_community.app.App


.. _`Thumbor repository`: https://github.com/thumbor/thumbor
