""" About textdescriptives, version number is specified in the setup.cfg
file."""

# if python >= 3.8, use importlib.metadata otherwise use pkg_resources
try:
    from importlib.metadata import version

    __version__ = version("textdescriptives")
except ImportError:
    from pkg_resources import get_distribution  # type: ignore

    __version__ = get_distribution("textdescriptives").version

__title__ = "textdescriptives"
__download_url__ = "https://github.com/HLasse/textdescriptives"
