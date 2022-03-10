import asyncio
from datetime import datetime
from tutti_client import TuttiClient

project_name = 'MyProject'
last_watch_id = '1646886426294-0'

async def on_response_for_project(data):
    print(data)

async def main():
    client = TuttiClient()
    await client.open('http://localhost:8080')
    await client.resource.sign_in(user_name='admin', password='admin')
    client.resource.on('watch_responses_for_project', on_response_for_project)
    await client.resource.watch_responses_for_project.send(
        project_name = project_name,
        last_watch_id = last_watch_id,
        exclusive = False,
    )

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
