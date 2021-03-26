import functools

from ducts_client import Duct
from .controllers import ResourceController, MTurkController
from .event_listeners import ResourceEventListener, MTurkEventListener

class TuttiDuct(Duct):
    def __init__(self):
        super().__init__()
        self.onopen_handlers = [];
        self.controllers = {
            "resource": ResourceController(self),
            "mturk": MTurkController(self)
        }
        self.event_listeners = {
            "resource": ResourceEventListener(),
            "mturk": MTurkEventListener()
        }

    def add_onopen_handler(self, handler_coro):
        self.onopen_handlers.append(handler_coro)

    async def _onopen(self, event):
        await super()._onopen(event)

        self.setup_handlers()
        for handler in self.onopen_handlers:
            await handler()

    def setup_handlers(self):
        self.set_event_handler( self.EVENT["LIST_PROJECTS"], functools.partial(self.handle_for, "resource", "list_projects"))

    async def handle_for(self, _type, event_name, rid, eid, data):
        await self._handle(_type, event_name, data)

    async def _handle(self, _type, name, data):
        if data["Status"]=="Success":
            for func in self.event_listeners[_type].get_handlers(name):  await func(data["Contents"], is_error=False)
        else:
            for func in self.event_listeners[_type].get_handlers(name):  await func(data, is_error=True)
