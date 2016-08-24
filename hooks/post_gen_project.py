#!/usr/bin/env python

import os
import subprocess as sp


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def execute(cmd):
    print(sp.getoutput(cmd))


def git_init():
    execute('git init')
    execute('git add .')
    execute('git commit -sm "first commit"')


def setup_develop():
    execute('python setup.py develop')


if __name__ == '__main__':
    git_init()
    setup_develop()
