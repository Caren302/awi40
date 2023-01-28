import web

urls = (
    '/', 'Tabla'
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class Tabla:
    def GET(self):
        datos=[
            ["1","DEJAH"],
            ["2","JOHN"]
        ]
        return render.tabla(datos)
        
if __name__ == "__main__":
    web.config.debug = False
    app.run()