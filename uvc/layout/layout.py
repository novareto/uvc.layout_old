# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de


from cromlech.webob.response import Response
from dolmen.layout import Layout
from grokcore.component import context
from uvc.layout.utils import get_template
from zope.interface import Interface


class UVCLayout(Layout):
    context(Interface)

    responseFactory = Response
    template = get_template('layout.cpt')
    base = u"/"
