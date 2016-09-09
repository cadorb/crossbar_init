#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.defer import inlineCallbacks
from twisted.logger import Logger

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from autobahn.wamp.exception import ApplicationError
import mysql.connector



class AppSession(ApplicationSession):

    log = Logger()

        

    @inlineCallbacks
    def onJoin(self, details):

        conn = mysql.connector.connect(host="localhost", user="user", password="user", database="crossbar")
        cursor = conn.cursor()
        # SUBSCRIBE to a topic and receive events
        #
        def onclick():
            self.log.info("event for 'onclick' received")
            cursor.execute("""INSERT INTO click (date_click) VALUES(NOW())""")

        yield self.subscribe(onclick, 'com.example.onclick')
        self.log.info("subscribed to topic 'onhello'")


        # REGISTER a procedure for remote calling
        #
        def click_counter():
            self.log.info("click counter called")
            cursor.execute("""SELECT COUNT(id) FROM click""")
            (number_of_rows,) = cursor.fetchone()
            return number_of_rows

        yield self.register(click_counter, 'com.example.click_counter')
        self.log.info("procedure click_counter() registered")

        """
        # PUBLISH and CALL every second .. forever
        #
        counter = 0
        while True:

            # PUBLISH an event
            #
            yield self.publish('com.example.oncounter', counter)
            self.log.info("published to 'oncounter' with counter {counter}",
                          counter=counter)
            counter += 1

            # CALL a remote procedure
            #
            try:
                res = yield self.call('com.example.mul2', counter, 3)
                self.log.info("mul2() called with result: {result}",
                              result=res)
            except ApplicationError as e:
                # ignore errors due to the frontend not yet having
                # registered the procedure we would like to call
                if e.error != 'wamp.error.no_such_procedure':
                    raise e

            yield sleep(1)
        """
        conn.cursor()
