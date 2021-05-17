"""
HomeTabs
Copyright (C) 2021  grildroid

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys, subprocess

CREATE_NEW_PROCESS_GROUP = 0x00000200
DETACHED_PROCESS = 0x00000008  # Can't be used with CREATE_NEW_CONSOLE
CREATE_NEW_CONSOLE = 0x00000010  # Can't be used with DETACHED_PROCESS
CREATE_NO_WINDOW = 0x08000000

# ONLY FOR WINDOWS SYSTEMS! Opening main (main.py) script without any console windows (silent)
if sys.platform == 'win32':  # SYSTEM: WINDOWS
    subprocess.Popen(['python', 'main.py'], creationflags=CREATE_NO_WINDOW)
