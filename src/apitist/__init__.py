"""Apitist package"""
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # For Python < 3.8
    from importlib_metadata import version, PackageNotFoundError

from .constructor import (
    AttrsConverter,
    Converter,
    ConverterType,
    DataclassConverter,
    convclass,
    converter,
)
from .hooks import (
    PreparedRequestHook,
    PrepRequestDebugLoggingHook,
    PrepRequestInfoLoggingHook,
    RequestAttrsConverterHook,
    RequestConverterHook,
    RequestDataclassConverterHook,
    RequestDebugLoggingHook,
    RequestHook,
    RequestInfoLoggingHook,
    ResponseAttrsConverterHook,
    ResponseConverterHook,
    ResponseDataclassConverterHook,
    ResponseDebugLoggingHook,
    ResponseHook,
    ResponseInfoLoggingHook,
    request_converter_hook,
    response_converter_hook,
)
from .random import Randomer
from .requests import Session, SharedSession, session

__all__ = [
    "__version__",
    "dist_name",
    "AttrsConverter",
    "DataclassConverter",
    "convclass",
    "converter",
    "ConverterType",
    "Converter",
    "PreparedRequestHook",
    "PrepRequestDebugLoggingHook",
    "PrepRequestInfoLoggingHook",
    "RequestAttrsConverterHook",
    "RequestConverterHook",
    "RequestDataclassConverterHook",
    "RequestDebugLoggingHook",
    "RequestHook",
    "RequestInfoLoggingHook",
    "ResponseAttrsConverterHook",
    "ResponseConverterHook",
    "ResponseDataclassConverterHook",
    "ResponseDebugLoggingHook",
    "ResponseHook",
    "ResponseInfoLoggingHook",
    "Randomer",
    "session",
    "Session",
    "SharedSession",
    "request_converter_hook",
    "response_converter_hook",
]

try:
    dist_name = "apitist"
    __version__ = version(dist_name)
except PackageNotFoundError as e:
    __version__ = "unknown"
    print(e)
