import pytest


class Test(object):

    @pytest.mark.complete("rcsdiff ")
    def test_(self, completion):
        assert completion.list
