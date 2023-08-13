# What's New

## 0.4.0

Misc updating and tidying.

- Stopped testing on python 3.7. Test on python 3.8 through 3.11
- Move from setup.cfg to pyproject.toml
- Update parsing to treat responses as xml rather than html: adds new dependency on lxml
- The legislative website now treats a member's district as
  as a string rather than an int.
  Returned dictionaries from functions such as get_active_committe_members,
  get_sponsors, etc. the district values are now strings as well.
- Input arguments were in readable "snake_case" but output dictionaries
  were formatted with "lower()" -- changed those to snake case to be consistent.
- Removed ugly homegrown documentation theme and swapped in pydata_sphinx_theme
- Update docs build for changes on readthedocs.


## 0.3.0

* Thanks to [ryansloan](https://github.com/ryansloan) for catching a bug
legislation.get_roll_calls now unpacks the returned votes correctly.

## 0.2.0

* Created a release history page in the docs dir
* Fixed a bug where get_legislation returned the string "true" or "false" instead of a boolean for the "active" return
  parameter
* Added mypy to the maintenance stack
