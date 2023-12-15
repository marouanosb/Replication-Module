from replc import replicate

def test_function1(x):
    return x


def test_replicate():
    assert replicate(2, 4,test_function1, 7)== [[7,7,7,7],[7,7,7,7]]