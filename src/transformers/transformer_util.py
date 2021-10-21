import importlib

from src.exceptions.usi_exceptions import BadInput
from src.transformers.transformer import StreamTransformer


def get_transformer(cls_path: str) -> StreamTransformer:
    module_name, class_name = cls_path.rsplit(".", 1)
    stream_transformer = getattr(importlib.import_module(module_name), class_name)

    if not issubclass(stream_transformer, StreamTransformer):
        raise BadInput(f'{cls_path} is not a subclass of StreamTransformer')

    return stream_transformer()
