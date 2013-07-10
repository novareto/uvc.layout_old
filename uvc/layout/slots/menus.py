# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grokcore.component as grok

from uvc.layout.interfaces import *
from uvc.layout.slots.components import Menu
from zope.interface import Interface


class GlobalMenu(Menu):
    grok.implements(IGlobalMenu)
    grok.name('globalmenu')


class Footer(Menu):
    grok.implements(IFooter)
    grok.name('footermenu')


class PersonalPreferences(Menu):
    grok.implements(IPersonalPreferences)
    grok.name('personalpreferences')


class DocumentActionsMenu(Menu):
    grok.implements(IDocumentActions)
    grok.name('documentactions')


class ExtraViews(Menu):
    grok.implements(IExtraViews)
    grok.context(Interface)
    grok.name('extraviews')


class PersonalMenu(Menu):
    grok.implements(IPersonalMenu)
    grok.context(Interface)
    grok.name('personalmenu')
