class AbstractFeatureWriter(object):

    def feature(self, name):
        return self

    def lookup(self, name):
        return self

    def table(self, name, data):
        pass

    def featureReference(self, name):
        pass

    def lookupReference(self, name):
        pass

    def classDefinition(self, name, contents):
        pass

    def lookupFlag(self, rightToLeft=False, ignoreBaseGlyphs=False, ignoreLigatures=False, ignoreMarks=False):
        pass

    def gsubType1(self, target, replacement):
        pass

    def gsubType3(self, target, replacement):
        pass

    def gsubType4(self, target, replacement):
        pass

    def gsubType6(self, precedingContext, target, trailingContext, replacement):
        pass

    def gposType1(self, target, value):
        pass

    def gposType2(self, target, value, needEnum=False):
        pass

    def languageSystem(self, languageTag, scriptTag):
        pass

    def script(self, scriptTag):
        pass

    def language(self, languageTag, includeDefault=True):
        pass

    def include(self, path):
        pass

    def subtableBreak(self):
        pass

    def rawText(self, text):
        pass
