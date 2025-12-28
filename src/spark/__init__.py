"""Stats Spark core package."""

__version__ = "1.0.0"
__author__ = "Mark Hazleton"

from spark.cache import APICache
from spark.config import SparkConfig

__all__ = ["APICache", "SparkConfig", "__version__", "__author__"]
