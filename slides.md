name: inverse
layout: true
class: center, middle, inverse

---

# Why I ♥ Python 3

???

Python 3.0 - December 3, 2008

Python 3.1 - June 27, 2009

Python 3.2 - February 20, 2011

Python 3.3 - September 29, 2012

Python 3.4 - March 16, 2014

Python 3.5 - September 13, 2015

---

class: center, middle

# NO

--

# MORE

--

# UnicodeDecodeError

---

class: center, middle

End of presentation.

--

Not really

---

## Fixed Stuff

---
layout: false
.left-column[
  ## Fixed Stuff
]

.right-column[
  ### Text/Binary Data  
  
  #### Python 2
    
  * `unicode` for text
  * `str` for text *and bytes*
  * `bytes` for bytes
    

  #### Python 3
    
  * `str` for text
  * `bytes` for bytes
]

---
.left-column[
  ## Fixed Stuff
]

.right-column[
### Print is a function now
#### Python 2

```python
print 'foo',
print >>open('somefile', 'w'), 'bar'
def printer(s):
    print s
my_awesome_function(log=printer)
```
  
#### Python 3

```python
print('foo', end='')
print('bar', file=open('somefile', 'w'))
my_awesome_function(log=print)
```
]

---
.left-column[
  ## Fixed Stuff
]

.right-column[
### Built-in Virtual Environments
#### Python 2

```sh
wget https://bootstrap.pypa.io/get-pip.py
sudo python2 get-pip.py
sudo pip install virtualenv
virtualenv -p python2 env
```
  
#### Python 3

```sh
python3 -m venv env
```
]

---
.left-column[
  ## Fixed Stuff
]

.right-column[
### `True` and `False` are now reserved Words
#### Python 2

```python
# valid python!
True, False = False, True 
```
  
#### Python 3

```python
# SyntaxError: can't assign to keyword
True, False = False, True
```
]

---
.left-column[
  ## Fixed Stuff
]

.right-column[
### Can no longer order arbitrary stuff
#### Python 2

```python
class Three: pass
sorted([1, 'two', Three()])
#[<__main__.Three instance at 0x1084a1560>, 1, 'two']
```
  
#### Python 3

```python
class Three: pass
sorted([1, 'two', Three()])
#TypeError: unorderable types: str() < int()
```
]

---
template: inverse

## Better Stuff

---
.left-column[
  ## Better Stuff
]

.right-column[
### `super` is now super
#### Python 2

```python
class Foo(object):
    def bar(self, baz):
        super(Foo, self).bar(baz)
```
  
#### Python 3

```python
class Foo:
    def bar(self, baz):
        super().bar(baz)
```
]

---
.left-column[
  ## Better Stuff
]

.right-column[
  ### Chained Exceptions
  #### Example Code
```python
def main():
    try:
        return requests.get('http://example.invalid')
    except:
        with open('/does/not/exist', 'w') as fobj:
            fobj.write('An Error Happened!')
  ```
]

---
.left-column[
  ## Better Stuff
]

.right-column[
  ### Chained Exceptions
  #### Python 2
```tiny-code
Traceback (most recent call last):
  File "examples/chained_exceptions.py", line 13, in <module>
    main()
  File "examples/chained_exceptions.py", line 8, in main
    with open('/does/not/exist', 'w') as fobj:
IOError: [Errno 2] No such file or directory: '/does/not/exist'
  ```
]

???

IOError: [Errno 2] No such file or directory: '/does/not/exist'

---
.left-column[
  ## Better Stuff
]

.right-column[
  ### Chained Exceptions
  #### Python 3
```tiny-code
Traceback (most recent call last):
  File "examples/chained_exceptions.py", line 13, in <module>
    main()
  File "examples/chained_exceptions.py", line 8, in main
    with open('/does/not/exist', 'w') as fobj:
IOError: [Errno 2] No such file or directory: '/does/not/exist'
(env) [jonasobrist ~/playground/py3talk]$ python3 examples/chained_exceptions.py 
Traceback (most recent call last):
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/connection.py", line 137, in _new_conn
    (self.host, self.port), self.timeout, **extra_kw)
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/util/connection.py", line 67, in create_connection
    for res in socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM):
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 732, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/connectionpool.py", line 559, in urlopen
    body=body, headers=headers)
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/connectionpool.py", line 353, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1083, in request
    self._send_request(method, url, body, headers)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1128, in _send_request
    self.endheaders(body)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1079, in endheaders
    self._send_output(message_body)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 911, in _send_output
    self.send(msg)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 854, in send
    self.connect()
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/connection.py", line 162, in connect
    conn = self._new_conn()
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/connection.py", line 146, in _new_conn
    self, "Failed to establish a new connection: %s" % e)
requests.packages.urllib3.exceptions.NewConnectionError: <requests.packages.urllib3.connection.HTTPConnection object at 0x10250b320>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/adapters.py", line 376, in send
    timeout=timeout
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/connectionpool.py", line 609, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/packages/urllib3/util/retry.py", line 273, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
requests.packages.urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='example.invalid', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x10250b320>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "examples/chained_exceptions.py", line 6, in main
    return requests.get('http://example.invalid')
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/api.py", line 67, in get
    return request('get', url, params=params, **kwargs)
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/api.py", line 53, in request
    return session.request(method=method, url=url, **kwargs)
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/sessions.py", line 468, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/sessions.py", line 576, in send
    r = adapter.send(request, **kwargs)
  File "/Users/jonasobrist/playground/py3talk/env/lib/python3.5/site-packages/requests/adapters.py", line 437, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='example.invalid', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x10250b320>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "examples/chained_exceptions.py", line 13, in <module>
    main()
  File "examples/chained_exceptions.py", line 8, in main
    with open('/does/not/exist', 'w') as fobj:
FileNotFoundError: [Errno 2] No such file or directory: '/does/not/exist'
```
]

???

socket.gaierror: [Errno 8] nodename nor servname provided, or not known

requests.packages.urllib3.exceptions.NewConnectionError: <requests.packages.urllib3.connection.HTTPConnection object at 0x10250b320>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

requests.packages.urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='example.invalid', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x10250b320>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))

requests.exceptions.ConnectionError: HTTPConnectionPool(host='example.invalid', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x10250b320>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))

FileNotFoundError: [Errno 2] No such file or directory: '/does/not/exist'

---

.left-column[
  ## Better Stuff
]

.right-column[
### Keyword-only Arguments
#### Python 2
```
def sort(*things, **kwargs):
    key = kwargs.pop('key', lambda x: x)
```

#### Python 3
```
def sort(*things, key=lambda x: x):
    pass
```
]

---

.left-column[
  ## Better Stuff
]

.right-column[
### Asyncio
```
import asyncio, aiohttp

async def download(session, url):
    async with session.get(url) as response:
        return await response.read()
  
async def download_many(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(
                download(session, url)
            )
            tasks.append(task)
        await asyncio.wait(tasks)    
    return tasks
```
]

---

.left-column[
  ## Better Stuff
]

.right-column[
### Function Annotations
```
from typing import *
from bs4 import Tag

Triples = Iterator[Tuple[Tag, Tag, Tag]]

def _transform(triples: Triples) -> Dict[str, str]: ...  

def _group(lst: List[Any], n: int) -> Iterator[List[Any]]:
    return zip(*[lst[i::n] for i in range(n)])

async def get_info(url: str) -> List[Dict[str, str]]:
    response = await aiohttp.get(url)
    logging.info("Got response")
    data = await response.text()
    logging.info("Got response body")
    soup = BeautifulSoup(data, "html.parser")
    raw_triples = _group(
        soup.select('div.trouble table tr td'),
        3
    )
    information = _transform(raw_triples)
    lines = list(
        sorted(
            information,
            key=lambda info: info['line_en']
        )
    )
    return lines
```
]

---

.left-column[
  ## Better Stuff
]

.right-column[
### Unicode Identifiers
```
def こんにちは世界():
    print("Hello World")
```

Sadly only "letter" characters are allowed, so sadly this is not allowed:
 
```python
def 🏩():
    print("😉")
```
]

---
template: inverse

## Thank You
### Questions?

---
