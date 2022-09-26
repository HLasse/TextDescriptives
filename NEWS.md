# News

## v1.1.0 - 21st of September, 2022
- Added the new pipe; "quality". This pipe implements a series of metrics related to text quality, some of which were used by Rae et al. (2021) and Raffel et al. (2020) to filter large text corpora. See the documentation for examples.

## v1.0.7 - 4th May, 2022
- Some minor fixes and bells and whistles.

## v1.0.5 - 4th October, 2021
- POS proportions now use `pos_` instead of `tag_` by default. This behavior can be changed by setting `use_tag` to `False` when initialising the `pos_stats` module. 