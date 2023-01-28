import web

urls = (
    '/', 'Operaciones'
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class Operaciones:
    def GET(self):
        return render.operaciones()
    
    def POST(self):
        form = dict(web.input())
        if form['operacion']=='suma':
            return (form['numero'],"+",form['numero2'],"=", int(form["numero"])+int(form['numero2'])) 
        elif form['operacion']=='resta': 
            return (form['numero'],"-",form['numero2'],"=", int(form["numero"]) - int(form['numero2']))
        elif form['operacion']=='multiplicacion': 
            return (form['numero'],"*",form['numero2'],"=", int(form["numero"]) * int(form['numero2']))
        elif form['operacion']=='division': 
            return (form['numero'],"/",form['numero2'],"=", int(form["numero"]) / int(form['numero2']))
        
if __name__ == "__main__":
    web.config.debug = False
    app.run()