"""
Add a timeout to the property's getter, and only return the cached page if the page
has been requested before the timeout has expired. You can use the time module to
determine whether the cache has expired.

time.time() - an_old_time

returns the number of seconds that have elapsed
since an_old_time
"""


from urllib.request import urlopen
from typing import Optional, cast, List


class WebPage:
    def __init__(self, url: str) -> None:
        self.url = url
        self._content: Optional[bytes] = None
        self._get_time = 0

    @property
    def content(self) -> bytes:
        if self._content is None or self.is_expired():
            print("Retrieving New Page...")
            with urlopen(self.url) as response:
                self._content = response.read()
            self._get_time = time.time()
        return self._content

    def is_expired(self) -> bool:
        return time.time() - self._get_time > 5


if __name__ == "__main__":

    import time

    webpage = WebPage("http://ccphillips.net/")

    now = time.perf_counter()
    content1 = webpage.content
    first_fetch = time.perf_counter() - now
    print(f"First Fetch: {first_fetch}")

    time.sleep(6)

    now = time.perf_counter()
    content2 = webpage.content
    second_fetch = time.perf_counter() - now
    print(f"Second Fetch: {second_fetch}")
