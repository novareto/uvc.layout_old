# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import os

from dolmen.template import TALTemplate


TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')


def get_template(filename):
    return TALTemplate(os.path.join(TEMPLATES_DIR, filename))
