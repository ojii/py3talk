import time

from flask import Flask, request


def handler():
    num = request.args.get('num')
    time.sleep(2 - int(num))
    response = 'Num: %s' % num
    return response.encode('utf-8')


def main():
    app = Flask(__name__)
    app.route('/')(handler)
    app.run(port=4788, debug=True)


if __name__ == '__main__':
    main()
