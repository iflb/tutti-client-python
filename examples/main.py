import asyncio
from tutti_client import TuttiDuct

class MyPlayground:
    def __init__(self):
        self.tutti = TuttiDuct()

    async def catchall_event_handler(self, rid, eid, data):
        print(eid, data) 

    async def on_open(self):
        await self.tutti.controllers["resource"].list_projects()

    async def main(self):
        self.tutti.add_onopen_handler(self.on_open)
        self.tutti.event_listeners["resource"].on("list_projects", self.on_list_projects)

        await self.tutti.open("http://localhost/ducts/wsd")

    async def on_list_projects(self, data, is_error):
        print(is_error, data)

if __name__=="__main__":
    pg = MyPlayground()
    asyncio.run(pg.main())
