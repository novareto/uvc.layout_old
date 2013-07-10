# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grokcore.component as grok
from dolmen.viewlet import Viewlet, slot
from zope.interface import Interface
from uvc.layout.interfaces import IPageFooter, IPageTop, IAboveContent, ITabs
from zope.component import getMultiAdapter
from uvc.layout.slots.utils import get_template
from dolmen.viewlet.interfaces import IViewlet, IViewletManager


class GlobalMenuViewlet(Viewlet):
    slot(IPageTop)
    grok.context(Interface)
    grok.order(20)

    template = get_template('globalmenutemplate.cpt')
    id = "globalmenuviewlet"

    def update(self):
        globalmenu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'globalmenu')
        self.menus = globalmenu.getMenuItems()
        self.renderableitems = globalmenu.getRenderableItems()


class PersonalPreferencesViewlet(Viewlet):
    slot(IPageTop)
    grok.context(Interface)
    grok.order(40)

    template = get_template('personalpreferencestemplate.cpt')
    id = "personalpreferencesviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'personalpreferences').getMenuItems()

    @property
    def username(self):
        return "BLA"


class DocumentActionsMenuViewlet(Viewlet):
    slot(IAboveContent)
    grok.context(Interface)
    grok.order(40)

    template = get_template('documentactionstemplate.cpt')
    id = "documentactionsmenuviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'documentactions').getMenuItems()


class FooterViewlet(Viewlet):
    slot(IPageFooter)
    grok.context(Interface)
    grok.order(10)

    template = get_template('footertemplate.cpt')
    id = "footerviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'footermenu').getMenuItems()
        print self.menus


class ExtraViewsViewlet(Viewlet):
    slot(ITabs)
    grok.context(Interface)
    grok.order(10)

    template = get_template('extraviewstemplate.cpt')
    id = "extraviewsviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'extraviews').getMenuItems()
