import web

urls = (
    '/', 'Index',
    '/welcome', 'Welcome'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Welcome:
    def GET(self):
        """num1= "Hola "   
        num2 = " a "
        num3 = " Pericles"
        x = num1 + num2 + num3
        print(x)"""
        return render.bienvenida("")

if __name__ == "__main__":
    app.run()