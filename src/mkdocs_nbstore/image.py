from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Self


@dataclass
class Image:
    alt: str
    src: str
    identifier: str
    attr: str
    mime: str = ""
    content: bytes | str = ""
    uri: str = ""

    def update(self, mime: str, content: bytes | str) -> Self:
        self.mime = mime
        self.content = content
        self.uri = f"{uuid.uuid4()}.{mime.split('/')[1]}"
        return self

    @property
    def markdown(self) -> str:
        src = self.uri or self.src
        return f"![{self.alt}]({src}){{#{self.identifier}{self.attr}}}"

    def __contains__(self, attr: str) -> bool:
        return attr in self.attr.split(" ")

    def remove(self, attr: str) -> None:
        self.attr = " ".join(x for x in self.attr.split(" ") if x != attr)
