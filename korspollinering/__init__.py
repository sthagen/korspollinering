"""Cross pollination (Swedish: korspollinering) of application data from editable files."""

# [[[fill git_describe()]]]
__version__ = '2023.4.20+parent.251ed4ec'
# [[[end]]] (checksum: 7f4f1fc8ebb72f45d3f92f6a1088f480)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
