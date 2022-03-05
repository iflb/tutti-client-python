```{eval-rst}
.. _communication:
```
# Communication with Server

Tutti.works client API provides two ways of communication: **send** and **call** modes.

## Send mode

As WebSocket-based communication, each request and response occurs asynchronously, meaning requests are "sent" without waiting for response as a return value and responses are received in corresponding event listeners.

For instance:

```
async def on_list_projects(data):
    print(data)   # prints list of existing projects
    
async def main():
    client.resource.on('list_projects', on_list_projects)   # set event listener
    await client.resource.list_projects.send()     # send request
```

### Making requests

For send mode communication, controller methods are executed with `called=False`:

```
await client.resource.list_projects(called=False)
```

OR via `.send()` syntax sugar:

```
await client.resource.list_projects.send()
```

### Receiving responses

Before sending requests, set a corresponding event listener with `.on()` method (specify the controller method name as a string):

```
client.resource.on('list_projects', some_handler_function)
```

and an (async) handler function:

```
async def some_handler_function(data):
    print(data)
```

## Call mode (default)

One-liner request & response is also supported.
With call mode, response for each request is received as a return value:

```
projects = await client.resource.list_projects()
```

or in explicit ways (but not necessary):

```
projects = await client.resource.list_projects(called=True)
projects = await client.resource.list_projects.call()
```
