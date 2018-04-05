# -*- coding: utf-8 -*-
import web
import json
from datetime import datetime

host = 'http://localhost:8888'

urls = (
    '/', 'add'
)
app = web.application(urls, globals())


class add:
    def POST(self):
        i = web.data()
        print repr(i)
        return '200'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()

