import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # N=3, M=3 => 1, 3, 9, 27
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b1\b', r'\b3\b', r'\b9\b', r'\b27\b'], content)


@pytest.mark.T2
def test_main_2():
    # N=2, M=4 => 1, 2, 4, 8, 16
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b1\b', r'\b2\b', r'\b4\b', r'\b8\b', r'\b16\b'], content)


@pytest.mark.T3
def test_main_3():
    # N=5, M=2 => 1, 5, 25
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b1\b', r'\b5\b', r'\b25\b'], content)


@pytest.mark.T4
def test_main_4():
    # N=4, M=3 => 1, 4, 16, 64
    content = open('result4.txt').read()
    print(content)
    regex_test([r'\b1\b', r'\b4\b', r'\b16\b', r'\b64\b'], content)
