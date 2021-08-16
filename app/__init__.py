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
import os, sys, time, sqlite3, contextlib, configparser
from flask import Flask

from flask_socketio import SocketIO


VERSION_NUM = '1.0.3'

logfile_name = f'lastlog.log' # Log-file name for ReLogger

flask_debug = False # [True/False] True - debug-mode Flask
socket_io__logging_block = False # [True/False] False - log SocketIO Werkzeug requests to console


# Collect data from STDOUT and STDERR. Prints data to log file
class ReLogger(object):
    __class_prefix = 'ReLogger'

    def __init__(self, stream_type):
        self.print(f'[INFO] Initiated ReLogger on {stream_type}')
        open(logfile_name, "w", encoding='utf-8').write('')

        if stream_type == 'stdout':
            self.terminal_stdout = sys.stdout
        else:
            self.terminal_stdout = sys.stderr

    def write(self, message):
        self.terminal_stdout.write(message)
        message = str(message).replace('[0m', '').replace('[33m', '').replace('[37m', '')
        open(logfile_name, "a", encoding='utf-8').write(message)

    def flush(self):
        pass

    # Print function for class
    def print(self, data):
        print(f'({time.strftime("%H:%M:%S")}) [{self.__class_prefix}] {data}')

sys.stdout = ReLogger(stream_type='stdout')
sys.stderr = ReLogger(stream_type='stderr')
print('\n  HomeTabs Copyright (C) 2021  grildroid. HomeTabs Licensed under GNU General Public License 3.0  \n')
print(f'Current HomeTabs version: {VERSION_NUM}\n')

# Code block for --onefile parameter of pytoexe
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

app.secret_key = os.urandom(24).hex()
socketio = SocketIO(app)

# Config controller class
class ConfigController:
    __class_prefix = 'ConfigController'
    config_file = 'config.ini'  # Config file name
    config = None

    def __init__(self):
        self.config = configparser.ConfigParser()

        if os.path.isfile(self.config_file):
            self.config.read(self.config_file)
            self.print(f"[OK] Found config: {self.config_file}")
        else:
            self.print(f"[ERROR] Can't find {self.config_file}")
            self.create_config()
            self.print(f"[OK] Created config: {self.config_file}")
        print('')

    def create_config(self):
        self.config.add_section('Settings')
        self.config.set('Settings', 'ip', '127.0.1.1')
        self.config.set('Settings', 'port', '8000')
        with open(self.config_file, 'w') as config_file_fp:
            self.config.write(config_file_fp)

    # Print function for class
    def print(self, data):
        print(f'({time.strftime("%H:%M:%S")}) [{self.__class_prefix}] {data}')

ConfigControllerOBJ = ConfigController()
ip = ConfigControllerOBJ.config.get("Settings", "ip")
port = int(ConfigControllerOBJ.config.get("Settings", "port"))
flask_addr = (ip, port) # Flask server address

if port != 443: print(f'[INFO] HomeTabs will be runned on: http://{ip}:{port}/\n')
else: print(f'[INFO] HomeTabs will be runned on: https://{ip}:{port}/\n')


# Database controller class
class TabsController:
    __class_prefix = 'TabsController'
    tabs_db_name = 'tabs_data.sqlite3' # Tabs database name. Should be .sqlite3

    __create_tabs__sql = """CREATE TABLE tabs (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name text, url text, icon_url text)"""
    __get_tabs_all__sql = """SELECT * FROM tabs"""
    __num_of_tabs = 32 # Number of generating tabs: 8/16/24/32

    def __init__(self):
        if os.path.isfile(self.tabs_db_name):
            self.print(f'[OK] Found tabs database: {self.tabs_db_name}')
        else:
            self.print(f"[ERROR] Can't find tabs database ({self.tabs_db_name})")
            self.create_db()
            self.print(f'[OK] Tabs database created: {self.tabs_db_name}')
        print('')


    # Create database function
    def create_db(self):
        with contextlib.closing(sqlite3.connect(self.tabs_db_name)) as conn:
            conn.row_factory = self.__dict_factory
            cursor = conn.cursor()
            cursor.execute(self.__create_tabs__sql)

            for iteration in range(1, self.__num_of_tabs+1):
                if iteration == 1:
                    cursor.execute('INSERT INTO tabs (id, name, url, icon_url) VALUES (?, ?, ?, ?)', (iteration, 'Visit author 💖', 'https://github.com/grildroid', '/static/icons/github.png'))
                else:
                    cursor.execute('INSERT INTO tabs (id) VALUES (?)', (iteration,))

            cursor.close()
            conn.commit()


    # Return all tabs data
    def get_all(self):
        with contextlib.closing(sqlite3.connect(self.tabs_db_name)) as conn:
            conn.row_factory = self.__dict_factory
            cursor = conn.cursor()

            cursor.execute(self.__get_tabs_all__sql)
            result = cursor.fetchall()

            cursor.close()
            conn.commit()
        return result

    # Update tab data
    def tab_update(self, tab_data):
        with contextlib.closing(sqlite3.connect(self.tabs_db_name)) as conn:
            cursor = conn.cursor()

            tab_data = dict(tab_data)
            for key in tab_data.keys():
                if tab_data[key] == '': # Replacing key:'' to key:None for database
                    tab_data[key] = None

            cursor.execute('UPDATE tabs SET (name, url, icon_url) = (?, ?, ?) WHERE id = ?', (tab_data['name'], tab_data['url'], tab_data['icon_url'], int(tab_data['id'])+1))
            conn.commit()
            self.print(f'[INFO] Updated tab with id: {int(tab_data["id"])+1}')

    # Replace all tab data to None
    def tab_delete(self, tab_id):
        with contextlib.closing(sqlite3.connect(self.tabs_db_name)) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE tabs SET (name, url, icon_url) = (?, ?, ?) WHERE id = ?', (None, None, None, int(tab_id)+1))
            conn.commit()
            self.print(f'[INFO] Deleted tab with id: {int(tab_id) + 1}')

    # Print function for class
    def print(self, data):
        print(f'({time.strftime("%H:%M:%S")}) [{self.__class_prefix}] {data}')

    # For get_all function. Returns data of tab in dictionary
    @staticmethod
    def __dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
Tabs = TabsController()

#flask_socketio_thread = threading.Thread(target=socketio.run, args=(app, flask_addr[0], flask_addr[1])) #TODO: Flask thread (SAVED FOR THE FUTURE)

from app import views
