from __future__ import annotations

from http import HTTPMethod
from typing import Any

import requests

from screenplay.abilities import CallAnApi
from screenplay.actor import Actor
from screenplay.interfaces import Performable


class Get(Performable):
    def __init__(self, path: str) -> None:
        self.path = path
        self.body: dict[str, Any] | None = None

    @classmethod
    def resource(cls, path: str) -> Get:
        return cls(path)

    def with_body(self, body: dict[str, Any]) -> Get:
        self.body = body
        return self

    def __str__(self) -> str:
        return f"Get {self.path}"

    def perform(self, actor: Actor) -> requests.Response:
        return actor.ability_to(CallAnApi).send(HTTPMethod.GET, self.path, json=self.body)
