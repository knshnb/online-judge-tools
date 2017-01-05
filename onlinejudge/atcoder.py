#!/usr/bin/env python3
import onlinejudge
import onlinejudge.problem
import onlinejudge.implementation.utils as utils
import re
import bs4

class AtCoder(onlinejudge.problem.OnlineJudge):
    onlinejudge_name = 'atcoder'

    def __init__(self, contest_id, problem_id):
        self.contest_id = contest_id
        self.problem_id = problem_id

    def download(self, session=None):
        content = utils.download(self.get_url(), session, get_options={ 'allow_redirects': False })  # allow_redirects: if the URL is wrong, AtCoder redirects to the top page
        soup = bs4.BeautifulSoup(content, 'lxml')
        samples = utils.SampleZipper()
        for pre in soup.find_all('pre'):
            it = self.parse_sample_tag(pre)
            if it is not None:
                s, name = it
                samples.add(s, name)
        return samples.get()

    def parse_sample_tag(self, tag):
        assert isinstance(tag, bs4.Tag)
        assert tag.name == 'pre'
        try:
            prv = tag.previous_sibling
            while prv and prv.string.strip() == '':
                prv = prv.previous_sibling
            if prv.name == 'h3' and tag.parent.name == 'section':
                return tag.string.lstrip().replace('\r\n', '\n'), prv.string
        except AttributeError:
            pass
        try:
            prv = tag.parent.previous_sibling
            while prv and prv.string.strip() == '':
                prv = prv.previous_sibling
            if tag.parent.name == 'section' and prv.name == 'h3':
                return tag.string.lstrip().replace('\r\n', '\n'), prv.string
        except AttributeError:
            pass

    def get_url(self):
        return 'http://{}.contest.atcoder.jp/tasks/{}'.format(self.contest_id, self.problem_id)

    @classmethod
    def from_url(cls, s):
        m = re.match('^https?://([0-9A-Za-z-]+)\.contest\.atcoder\.jp/tasks/([0-9A-Za-z_]+)/?$', s)
        if m:
            return cls(m.group(1), m.group(2))

onlinejudge.problem.list += [ AtCoder ]