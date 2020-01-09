#
# passwordDialog.py - GUI front end code for setting the root password
#
# Brent Fox <bfox@redhat.com>
# Damien Durand <splinux@fedoraproject.org>
# Haikel Guemar <karlthered@fedoraproject.org>
#
# Copyright 2002 - 2006 Red Hat, Inc. and Fedora Usability
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

import gtk
import libuser
import sys

from firstboot.config import *
from firstboot.constants import *
from firstboot.functions import *
from firstboot.module import *

##
## I18N
##
import gettext
_ = lambda x: gettext.ldgettext("firstboot", x)
N_ = lambda x: x


class moduleClass(Module):

    def __init__(self):
        Module.__init__(self)
        self.priority = 40
        self.sidebarTitle = N_("Root Password")
        self.title = N_("Root Password")
        self.icon = None
        self.mode = MODE_RECONFIG

        self.admin = libuser.ADMIN()

    def apply(self, interface, testing=False):
        if testing:
            return RESULT_SUCCESS

        passwd1 = self.passwordEntry.get_text()
        passwd2 = self.confirmEntry.get_text()

        if passwd1 != passwd2:
            self._showErrorMessage(_("The passwords do not match. Please enter the password again."))
            self.passwordEntry.set_text("")
            self.confirmEntry.set_text("")
            self.focus()
            return RESULT_FAILURE

        if passwd1 != "":
            userEnt = self.admin.lookupUserByName("root")
            self.admin.setpassUser(userEnt, passwd1, 0)

        return RESULT_SUCCESS

    def createScreen(self):
        self.vbox = gtk.VBox(False, 10)
        self.vbox.set_border_width(10)

        self.msgLabel = gtk.Label(_("You can change the root password by filling \nthe following fields. If you leave them empty the password will not be changed."))
        self.msgLabel.set_line_wrap(False)
        self.msgLabel.set_alignment(0.0, 0.5)
        self.msgLabel.set_size_request(500, -1)
        self.vbox.pack_start(self.msgLabel, False)

        self.passwordEntry = gtk.Entry()
        self.passwordEntry.set_visibility(False)
        self.confirmEntry = gtk.Entry()
        self.confirmEntry.set_visibility(False)

        table = gtk.Table(2, 2)
        label = gtk.Label(_("New Root Password:"))
        label.set_alignment(0.0, 0.5)
        table.attach(label, 0, 1, 0, 1, gtk.FILL)
        table.attach(self.passwordEntry, 1, 2, 0, 1, gtk.SHRINK, gtk.FILL, 5, 5)
        label = gtk.Label(_("Confirm Root Password:"))
        label.set_alignment(0.0, 0.5)
        table.attach(label, 0, 1, 1, 2, gtk.FILL)
        table.attach(self.confirmEntry, 1, 2, 1, 2, gtk.SHRINK, gtk.FILL, 5, 5)
        self.vbox.pack_start(table, False)
        self.focus()

    def initializeUI(self):
        pass

    def focus(self):
        self.passwordEntry.grab_focus()

    def _showErrorMessage(self, text):
        dlg = gtk.MessageDialog(None, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, text)
        dlg.set_position(gtk.WIN_POS_CENTER)
        dlg.set_modal(True)
        rc = dlg.run()
        dlg.destroy()
        return None
