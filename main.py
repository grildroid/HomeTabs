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
import logging
from app import app, socketio, flask_addr, flask_debug, socket_io__logging


# socket.io requests filtering
class LoggerFilter(logging.Filter):
    def filter(self, record):
        if 'socket.io' not in str(record.getMessage()):
            return record


if socket_io__logging is True:
    logging.getLogger("werkzeug").addFilter(LoggerFilter())

from engineio.async_drivers import gevent
socketio.run(app, host=flask_addr[0], port=flask_addr[1], debug=flask_debug)
