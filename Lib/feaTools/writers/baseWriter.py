class AbstractFeatureWriter(object):

    def feature(self, name):
        raise NotImplementedError

    def lookup(self, name):
        raise NotImplementedError

    def featureReference(self, name):
        raise NotImplementedError

    def lookupReference(self, name):
        raise NotImplementedError

    def classDefinition(self, name, contents):
        raise NotImplementedError

    def gsubType1(self, target, replacement):
        raise NotImplementedError

    def gsubType3(self, target, replacement):
        raise NotImplementedError

    def gsubType4(self, target, replacement):
        raise NotImplementedError

    def gsubType6(self, precedingContext, target, trailingContext, replacement):
        raise NotImplementedError

    def gposType1(self, target, value):
        raise NotImplementedError

    def gposType2(self, target, value):
        raise NotImplementedError

    def languageSystem(self, languageTag, scriptTag):
        raise NotImplementedError

    def script(self, scriptTag):
        raise NotImplementedError

    def language(self, languageTag, includeDefault=True):
        raise NotImplementedError

    def include(self, path):
        raise NotImplementedError

    def subtableBreak(self):
        raise NotImplementedError
