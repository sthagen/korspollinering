"""Cross pollination (Swedish: korspollinering) of application data from editable files."""

# [[[fill git_describe()]]]
__version__ = '2023.10.29+parent.613add8d'
# [[[end]]] (checksum: 1c1a765024202dbf37ac10023dc415e2)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
