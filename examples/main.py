import asyncio
from tutti_client import TuttiDuct

import logging
logger = logging.getLogger(__name__)

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
        if is_error:
            # handle error here

            '''
            data = {
                Status: "Error",
                Reason: str,
                Timestamp: {
                  "Requested": int,
                  "Responded": int
                }
            }
            '''
        else:
            print(data)
            # do anything here

            '''
            data = {
              Contents: {
                 ...
              },
              Timestamp: {
                "Requested": int,
                "Responded": int
              }
            }
            '''


if __name__=="__main__":
    pg = MyPlayground()
    asyncio.run(pg.main())
