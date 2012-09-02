#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

import os
import re

ref = re.M|re.I|re.U

from minitage.recipe.common.common import which

def pycairo(options,buildout):
    cwd = os.getcwd()
    if not os.path.isfile(options['configure']):
        options['configure'] = which(options['configure'])
    os.chdir(options['compile-directory'])
    cmd = '%s %s%s %s' % (
        options['configure'],
        options['prefix-option'],
        options['prefix'],
        options['configure-options']
        )
    print "Running %s"  % cmd
    os.system(cmd)
    os.chdir(cwd)



# vim:set et sts=4 ts=4 tw=80:
