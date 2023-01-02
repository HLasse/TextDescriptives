News and Changelog
---------------------------------

**v2.0.0 - 1st of January 2023**

- All components have been renamed to have the :code:`textdescriptives/` prefix. I.e. components should now be loaded with e.g. :code:`nlp.add_pipe("textdescriptives/descriptive_stats)`. :code:`textdescriptives/all` can be used to load all components at once.
- :code:`pos_stats` has been renamed to :code:`pos_proportions` for consistency.

**v1.1.0 - 21st of September, 2022**

- Added the new pipe; "quality". This pipe implements a series of metrics related to text quality, some of which were used by Rae et al. (2021) and Raffel et al. (2020) to filter large text corpora. See the documentation for examples.

**v1.0.7 - 4th May, 2022**

- Some minor fixes and bells and whistles.

**v1.0.5 - 4th October, 2021**

- POS proportions now use :code:`pos_` instead of :code:`tag_` by default. This behavior can be changed by setting `use_tag` to `False` when initialising the `pos_stats` module. 
