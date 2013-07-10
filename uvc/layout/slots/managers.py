# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de


import grokcore.component as grok

from dolmen.viewlet import ViewletManager
from uvc.layout.interfaces import *
from zope.interface import Interface


class Resources(ViewletManager):
    grok.name('uvc-resources')
    grok.context(Interface)


class Headers(ViewletManager):
    """Viewlet Manager for the Header
    """
    grok.name('uvc-headers')
    grok.context(Interface)
    grok.implements(IHeaders)


class AboveContent(ViewletManager):
    grok.name('uvc-above-body')
    grok.context(Interface)
    grok.implements(IAboveContent)


class Tabs(ViewletManager):
    grok.name('uvc-tabs')
    grok.context(Interface)
    grok.implements(ITabs)

    def content(self):
        results = [v.render() for v in self.viewlets]
        return "\n".join([r for r in results if r.strip()])

    def render(self):
        res = self.content()
        if not res:
            return u""
        return """<ul class='nav nav-pills'>%s</ul>""" % res


class BelowContent(ViewletManager):
    grok.name('uvc-below-body')
    grok.context(Interface)
    grok.implements(IBelowContent)


class PageTop(ViewletManager):
    """ViewletManager for the PageTop
    """
    grok.name('uvc-pagetop')
    grok.context(Interface)
    grok.implements(IPageTop)


class Footer(ViewletManager):
    """ViewletManager for the PageTop
    """
    grok.name('uvc-footer')
    grok.context(Interface)
    grok.implements(IPageFooter)
    #grok.require('zope.View')


class BeforeActions(ViewletManager):
    grok.name('uvcsite.beforeactions')
    grok.context(Interface)
    grok.implements(IBeforeActions)
    #grok.require('zope.View')


class ExtraInfo(ViewletManager):
    grok.name('uvcsite.extrainfo')
    grok.context(Interface)
    grok.implements(IExtraInfo)
    #grok.require('zope.View')
