# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de


from cromlech.webob.response import Response
from dolmen.layout import Layout
from grokcore.component import context
from uvc.layout.utils import get_template
from zope.interface import Interface

from nva.fernlehrgang.resources import css


class UVCLayout(Layout):
    context(Interface)

    responseFactory = Response
    template = get_template('layout.cpt')

    title = u"Fernlehrgang"
    base = u"/"

    def __call__(self, content, **extra):
        css.need()
        return Layout.__call__(self, content, **extra)
