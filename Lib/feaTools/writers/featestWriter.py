"""
Experimental .featest writer.
"""

from baseWriter import AbstractFeatureWriter


class FeatestWriter(object):

    def __init__(self):
        self._classes = {}
        self._tests = []
        self._currentFeature = None

    def write(self):
        return "\n".join(self._tests)

    def _flatten(self, item):
        if isinstance(item, list):
            item = item[0]
        if item.startswith("@"):
            contents = []
            for i in self._classes[item]:
                i = self._flatten(i)
                contents.extend(i)
            item = contents
        else:
            item = [item]
        return item

    def _stringify(self, items):
        return " ".join(items)

    def feature(self, name):
        self._tests.append("")
        self._tests.append("+ %s" % name)
        self._tests.append("- %s" % self._currentFeature)
        self._tests.append("")
        self._currentFeature = name
        return self

    def lookup(self, name):
        return self

    def classDefinition(self, name, contents):
        self._classes[name] = contents

    def gsubType1(self, target, replacement):
        target = self._flatten(target)
        replacement = self._flatten(replacement)
        self._tests.append("> %s" % self._stringify(target))
        self._tests.append("< %s" % self._stringify(replacement))

    gsubType3 = gsubType1
    gsubType4 = gsubType1

    def _simplifyContext(self, context):
        simplified = []
        for i in context:
            if isinstance(i, list):
                i = i[0]
            i = self._flatten(i)[0]
            simplified.append(i)
        return simplified

    def gsubType6(self, precedingContext, target, trailingContext, replacement):
        precedingContext = self._simplifyContext(precedingContext)
        target = self._simplifyContext(target)
        trailingContext = self._simplifyContext(trailingContext)
        before = precedingContext + target + trailingContext

        if isinstance(replacement, list):
            replacement = replacement[0]
        replacement = self._flatten(replacement)[0]

        self._tests.append("# XXX contextual substitution was mechanically simplified")
        self._tests.append("> %s" % self._stringify(before))
        self._tests.append("< %s" % replacement)

    def gposType1(self, target, value):
        raise NotImplementedError

    def gposType2(self, target, value):
        raise NotImplementedError

    def languageSystem(self, languageTag, scriptTag):
        self._tests.append("^ %s" % scriptTag)
        self._tests.append("@ %s" % languageTag)

    def script(self, scriptTag):
        self._tests.append("^ %s" % scriptTag)

    def language(self, languageTag, includeDefault=True):
        self._tests.append("@ %s" % languageTag)

    def include(self, path):
        # need to resolve the path, parse and write
        raise NotImplementedError

