import asyncio
from tutti_client import TuttiClient

async def main():
    client = TuttiClient()
    await client.open('http://localhost:8080')
    await client.resource.sign_in(user_name='admin', password='admin')
    print(await client.resource.list_projects())

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
