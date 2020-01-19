import asyncio

from aiohttp.client import ClientSession, ClientTimeout, ClientError

from core.models import ACTIVE, BROKEN, LIVENESS_CHECK_FAILED


async def _check_url(cs, url):
    try:
        async with cs.get(url) as resp:
            if 200 <= resp.status < 400:
                return url, ACTIVE
            else:
                return url, BROKEN

    except ClientError:
        return url, LIVENESS_CHECK_FAILED


async def _check_urls(urls):
    cs = ClientSession(timeout=ClientTimeout(5))

    result = await asyncio.gather(
        *map(
            lambda x: _check_url(cs, x),
            urls
        )
    )

    await cs.close()
    return result


def check_urls(urls):
    loop = asyncio.new_event_loop()

    result = loop.run_until_complete(_check_urls(urls))

    loop.close()

    return result

