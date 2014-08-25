# -*- encoding:utf-8 -*-
#  This file is part of gedit-advanced-find
#  Copyright (c) 2012  GPL William Heaton <William.G.Heaton@gmail.com>
#  
#  gedit-advanced-find is free software: you may copy, redistribute
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 2 of the
#  License, or (at your option) any later version.
#  
#  This file is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  This file incorporates work covered by the following copyright and
#  permission notice:  
# 
#######################################################################
# __init__.py is part of advancedfind-gedit
#
# Copyright 2010-2012 swatch
#
# advancedfind-gedit is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#######################################################################
from gi.repository import GObject, Gtk, Gedit, PeasGtk
from .advancedfind import AdvancedFindWindowHelper
from .config_ui import ConfigUI
class AdvancedFindReplacePlugin(GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable):
	__gtype_name__ = "AdvancedFindReplacePlugin"
	window = GObject.property(type=Gedit.Window)
	def __init__(self):
		GObject.Object.__init__(self)
	def do_activate(self):
		self._plugin = AdvancedFindWindowHelper(self, self.window)
	def do_deactivate(self):
		self._plugin.deactivate()
		del self._plugin
	def get_instance(self):
		return self._plugin, self.window

