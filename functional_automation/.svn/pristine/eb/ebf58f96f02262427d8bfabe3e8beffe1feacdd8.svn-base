# connect database class
# -*- coding:utf-8 -*-

import psycopg2


# import traceback


class ConnectDb(object):

    def __init__(self, database, user, password, host, port):

        self._database = database
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._conn = self.Connect_to_postgreSQL()

        if self._conn:
            self._cur = self._conn.cursor()

    def Connect_to_postgreSQL(self):

        try:
            conn = psycopg2.connect(database=self._database, user=self._user, password=self._password, host=self._host,
                                    port=self._port)
        except Exception, e:
            print e
            conn = False

        self._conn = conn

        return conn

    def ExecuteSQL(self, sql):

        if self._conn:

            try:
                self._cur.execute(sql)
                result = self._cur.fetchall()
            except Exception, e:
                print e

        return result

    def Disconnect_from_postgreSQL(self):

        if self._conn:

            if type(self._cur) == 'object':
                self._cur.close()

            if type(self._conn) == 'object':
                self._conn.close()
