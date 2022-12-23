"""About textdescriptives, version number is specified in the setup.cfg
file."""

# if python >= 3.8, use importlib.metadata otherwise use pkg_resources
try:
    from importlib.metadata import version

    __version__ = version(__name__)
except ImportError:
    from pkg_resources import get_distribution  # type: ignore

    __version__ = get_distribution(__name__).version

__title__ = "textdescriptives"
__download_url__ = "https://github.com/HLasse/textdescriptives"
