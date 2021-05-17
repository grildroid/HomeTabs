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
from app import app, Tabs, socketio
import flask

yandex_se = 'https://yandex.ru/search/?text='
google_se = 'https://www.google.ru/search?q='

@socketio.on('save_tab')
def savetab(tab_data):
    Tabs.tab_update(tab_data)
    socketio.emit('reload_page', 'tab_saved')

@socketio.on('delete_tab')
def deletetab(tab_id):
    Tabs.tab_delete(tab_id['id'])
    socketio.emit('reload_page', 'tab_deleted')


# Главная страница
@app.route('/', methods=['get', 'post'])
def page__index():
    response = flask.make_response(flask.render_template('index.html', tabs_data=Tabs.get_all()))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Простой поиск (БЕЗ ПОДСКАЗОК)
@app.route('/search-simple', methods=['get', 'post'])
def search_system():
    searchbar_data = flask.request.form.get('searchbar_input')
    yandex_search_url = google_se + searchbar_data
    return flask.redirect(yandex_search_url)
