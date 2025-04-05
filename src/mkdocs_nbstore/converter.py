from __future__ import annotations

from typing import TYPE_CHECKING

from .logger import logger
from .markdown import iter_images

if TYPE_CHECKING:
    from collections.abc import Iterator

    from nbstore.store import Store

    from .image import Image


def convert(markdown: str, store: Store) -> Iterator[str | Image]:
    for image in iter_images(markdown):
        if isinstance(image, str):
            yield image
        else:
            try:
                yield from convert_image(image, store)
            except ValueError:
                logger.warning(f"Could not convert {image.src}#{image.identifier}")
                yield image.markdown


def convert_image(image: Image, store: Store) -> Iterator[str | Image]:
    if "source" in image.classes:
        image.classes.remove("source")
        if source := get_source(image, store):
            yield source

    if mime_content := store.get_mime_content(image.src, image.identifier):
        yield image.update(*mime_content)


def get_source(image: Image, store: Store) -> str:
    if source := store.get_source(image.src, image.identifier):
        language = store.get_language(image.src)
        return f"```{language}\n{source}\n```\n\n"

    return ""
