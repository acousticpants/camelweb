import web
from camelweb import map

urls = (
    '/game', 'GameEngine', '/', 'index',
)

app = web.application(urls, globals())

# a little hack so debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer = {'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

class index(object):
    def GET(self):
        # this is used to 'setup' session with start values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room = session.room)
        else:
            # why is this here? is it needed?
            return render.you_died()

    def POST(self):
        form = web.input(action = None)

        # there is a bug here. fix.
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
