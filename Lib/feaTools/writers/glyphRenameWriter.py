"""
This writer lets you rename glyphs and output text in FDK syntax.
To rename glyphs, pass a dictionary of {beforeName:afterName} as the
remap argument in the constructor.
"""

from baseWriter import AbstractFeatureWriter
from fdkSyntaxWriter import FDKSyntaxFeatureWriter


class GlyphRenameFeatureWriter(FDKSyntaxFeatureWriter):

    def __init__(self, remap, name=None, isFeature=False):
        self._map = remap
        super(GlyphRenameFeatureWriter, self).__init__(name=name, isFeature=isFeature)

    def _rename(self, glyphList):
        if glyphList is None:
            return None
        if isinstance(glyphList, basestring):
            return self._map.get(glyphList, glyphList)
        return [self._rename(glyphName) for glyphName in glyphList]

    def _subwriter(self, name, isFeature):
        return GlyphRenameFeatureWriter(self._map, name, isFeature=isFeature)

    def classDefinition(self, name, contents):
        contents = self._rename(contents)
        super(GlyphRenameFeatureWriter, self).classDefinition(name, contents)

    def gsubType1(self, target, replacement):
        target = self._rename(target)
        replacement = self._rename(replacement)
        super(GlyphRenameFeatureWriter, self).gsubType1(target, replacement)

    def gsubType3(self, target, replacement):
        target = self._rename(target)
        replacement = self._rename(replacement)
        super(GlyphRenameFeatureWriter, self).gsubType3(target, replacement)

    def gsubType4(self, target, replacement):
        target = self._rename(target)
        replacement = self._rename(replacement)
        super(GlyphRenameFeatureWriter, self).gsubType4(target, replacement)

    def gsubType6(self, precedingContext, target, trailingContext, replacement):
        precedingContext = self._rename(precedingContext)
        target = self._rename(target)
        trailingContext = self._rename(trailingContext)
        replacement = self._rename(replacement)
        super(GlyphRenameFeatureWriter, self).gsubType6(precedingContext, target, trailingContext, replacement)

    def gposType1(self, target, value):
        target = self._rename(target)
        super(GlyphRenameFeatureWriter, self).gposType1(target, value)

    def gposType2(self, target, value):
        target = self._rename(target)
        super(GlyphRenameFeatureWriter, self).gposType2(target, value)
