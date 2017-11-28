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
