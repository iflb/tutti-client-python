# Basic Usage

A simplest tutorial of using Tutti.works client API:

```python
import asyncio
from tutti_client import TuttiClient

HOST = 'http://localhost:8080'
USERNAME = 'myusername'
PASSWORD = 'mypassword'

async def main():
    client = TuttiClient()
    await client.open(HOST)
    await client.resource.sign_in(user_name=USERNAME, password=PASSWORD)
    projects = await client.resource.list_projects()
    print(projects)   # prints list of existing projects

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

:::{note}
Note that since Tutti Client API is built upon [DUCTS](https://github.com/iflb/ducts) web server framework, which is based on asynchronous WebSocket connection, therefore `async/await` is needed in most cases of calling methods.
:::

:::{note}
Remember to sign in (by calling `await client.resource.sign_in()`) before calling any controller methods, otherwise it fails.
:::
