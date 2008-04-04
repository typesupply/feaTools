"""
Printing writer. Used for testing.
"""

from baseWriter import AbstractFeatureWriter


class PrintFeatureWriter(AbstractFeatureWriter):

    def feature(self, name):
        print ("feature", name)
        return self

    def lookup(self, name):
        print ("lookup", name)
        return self

    def classDefinition(self, name, contents):
        print ("class", (name, contents))

    def gsubType1(self, target, replacement):
        print ("gsub type 1", (target, replacement))

    def gsubType3(self, target, replacement):
        print ("gsub type 3", (target, replacement))

    def gsubType4(self, target, replacement):
        print ("gsub type 4", (target, replacement))

    def gsubType6(self, precedingContext, target, trailingContext, replacement):
        print ("gsub type 6", (precedingContext, target, trailingContext, replacement))

    def gposType1(self, target, value):
        print ("gpos type 1", (target, value))

    def gposType2(self, target, value):
        print ("gpos type 2", (target, value))

    def languageSystem(self, languageTag, scriptTag):
        print ("language system", (languageTag, scriptTag))

    def script(self, scriptTag):
        print ("script", (scriptTag))

    def language(self, languageTag, includeDefault=True):
        print ("language", (languageTag, includeDefault))

    def include(self, path):
        print ("include", (path))

    def subtableBreak(self):
        print "subtable break"
