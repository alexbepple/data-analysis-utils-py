from ._util import unzip

class TestUnzip(object):
    def test_list_of_2_tuples(self):
        assert unzip([(0, 2), (1, 3)]) == ([0, 1], [2, 3])
    def test_list_of_3_tuples(self):
        assert unzip([(0, 1, 2)]) == ([0], [1], [2])
