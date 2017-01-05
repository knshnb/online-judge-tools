#!/usr/bin/env python3

class OnlineJudge(object):
    def download(self, session=None):
        raise NotImplementedError
    def submit(self, code, language=None, session=None):
        raise NotImplementedError
    @classmethod
    def from_url(self, s):
        pass

list = []
def from_url(s):
    for cls in list:
        it = cls.from_url(s)
        if it is not None:
            return it