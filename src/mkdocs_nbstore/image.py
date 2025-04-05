from __future__ import annotations

import shlex
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Self


class Image:
    alt: str
    src: str
    uri: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    mime: str = ""
    content: bytes | str = ""

    def __init__(self, alt: str, src: str, attrs: str) -> None:
        self.alt = alt
        self.src = self.uri = src
        self.identifier = ""
        self.classes = []
        self.attributes = {}

        for attr in shlex.split(attrs):
            if attr.startswith("#"):
                self.identifier = attr[1:]
            elif attr.startswith("."):
                self.classes.append(attr[1:])
            elif "=" in attr:
                key, value = attr.split("=", 1)
                self.attributes[key] = value

    def update(self, mime: str, content: bytes | str) -> Self:
        self.mime = mime
        self.content = content
        self.uri = f"{uuid.uuid4()}.{mime.split('/')[1]}"
        return self

    @property
    def markdown(self) -> str:
        attrs = [f"#{self.identifier}"] if self.identifier else []
        attrs.extend(f".{cls}" for cls in self.classes)
        attrs.extend(f"{k}={shlex.quote(v)}" for k, v in self.attributes.items())
        attr = f"{{{' '.join(attrs)}}}" if attrs else ""
        return f"![{self.alt}]({self.uri}){attr}"
