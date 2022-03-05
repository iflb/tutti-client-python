# Event Listeners (Receiving responses)

When event listeners are properly set for corresponding controller methods, their responses are handled and passed as an argument of the passed handler coroutines.
Set handler coroutines are called every time each response is received, regardless of requests are made in **send** or **call** mode.

## Base Class

```{eval-rst}
.. module:: tutti_client.listener
.. autoclass:: DuctEventListener
    :members: on
    :undoc-members:
```

## Tutti.works Resources

```{eval-rst}
.. autoclass:: ResourceEventListener
    :members:
    :show-inheritance:
```

## Amazon MTurk Resources

```{eval-rst}
.. autoclass:: MTurkEventListener
    :members:
    :undoc-members:
    :show-inheritance:
```
