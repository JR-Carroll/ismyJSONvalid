#! /usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor
#from twisted.web.websocket
from twisted.web import resource
from twisted.web import server

import cgi
import subprocess
import tempfile
import uuid

from syslog import LOG_WARNING, LOG_INFO, LOG_ERR, syslog

class MyFile(File):
    def render_GET(self, request):
        """Intercept the request and print to console"""
        return File.render_GET(self, request)

    def render_POST(self, request):
        """Handle all POST's from WebSite"""
        print dir(request)
        print request
        ## Capture the JSON the user wants to validate
        print str(request.args.get('pastedJSON', [{"No JSON":"Passed"},])[0])
        self._json = str(request.args.get('pastedJSON', [{"No JSON":"Passed"},])[0]).replace("escaped_3B", ";").replace("escaped_26", "&")
        
        myJSON = [x.replace('\n', '<br>').replace(" ", "&nbsp;") for x in self.validateJSON()]
        
        self.creatPermFile()
        
        myString = ""
        for line in myJSON:
            myString += str(line)
        return myString
    
    def encodeData(self):
        pass
    
    def createTMP(self):
        """Write the JSON sent via the client to a tempFile"""
        self._tempFile = tempfile.TemporaryFile()
        return self._tempFile
    
    def creatPermFile(self):
        """Create a file on the FS that can be used to track submissions"""
        ## Context manager for write out.
        _uuid = "{0}.json".format(uuid.uuid4())
        try:
            with open("./submitted/{0}".format(_uuid), 'w') as permFile:
                permFile.write(self._json)
        except:
            ## Pokemon error catching
            raise
        
    def validateJSON(self):
        """Return JSON verification"""
        checkJSON = subprocess.Popen(['json_verify',], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(self._json)
        return checkJSON
            
def receivedData():
    """Pass web data data to the JSON validator"""
    COMMAND = "json -f {0}".format(tmp)
    
def main():
    """The main loop/reactor for the Twisted session."""
    entryPage = MyFile('.')
    factory = Site(entryPage)
    _port = 8888
    reactor.listenTCP(_port, factory)
    print "ismyJSONvalid is running on port {0}".format(_port)
    syslog(LOG_INFO, "ismyJSONvalid is running on port {0}".format(_port))
    reactor.run()

if __name__ == "__main__":
    main()