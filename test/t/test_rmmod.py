import pytest


class Test(object):

    @pytest.mark.complete("rmmod -")
    def test_dash(self, completion):
        assert completion.list
