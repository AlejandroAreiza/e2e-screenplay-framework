from typing import Any

from config.endpoints import Endpoints
from screenplay.actions.api import Get
from screenplay.actor import Actor
from screenplay.interfaces import Question


class TheBalance(Question):
    def __str__(self) -> str:
        return "the balance in the API"

    def answered_by(self, actor: Actor) -> Any:
        response = actor.attempts_to(Get.resource(Endpoints.BALANCE))
        response.raise_for_status()
        return response.json()
