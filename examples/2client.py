import time

import requests

URL = 'http://localhost:4788'


def download(session, num):
    print(session.get(URL, params={'num': num}).text)


def run():
    with requests.session() as session:
        for num in range(2):
            download(session, num)


def main():
    start = time.time()
    run()
    print("Done after %.2f seconds" % (time.time() - start))


if __name__ == '__main__':
    main()
