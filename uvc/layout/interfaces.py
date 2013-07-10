# -*- coding: utf-8 -*-

from zope.interface import Interface
from dolmen.viewlet.interfaces import IViewSlot


class IPageTop(IViewSlot):
    """Marker For the area that sits at the top of the page.
    """


class ITabs(IViewSlot):
    """Marker for the action tabs.
    """


class IAboveContent(IViewSlot):
    """Marker For the area that sits above the page body.
    """


class IBelowContent(IViewSlot):
    """Marker For the area that sits under the page body.
    """


class IHeaders(IViewSlot):
    """Marker For Headers
    """


class IToolbar(IViewSlot):
    """Marker for Toolbar
    """


class IDocumentActions(IViewSlot):
    """Marker for DocumentActions
    """


class IPersonalPreferences(IViewSlot):
    """Marker for PersonalPreferences
    """


class IGlobalMenu(IViewSlot):
    """Marker for GlobalMenu
    """


class IPersonalMenu(IViewSlot):
    """Marker for PersonalMenu
    """


class ISidebar(IViewSlot):
    """Marker for Sitebar
    """


class IFooter(IViewSlot):
    """Marker for Footer
    """

class IPageFooter(IViewSlot):
    """ """


class IPanels(IViewSlot):
    """Marker interface for the panels display.
    """


class IHelp(IViewSlot):
    """Marker for Help
    """


class IExtraInfo(IViewSlot):
    """Marker for ExtraInfo in Forms
    """


class IExtraViews(IViewSlot):
    """Marker for additional Views for Folders
       Objects etc...
    """

class ISpotMenu(IViewSlot):
    """ Special Menu """


class IBeforeActions(IViewSlot):
    """ Marker Interfae"""
