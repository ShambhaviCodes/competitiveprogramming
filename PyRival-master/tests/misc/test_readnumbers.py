import io
import random
import sys

import pyrival.misc


def test_readnumbers(monkeypatch):
    nums = [random.randint(-10000, 10000) for _ in range(100000)]

    string = "".join(str(num) + random.choice([" ", "\n", "\r\n"]) for num in nums).rstrip()
    stream = io.TextIOWrapper(io.BytesIO(string.encode("ascii")))
    monkeypatch.setattr(sys, "stdin", stream)

    read_nums = pyrival.misc.readnumbers()

    assert nums == read_nums
