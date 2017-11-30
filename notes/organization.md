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
