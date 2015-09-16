#!/usr/bin/python
# -*- coding: UTF-8 -*-
from web import background
import web
from datetime import datetime
import random
import time

# URL 规则
urls = ("/", "count_holder",
        "/count", "count",
        "/(.*)", "count_down")

# 应用程序
app = web.application(urls, globals())
#render = web.template.render('templates/')
web.config.debug = False


db = web.database(dbn="mysql", db="db1", user="root", pw="ljgade")
database = web.session.DBStore(db, "session_test")
session = web.session.Session(app, database, initializer={'count': 0})
if 'count' not in session:
    session.count = 0


class count:
    def GET(self):
        session.count += 1
        return 'session count is ' + str(session.count)

# 启动
if __name__ == "__main__":
    app.run()
