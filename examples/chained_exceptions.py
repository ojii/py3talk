import requests


def main():
    try:
        return requests.get('http://example.invalid')
    except:
        with open('/does/not/exist', 'w') as fobj:
            fobj.write('An Error Happened!')


if __name__ == '__main__':
    main()