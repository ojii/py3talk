import asyncio

from aiohttp import web


async def handler(request):
    num = request.GET.get('num')
    await asyncio.sleep(2 - int(num))
    response = 'Num: %s' % num
    return web.Response(body=response.encode('utf-8'))


def main():
    app = web.Application()
    app.router.add_route('GET', '/', handler)
    web.run_app(app, port=4788)


if __name__ == '__main__':
    main()
