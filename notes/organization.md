Organization
============

- **package:**
  - a module which can contain other modules
  - generally a directory, whereas a standard module is a file
  - responds to the `__path__` property
  - packages must be in `sys.path`
    - packages can be manually added to path for module discoverability
      - `sys.path.append('packagename')`
      - `export PYTHONPATH=packagename`
  - the existence of `__init__.py` defines a package
    - executed when the package is imported
    - `mypackage.__file__ => './mypackage/__init__.py`
  - use `__init__.py` to hoist Classnames into top level of package

- **imports**
  - _absolute_ (preferred)
    - use a full path to the module
    - `from reader.reader import Reader`
  - _relative_
    - use a relative path to modules _in the same package_
    - `from .reader import Reader`
    - `from . import Reader => must qualify via reader.Reader`
    - `from ..other import Other`

- **__all__**
  - list of attribute names imported via `from module import *`
  - can limit what names are exposed in modules (via `__init__.py`)

- **namespace packages**
  - packages split across several directories (PEP420)
  - no `__init__.py` (avoids compex initialization ordering issues)
  - importing:
    1. python scans all entries in `sys.path`
    2. if a matching directory with `__init__.py` is found, a normal package is loaded
    3. if a matching module/file is found, then it's loaded
    4. Else, all matching directories in `sys.path` are considered part of the namespace package

- **executable directories**
  - specify a main entry point for python execution in the directory
  - requires `__main__.py`
    - can be used as a simple driver for the package
  - can be turned into an **executable zip files**

- **modules are singletons**
  - only executed once, when _first_ imported
  - module initialization order is well defined

- **general purpose project structure**

    ```
    projectname/
    |-- __main__.py
    |-- projectname/
    |   |-- __init__.py
    |   |-- source_mod.py
    |   |-- subpackage1/
    |   |   |-- __init__.py
    |   |   |-- __more_source.py
    |   |-- test/
    |       |-- __init__.py
    |       |-- test_mod.py
    |-- setup.py
    ```

