import web

urls = (
    '/2', 'Index',
    '/hello', 'Index',
    '/test', 'Test',
    '/hello2', 'Index2',
    '/hello4', 'Index4',
    '/test3', 'Index3'
    )

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

class Index2(object):
    def GET(self):
        form = web.input(greet="Hello", name="Nobody")
        greeting2 = "%s, %s!" % (form.greet, form.name)
        return render.index2(greeting2 = greeting2)


class Test(object):
    def GET(self):
        copy = "Test Copy"
        return render.test(copy = copy)


if __name__ == "__main__":

    app.run()
