"""Cross pollination (Swedish: korspollinering) of application data from editable files."""

# [[[fill git_describe()]]]
__version__ = '2023.4.20+parent.61756ddb'
# [[[end]]] (checksum: 0c1d3b246b02abf58c0523160a0ac08a)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
