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
# config_ui.py is part of advancedfind-gedit.
#
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
from gi.repository import Gtk, Gedit, Gdk
import os.path
	
#from gettext import gettext as _
APP_NAME = 'advancedfind'
CONFIG_DIR = os.path.expanduser('~/.local/share/gedit/plugins/' + APP_NAME + '/config')
class ConfigUI(object):
	def __init__(self, plugin):
		self._instance, self._window = plugin.get_instance()
		gladefile = os.path.join(os.path.dirname(__file__),"config.glade")
		UI = Gtk.Builder()
		UI.set_translation_domain('advancedfind')
		UI.add_from_file(gladefile)
		self.configWindow = UI.get_object("configWindow")
		self.fgColorbutton = UI.get_object("fgColorbutton")
		self.bgColorbutton = UI.get_object("bgColorbutton")
		self.fgColorbutton.set_color(Gdk.color_parse(self._instance.result_highlight['FOREGROUND_COLOR']))
		self.bgColorbutton.set_color(Gdk.color_parse(self._instance.result_highlight['BACKGROUND_COLOR']))

	def on_colorThemeComboboxtext_changed(self, object):
		print(os.path.expanduser('~/.local/share/gedit/plugins/' + APP_NAME + '/config/theme/') + object.get_active_text() + '.xml')
		
	def on_colorThemeComboboxtext_popup(self, object):
		print('Theme selection popdown.')
		object.remove_all();
		for root, dirs, files in os.walk(os.path.expanduser('~/.local/share/gedit/plugins/' + APP_NAME + '/config/theme')):
			for f in files:
				if f.endswith('.xml'):
					object.append_text(f[0:-4])
	def on_rootFollowFilebrowserCheckbutton_toggled(self, widget):
		self._instance.find_options['ROOT_FOLLOW_FILEBROWSER'] = widget.get_active()
		
	def on_keepHistoryCheckbutton_toggled(self, object):
		self._instance.find_dlg_setting['KEEP_HISTORY'] = object.get_active()
if __name__ == '__main__':
	dlg = ConfigUI(None)
	Gtk.main()
	
