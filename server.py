
import cherrypy
import json

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"


@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return "hello world"
    
    def POST(self, content=""):
        d = {"content": content}
        with open("/home/vivekkulkarni/pose_test/sample.json", "w") as f:
            json.dump(d, f)
        return "Success"

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.config.update({'server.socket_port': 80})
    cherrypy.quickstart(StringGeneratorWebService(), '/sample', conf)