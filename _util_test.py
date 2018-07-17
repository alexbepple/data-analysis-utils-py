from ._util import unzip

def test_unzip_list_of_2_tuples():
    assert unzip([(0, 2), (1, 3)]) == ([0, 1], [2, 3])
def test_unzip_list_of_3_tuples():
    assert unzip([(0, 1, 2)]) == ([0], [1], [2])
