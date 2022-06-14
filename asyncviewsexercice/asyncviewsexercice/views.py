import asyncio
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)


async def teste():
    for l in range(100, 106):
        await asyncio.sleep(1)
        print(l)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    loop.create_task(teste())

    return HttpResponse('Non blocking HTTP request')
