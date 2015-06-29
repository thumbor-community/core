# Thumbor Community / Core

[![CircleCI](https://circleci.com/gh/thumbor-community/core.png)](https://circleci.com/gh/thumbor-community/core)

This is the main package of the Thumbor Community. This will handle the loading of custom extensions to [Thumbor](https://github.com/thumbor/thumbor).

Please note that this is still in beta stage for now.


## Quick setup

1. Install thumbor (see https://github.com/thumbor/thumbor)
2. Clone this repository
3. If you've set a virtualenv up for thumbor, activate it.
4. Install the Thumbor Community Core:
```bash
$ cd thumbor-community/core
$ pip install .
```
5. Install the extensions you wish to load.
6. Register the extensions to load within Thumbor's configuration file:
```ini
COMMUNITY_EXTENSIONS = [
    'my_extension',
    ...
]
```
7. Launch thumbor with the Thumbor Community custom application:
```bash
$ thumbor --conf=my_configuration_file -a tc_core.app.App
```

## Documentation

Documentation is ongoing. You may see it at [Read the Docs](http://thumbor-community-core.readthedocs.org/en/latest/). Feel free to contribute to improve it!
