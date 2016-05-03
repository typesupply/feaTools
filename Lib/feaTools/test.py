from __future__ import print_function, division, absolute_import, unicode_literals
import unittest
from .parser import parseFeatures
from .writers.baseWriter import AbstractFeatureWriter


class TestFeatureWriter(AbstractFeatureWriter):

    def __init__(self, name=None):
        self._name = name
        self._instructions = []

    def getData(self):
        data = []
        for token, obj in self._instructions:
            if token == "feature" or token == "lookup":
                obj = (obj._name, obj.getData())
            data.append((token, obj))
        return data

    def feature(self, name):
        self._instructions.append(("feature", TestFeatureWriter(name)))
        token, obj = self._instructions[-1]
        return obj

    def lookup(self, name):
        self._instructions.append(("lookup", TestFeatureWriter(name)))
        token, obj = self._instructions[-1]
        return obj

    def table(self, name, data):
        self._instructions.append(("table", (name, data)))

    def classDefinition(self, name, contents):
        self._instructions.append(("class", (name, contents)))

    def lookupFlag(self, rightToLeft=False, ignoreBaseGlyphs=False, ignoreLigatures=False, ignoreMarks=False):
        self._instructions.append(("lookup flag", (rightToLeft, ignoreBaseGlyphs, ignoreLigatures, ignoreMarks)))

    def gsubType1(self, target, replacement):
        self._instructions.append(("gsub type 1", (target, replacement)))

    def gsubType2(self, target, replacement):
        self._instructions.append(("gsub type 2", (target, replacement)))

    def gsubType3(self, target, replacement):
        self._instructions.append(("gsub type 3", (target, replacement)))

    def gsubType4(self, target, replacement):
        self._instructions.append(("gsub type 4", (target, replacement)))

    def gsubType6(self, precedingContext, target, trailingContext, replacement):
        self._instructions.append(("gsub type 6", (precedingContext, target, trailingContext, replacement)))

    def gposType1(self, target, value):
        self._instructions.append(("gpos type 1", (target, value)))

    def gposType2(self, target, value, needEnum=False):
        self._instructions.append(("gpos type 2", (target, value)))

    def languageSystem(self, languageTag, scriptTag):
        self._instructions.append(("language system", (languageTag, scriptTag)))

    def script(self, scriptTag):
        self._instructions.append(("script", (scriptTag)))

    def language(self, languageTag, includeDefault=True):
        self._instructions.append(("language", (languageTag, includeDefault)))

    def include(self, path):
        self._instructions.append(("include", (path)))

    def subtableBreak(self):
        self._instructions.append(("subtable break", None))

    def lookupReference(self, name):
        self._instructions.append(("lookup reference", name))

    def featureReference(self, name):
        self._instructions.append(("feature reference", name))


class TestRead(unittest.TestCase):

    def testLanguageSystem(self):
        test = "languagesystem DFLT dflt;"
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [('language system', ('dflt', 'DFLT'))]
        self.assertEqual(result, expected)

    def testStrings(self):
        test = """
            "feature test { sub foo by bar; } test;"
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = []
        self.assertEqual(result, expected)

    def testFeatureBlocks(self):
        test = """
        feature test {
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", []))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test{}test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", []))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            sub foo by bar;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 1", ("foo", "bar"))
                ]))
                ]
        self.assertEqual(result, expected)

    def testLookupBlocks(self):
        test = """
        lookup test {
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup", ("test", []))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        lookup test{}test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup", ("test", []))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            lookup TEST {} TEST;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("lookup", ("TEST", []))
                ]))]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            lookup TEST {
                sub foo by bar;
            } TEST;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("lookup", ("TEST", [
                ("gsub type 1", ("foo", "bar"))
                ]))
                ]))]
        self.assertEqual(result, expected)
        #
        test = """
        feature test{lookup TEST{}TEST;}test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("lookup", ("TEST", []))
                ]))]
        self.assertEqual(result, expected)

    def testTableBlocks(self):
        test = """
        table test {
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = []
        self.assertEqual(result, expected)
        #
        test = """
        table test{}test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = []
        self.assertEqual(result, expected)
        #
        test = """
        table test {
            lookup TEST {} TEST;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = []
        self.assertEqual(result, expected)
        #
        test = """
        table OS/2 {
            FSType 0;
            Panose 0 1 2 3 4 5 6 7 8 9;
            UnicodeRange 0 1 2 3 4 5;
            CodePageRange 0 1 2 3 4 5;
            TypoAscender 750;
            TypoDescender -250;
            TypoLineGap 200;
            winAscent 750;
            winDescent -250;
            XHeight 400;
            CapHeight 750;
            WeightClass 500;
            WidthClass 3;
            Vendor "test";
        } OS/2;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("table", ("OS/2", [
            ("FSType", 0),
            ("Panose", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ("UnicodeRange", [0, 1, 2, 3, 4, 5]),
            ("CodePageRange", [0, 1, 2, 3, 4, 5]),
            ("TypoAscender", 750.0),
            ("TypoDescender", -250.0),
            ("TypoLineGap", 200.0),
            ("winAscent", 750.0),
            ("winDescent", -250.0),
            ("XHeight", 400.0),
            ("CapHeight", 750.0),
            ("WeightClass", 500.0),
            ("WidthClass", 3.0)
        ]))]
        self.assertEqual(result, expected)
        #
        test = """
        table head {
            FontRevision 1.1;
        } head;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("table", ("head", [
            ("FontRevision", 1.1),
        ]))]
        self.assertEqual(result, expected)
        #
        test = """
        table hhea {
            CaretOffset 1;
            Ascender 2;
            Descender 3;
            LineGap 4;
        } hhea;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("table", ("hhea", [
            ("CaretOffset", 1),
            ("Ascender", 2),
            ("Descender", 3),
            ("LineGap", 4),
        ]))]
        self.assertEqual(result, expected)
        #
        test = """
        table vhea {
            VertTypoAscender 2;
            VertTypoDescender 3;
            VertTypoLineGap 4;
        } vhea;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("table", ("vhea", [
            ("VertTypoAscender", 2.0),
            ("VertTypoDescender", 3.0),
            ("VertTypoLineGap", 4.0),
        ]))]
        self.assertEqual(result, expected)

    def testLookupFlag(self):
        test = """lookupflag RightToLeft;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup flag", (True, False, False, False))
                ]
        self.assertEqual(result, expected)
        #
        test = """lookupflag IgnoreBaseGlyphs;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup flag", (False, True, False, False))
                ]
        self.assertEqual(result, expected)
        #
        test = """lookupflag IgnoreLigatures;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup flag", (False, False, True, False))
                ]
        self.assertEqual(result, expected)
        #
        test = """lookupflag IgnoreMarks;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup flag", (False, False, False, True))
                ]
        self.assertEqual(result, expected)
        #
        test = """lookupflag RightToLeft, IgnoreBaseGlyphs, IgnoreLigatures, IgnoreMarks;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup flag", (True, True, True, True))
                ]
        self.assertEqual(result, expected)
        #
        test = """lookupflag 0;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup flag", (False, False, False, False))
                ]
        self.assertEqual(result, expected)

    def testGSUBType1(self):
        test = """sub foo by bar;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 1", ("foo", "bar"))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub [foo] by [bar];"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 1", (["foo"], ["bar"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub [foo foo.alt] by [bar];"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 1", (["foo", "foo.alt"], ["bar"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub @foo by @bar;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 1", ("@foo", "@bar"))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        sub foo1 by bar1;
        sub foo2 by bar2;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 1", ("foo1", "bar1")),
                ("gsub type 1", ("foo2", "bar2"))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            sub foo by bar;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 1", ("foo", "bar"))
                ]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {sub foo1 by bar1;sub foo2 by bar2;} test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 1", ("foo1", "bar1")),
                ("gsub type 1", ("foo2", "bar2"))
                ]))
                ]
        self.assertEqual(result, expected)

    def testGSUBType2(self):
        test = """sub f_o_o by f o o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 2", ("f_o_o", ["f", "o", "o"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub f_o_o by [f] o o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 2", ("f_o_o", [["f"], "o", "o"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub f_o_o by @f o o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 2", ("f_o_o", ["@f", "o", "o"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        sub f_o_o by f o o;
        sub b_a_r by b a r;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 2", ("f_o_o", ["f", "o", "o"])),
                ("gsub type 2", ("b_a_r", ["b", "a", "r"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            sub f_o_o by f o o;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 2", ("f_o_o", ["f", "o", "o"]))
                ]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {sub f_o_o by f o o;sub b_a_r by b a r;} test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 2", ("f_o_o", ["f", "o", "o"])),
                ("gsub type 2", ("b_a_r", ["b", "a", "r"]))
                ]))
                ]
        self.assertEqual(result, expected)

    def testGSUBType3(self):
        test = """sub foo from [bar];"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 3", ("foo", ["bar"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        sub foo1 from [bar1];
        sub foo2 from [bar2];
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 3", ("foo1", ["bar1"])),
                ("gsub type 3", ("foo2", ["bar2"]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            sub foo from bar;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 3", ("foo", ["bar"]))
                ]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {sub foo1 from [bar1];sub foo2 from [bar2];} test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 3", ("foo1", ["bar1"])),
                ("gsub type 3", ("foo2", ["bar2"]))
                ]))
                ]
        self.assertEqual(result, expected)

    def testGSUBType4(self):
        test = """sub f o o by f_o_o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 4", (["f", "o", "o"], "f_o_o"))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub [f] o o by f_o_o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 4", ([["f"], "o", "o"], "f_o_o"))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub @f o o by f_o_o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 4", (["@f", "o", "o"], "f_o_o"))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        sub f o o by f_o_o;
        sub b a r by b_a_r;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 4", (["f", "o", "o"], "f_o_o")),
                ("gsub type 4", (["b", "a", "r"], "b_a_r"))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {
            sub f o o by f_o_o;
        } test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 4", (["f", "o", "o"], "f_o_o"))
                ]))
                ]
        self.assertEqual(result, expected)
        #
        test = """
        feature test {sub f o o by f_o_o;sub b a r by b_a_r;} test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature", ("test", [
                ("gsub type 4", (["f", "o", "o"], "f_o_o")),
                ("gsub type 4", (["b", "a", "r"], "b_a_r"))
                ]))
                ]
        self.assertEqual(result, expected)

    def testGSUBType6(self):
        test = """sub f o' by o.alt;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o"], [], "o.alt"))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub f o' o by o.alt;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o"], ["o"], "o.alt"))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub f o' o' by o_o.alt;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o", "o"], [], "o_o.alt"))
                ]
        self.assertEqual(result, expected)
        #
        test = """sub f o' o' b by o_o.alt;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o", "o"], ["b"], "o_o.alt"))
                ]
        self.assertEqual(result, expected)
        #
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        #test = """sub [f] [o]' [o] by o.alt;"""
        #writer = TestFeatureWriter()
        #parseFeatures(writer, test)
        #result = writer.getData()
        #expected = [
        #        ("gsub type 6", ([["f"]], [["o"]], [["o"]], "o.alt"))
        #        ]
        #self.assertEqual(result, expected)
        ##
        #
        test = """sub [foo bar]' bar by [foo.alt bar.alt];"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", ([], [["foo", "bar"]], ["bar"], ["foo.alt", "bar.alt"]))
                ]
        self.assertEqual(result, expected)

    def testIgnoreGSUBType6(self):
        # ("gsub type 6", (precedingContext, target, trailingContext, replacement))
        test = """ignore sub f o';"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o"], [], None))
                ]
        self.assertEqual(result, expected)
        #
        test = """ignore sub f o' o;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o"], ["o"], None))
                ]
        self.assertEqual(result, expected)
        #
        test = """ignore sub f o' o';"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o", "o"], [], None))
                ]
        self.assertEqual(result, expected)
        #
        test = """ignore sub f o' o' b;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", (["f"], ["o", "o"], ["b"], None))
                ]
        self.assertEqual(result, expected)
        #
        test = """ignore sub [foo bar]' bar;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gsub type 6", ([], [["foo", "bar"]], ["bar"], None))
                ]
        self.assertEqual(result, expected)

    def testGPOSType1(self):
        test = """pos foo <0 0 0 0>;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 1", ("foo", (0.0, 0.0, 0.0, 0.0)))
                ]
        self.assertEqual(result, expected)
        #
        test = """pos foo <-10 -10 -10 -10>;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 1", ("foo", (-10.0, -10.0, -10.0, -10.0)))
                ]
        self.assertEqual(result, expected)
        #
        test = """
                pos foo <0 0 0 0>;
                pos foo <-10 -10 -10 -10>;
                """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 1", ("foo", (0.0, 0.0, 0.0, 0.0))),
                ("gpos type 1", ("foo", (-10.0, -10.0, -10.0, -10.0)))
                ]
        self.assertEqual(result, expected)

    def testGPOSType2(self):
        test = """pos foo bar 100;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 2", (["foo", "bar"], 100.0))
                ]
        self.assertEqual(result, expected)
        #
        test = """pos foo bar -100;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 2", (["foo", "bar"], -100.0))
                ]
        self.assertEqual(result, expected)
        #
        test = """enum pos foo [bar bar.alt] -100;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 2", (["foo", ["bar", "bar.alt"]], -100.0))
                ]
        self.assertEqual(result, expected)
        #
        test = """pos @foo @bar -100;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 2", (["@foo", "@bar"], -100.0))
                ]
        self.assertEqual(result, expected)
        #
        test = """pos [foo foo.alt] [bar bar.alt] -100;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("gpos type 2", ([["foo", "foo.alt"], ["bar", "bar.alt"]], -100.0))
                ]
        self.assertEqual(result, expected)

    def testScript(self):
        test = """script test;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("script", "test")
                ]
        self.assertEqual(result, expected)
        #
        test = """
        script test;
        script TEST;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("script", "test"),
                ("script", "TEST"),
                ]
        self.assertEqual(result, expected)
        #
        test = """
        script TEST;script test;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("script", "TEST"),
                ("script", "test"),
                ]
        self.assertEqual(result, expected)
        #
        test = """
        pos foo.subscript bar 100;
        """
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("gpos type 2", (["foo.subscript", "bar"], 100.0))]
        self.assertEqual(result, expected)

    def testInclude(self):
        test = """include(../foo.fea)"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("include", "../foo.fea")
                ]
        self.assertEqual(result, expected)
        #
        test = """include(../foo.fea);"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("include", "../foo.fea")
                ]
        self.assertEqual(result, expected)
        #
        test = """pos include bar 100;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("gpos type 2", (["include", "bar"], 100.0))]
        self.assertEqual(result, expected)

    def testSubtableBreak(self):
        test = """subtable;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("subtable break", None)
                ]
        self.assertEqual(result, expected)
        #
        test = """subtable;subtable;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("subtable break", None),
                ("subtable break", None)
                ]
        self.assertEqual(result, expected)

    def testFeatureReference(self):
        test = """feature test;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("feature reference", "test")
                ]
        self.assertEqual(result, expected)
        #
        test = """feature TEST {feature test;} TEST;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("feature", ("TEST", [("feature reference", "test")]))]
        self.assertEqual(result, expected)

    def testLookupReference(self):
        test = """lookup test;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [
                ("lookup reference", "test")
                ]
        self.assertEqual(result, expected)
        #
        test = """lookup TEST {lookup test;} TEST;"""
        writer = TestFeatureWriter()
        parseFeatures(writer, test)
        result = writer.getData()
        expected = [("lookup", ("TEST", [("lookup reference", "test")]))]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
