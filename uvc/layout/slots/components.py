# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grokcore.component as grok
from dolmen.viewlet import ViewletManager, Viewlet
from dolmen.viewlet.interfaces import IViewlet

from zope.interface import Interface
from uvc.layout.slots.interfaces import ISubMenu, IRenderable


class Menu(ViewletManager):
    grok.baseclass()
    grok.context(Interface)

    def getRenderableItems(self):
        self.update()
        return [v for v in self.viewlets if IRenderable.providedBy(v)]

    def getMenuItems(self):
        rc = []
        self.update()
        for viewlet in self.viewlets:
            if not IRenderable.providedBy(viewlet):
                submenuitems = []
                if ISubMenu.providedBy(viewlet):
                    submenu = viewlet
                    submenu.update()
                    for submenuitem in submenu.viewlets:
                        submenuitems.append(dict(
                            title = submenuitem.title or grok.title.bind().get(submenuitem),
                            id = submenuitem.__class__.__name__.lower(),
                            description = grok.description.bind().get(submenuitem),
                            selected = submenuitem.selected,
                            icon = submenuitem.icon,
                            action = submenuitem.action))
                submenuitems.reverse()
                rc.append(dict(
                    title = viewlet.title or grok.title.bind().get(viewlet),
                    id = viewlet.__class__.__name__.lower(),
                    description = grok.description.bind().get(viewlet),
                    selected = viewlet.selected,
                    icon = viewlet.icon,
                    submenu = submenuitems,
                    action = viewlet.action))
        rc.reverse()
        return rc


class MenuItem(Viewlet):
    grok.baseclass()
    grok.context(Interface)

    title = ""
    action = ""
    icon = ""

    @property
    def selected(self):
        return False
        request_url = self.request.getURL()
        normalized_action = self.action
        if not self.action:
            return False
        if self.action.startswith('@@'):
            normalized_action = self.action[2:]
        if request_url.endswith('/'+normalized_action):
            return True
        if request_url.endswith('/++view++'+normalized_action):
            return True
        if request_url.endswith('/@@'+normalized_action):
            return True
        if request_url == self.action:
            return True
        if request_url.endswith('/@@index'):
            if request_url[:-8] == self.action:
                return True
        return False

    def render(self):
        return u""


class SubMenu(MenuItem, ViewletManager):
    grok.baseclass()
    grok.implements(ISubMenu)

    def update(self):
        ViewletManager.update(self)
