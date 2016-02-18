import asyncio
import time

import aiohttp


URL = 'http://localhost:4788'


async def download(session, num):
    async with session.get(URL, params={'num': num}) as response:
            assert response.status == 200
            content = await response.read()
            print(content.decode('utf-8'))


async def run():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for num in range(2):
            task = asyncio.ensure_future(download(session, num))
            tasks.append(task)
        await asyncio.wait(tasks)


def main():
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    print("Done after %.2f seconds" % (time.time() - start))


if __name__ == '__main__':
    main()