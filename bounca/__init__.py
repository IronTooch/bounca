from django.utils.version import get_version

# version types: final, 'alpha', 'beta', 'rc'

VERSION = (0, 1, 1, 'final', 0)

__version__ = get_version(VERSION)
