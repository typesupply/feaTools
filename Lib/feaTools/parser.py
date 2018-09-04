from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import re


class FeaToolsParserSyntaxError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# used for removing all comments
commentRE = re.compile(r"#.*")

# used for finding all strings
stringRE = re.compile(
    r"\""         # "
    r"([^\"]*)"   # anything but "
    r"\""         # "
)

# used for removing all comments
terminatorRE = re.compile(r";")

# used for finding all feature names.
feature_findAll_RE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"feature\s+"           # feature
        r"([\w\d]{4})"          # name
        r"\s*{"                 # {
        )

# used for finding the content of features.
# this regular expression will be compiled
# for each feature name found.
featureContentRE = [
        r"([\s;\{\}]|^)",       # whitepace, ; {, } or start of line
        r"feature\s+",          # feature
        # feature name         # name
        r"\s*\{",               # {
        r"([\S\s]*?)",          # content
        r"}\s*",                # }
        # feature name         # name
        r"\s*;"                 # ;
        ]

# used for finding all lookup names.
lookup_findAll_RE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"lookup\s+"            # lookup
        r"([\w\d_.]+)"          # name
        r"\s*{"                 # {
        )

# used for finding the content of lookups.
# this regular expression will be compiled
# for each lookup name found.
lookupContentRE = [
        r"([\s;\{\}]|^)",       # whitepace, ; {, } or start of line
        r"lookup\s+",           # lookup
        # lookup name          # name
        r"\s*\{",               # {
        r"([\S\s]*?)",          # content
        r"}\s*",                # }
        # lookup name          # name
        r"\s*;"                 # ;
        ]

# used for finding all table names.
table_findAll_RE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"table\s+"             # table
        r"([\w\d/]+)"        # name
        r"\s*{"                 # {
        )

# used for finding the content of tables.
# this regular expression will be compiled
# for each table name found.
tableContentRE = [
        r"([\s;\{\}]|^)",       # whitepace, ; {, } or start of line
        r"table\s+",            # feature
        # table name           # name
        r"\s*\{",               # {
        r"([\S\s]*?)",          # content
        r"}\s*",                # }
        # table name           # name
        r"\s*;"                 # ;
        ]

# used for getting tag value pairs from tables.
tableTagValueRE = re.compile(
    r"([\w\d_.]+)"       # tag
    r"\s+"               #
    r"([^;]+)"           # anything but ;
    r";"                 # ;
)

# used for finding all class definitions.
classDefinitionRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"@"                    # @
        r"([\w\d_.]+)"          # name
        r"\s*=\s*"              #  =
        r"\["                   # [
        r"([\w\d\s\-_.@]+)"     # content
        r"\]"                   # ]
        r"\s*;"                 # ;
        , re.M
        )

# used for getting the contents of a class definition
classContentRE = re.compile(
        r"([\w\d\-_.@]+)"
        )

# used for finding inline classes within a sequence
sequenceInlineClassRE = re.compile(
        r"\["                   # [
        r"([\w\d\s_.@]+)"       # content
        r"\]"                   # ]
        )

# used for finding all substitution type 1
subType1And2And4RE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"substitute|sub\s+"    # sub
        r"([\w\d\s_.@\[\]]+)"   # target
        r"\s+by\s+"             #  by
        r"([\w\d\s_.@\[\]]+)"   # replacement
        r"\s*;"                 # ;
        )

# used for finding all substitution type 3
subType3RE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"substitute|sub\s+"    # sub
        r"([\w\d\s_.@\[\]]+)"   # target
        r"\s+from\s+"           #  from
        r"([\w\d\s_.@\[\]]+)"   # replacement
        r"\s*;"                 # ;
        )

# used for finding all ignore substitution type 6
ignoreSubType6RE = re.compile(
        r"([\s;\{\}]|^)"                          # whitepace, ; {, } or start of line
        r"ignore\s+substitute|ignore\s+sub\s+"    # ignore sub
        r"([\w\d\s_.@\[\]']+)"                    # preceding context, target, trailing context
        r"\s*;"                                   # ;
        )

# used for finding all substitution type 6
# XXX see failing unit test
subType6RE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"substitute|sub\s+"    # sub
        r"([\w\d\s_.@\[\]']+)"  # preceding context, target, trailing context
        r"\s+by\s+"             #  by
        r"([\w\d\s_.@\[\]]+)"   # replacement
        r"\s*;"                 # ;
        )

subType6TargetRE = re.compile(
        r"(\["                  # [
        r"[\w\d\s_.@]+"         # content
        r"\]"                   # ]'
        r"|"                    # <or>
        r"[\w\d_.@]+)'"         # content
        )

subType6TargetExtractRE = re.compile(
        r"([\w\d_.@]*)"       # glyph or class names
        )

# used for finding positioning type 1
posType1RE = re.compile(
    r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
    r"position|pos\s+"      # pos
    r"([\w\d\s_.@\[\]]+)"   # target
    r"\s+<"                 # <
    r"([-\d\s]+)"           # value
    r"\s*>\s*;"             # >;
    )

# used for finding positioning type 2
posType2RE = re.compile(
    r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
    r"(enum\s+|\s*)"        # enum
    r"(position|pos\s+)"    # pos
    r"([-\w\d\s_.@\[\]]+)"  # left, right, value
    r"\s*;"                 # ;
    )

# used for finding all languagesystem
languagesystemRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"languagesystem\s+"    # languagesystem
        r"([\w\d]+)"            # script tag
        r"\s+"                  #
        r"([\w\d]+)"            # language tag
        r"\s*;"                 # ;
        )

# use for finding all script
scriptRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"script\s+"            # script
        r"([\w\d]+)"            # script tag
        r"\s*;"                 # ;
        )

# used for finding all language
languageRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"language\s+"          # language
        r"([\w\d]+)"            # language tag
        r"\s*"                  #
        r"([\w\d]*)"            # include_dflt or exclude_dflt or nothing
        r"\s*;"                 # ;
        )

# use for finding all includes
includeRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"include\s*"           # include
        r"\(\s*"                # (
        r"([^\)]+)"             # anything but )
        r"\s*\)"                # )
        r"\s*;{0,1}"            # ; which will occur zero or one times (ugh!)
        )

# used for finding subtable breaks
subtableRE = re.compile(
    r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
    r"subtable\s*"          # subtable
    r"\s*;"                 # ;
)

# used for finding feature references
featureReferenceRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"feature\s+"           # feature
        r"([\w\d]{4})"          # name
        r"\s*;"                 # {
        )

# used for finding lookup references
lookupReferenceRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"lookup\s+"            # lookup
        r"([\w\d]+)"            # name
        r"\s*;"                 # {
        )

# use for finding all lookup flags
lookupflagRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"lookupflag\s+"        # lookupflag
        r"([\w\d,\s]+)"         # values
        r"\s*;"                 # ;
        )

# used for finding all stylistic set featureNames.
featureNamesRE = re.compile(
        r"([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        r"featureNames"         # featureNames
        r"[\S\s]*?}\s*;"        # everything up until }; with whitespace
        )


def _parseUnknown(writer, text):
    text = text.strip()
    ## extract all table names
    tableNames = table_findAll_RE.findall(text)
    for precedingMark, tableName in tableNames:
        # a regular expression specific to this lookup must
        # be created so that nested lookups are safely handled
        thisTableContentRE = list(tableContentRE)
        thisTableContentRE.insert(2, tableName)
        thisTableContentRE.insert(6, tableName)
        thisTableContentRE = re.compile("".join(thisTableContentRE))
        found = thisTableContentRE.search(text)
        tableText = found.group(2)
        start, end = found.span()
        precedingText = text[:start]
        if precedingMark:
            precedingText += precedingMark
        _parseUnknown(writer, precedingText)
        _parseTable(writer, tableName, tableText)
        text = text[end:]
    ## extract all feature names
    featureTags = feature_findAll_RE.findall(text)
    for precedingMark, featureTag in featureTags:
        # a regular expression specific to this lookup must
        # be created so that nested lookups are safely handled
        thisFeatureContentRE = list(featureContentRE)
        thisFeatureContentRE.insert(2, featureTag)
        thisFeatureContentRE.insert(6, featureTag)
        thisFeatureContentRE = re.compile("".join(thisFeatureContentRE))
        found = thisFeatureContentRE.search(text)
        featureText = found.group(2)
        start, end = found.span()
        precedingText = text[:start]
        if precedingMark:
            precedingText += precedingMark
        _parseUnknown(writer, precedingText)
        _parseFeature(writer, featureTag, featureText)
        text = text[end:]
    ## extract all lookup names
    lookupNames = lookup_findAll_RE.findall(text)
    for precedingMark, lookupName in lookupNames:
        # a regular expression specific to this lookup must
        # be created so that nested lookups are safely handled
        thisLookupContentRE = list(lookupContentRE)
        thisLookupContentRE.insert(2, lookupName)
        thisLookupContentRE.insert(6, lookupName)
        thisLookupContentRE = re.compile("".join(thisLookupContentRE))
        found = thisLookupContentRE.search(text)
        lookupText = found.group(2)
        start, end = found.span()
        precedingText = text[:start]
        if precedingMark:
            precedingText += precedingMark
        _parseUnknown(writer, precedingText)
        _parseLookup(writer, lookupName, lookupText)
        text = text[end:]
    ## extract all class data
    classes = classDefinitionRE.findall(text)
    for precedingMark, className, classContent in classes:
        text = _executeSimpleSlice(precedingMark, text, classDefinitionRE, writer)
        className = "@" + className
        _parseClass(writer, className, classContent)
    ## extract substitutions
    # sub type 1 and 4
    subType1s = subType1And2And4RE.findall(text)
    for precedingMark, target, replacement in subType1s:
        text = _executeSimpleSlice(precedingMark, text, subType1And2And4RE, writer)
        _parseSubType1And2And4(writer, target, replacement)
    # sub type 3
    subType3s = subType3RE.findall(text)
    for precedingMark, target, replacement in subType3s:
        text = _executeSimpleSlice(precedingMark, text, subType3RE, writer)
        _parseSubType3(writer, target, replacement)
    # sub type 6
    subType6s = subType6RE.findall(text)
    for precedingMark, target, replacement in subType6s:
        text = _executeSimpleSlice(precedingMark, text, subType6RE, writer)
        _parseSubType6(writer, target, replacement)
    # ignore sub type 6
    ignoreSubType6s = ignoreSubType6RE.findall(text)
    for precedingMark, target in ignoreSubType6s:
        text = _executeSimpleSlice(precedingMark, text, ignoreSubType6RE, writer)
        _parseSubType6(writer, target, replacement=None, ignore=True)
    ## extract positions
    # pos type 1
    posType1s = posType1RE.findall(text)
    for precedingMark, target, value in posType1s:
        text = _executeSimpleSlice(precedingMark, text, posType1RE, writer)
        _parsePosType1(writer, target, value)
    # pos type 2
    posType2s = posType2RE.findall(text)
    for precedingMark, enumTag, posTag, targetAndValue in posType2s:
        text = _executeSimpleSlice(precedingMark, text, posType2RE, writer)
        _parsePosType2(writer, targetAndValue, needEnum=enumTag.strip())
    ## extract other data
    # XXX look at FDK spec. sometimes a language tag of dflt will be passed
    # it should be handled differently than the other tags.
    # languagesystem
    languagesystems = languagesystemRE.findall(text)
    for precedingMark, scriptTag, languageTag in languagesystems:
        text = _executeSimpleSlice(precedingMark, text, languagesystemRE, writer)
        writer.languageSystem(languageTag, scriptTag)
    # script
    scripts = scriptRE.findall(text)
    for precedingMark, scriptTag in scripts:
        text = _executeSimpleSlice(precedingMark, text, scriptRE, writer)
        writer.script(scriptTag)
    # language
    languages = languageRE.findall(text)
    for precedingMark, languageTag, otherKeyword in languages:
        text = _executeSimpleSlice(precedingMark, text, languageRE, writer)
        if not otherKeyword or otherKeyword == "include_dflt":
            writer.language(languageTag)
        elif otherKeyword == "exclude_dflt":
            writer.language(languageTag, includeDefault=False)
    # include
    inclusions = includeRE.findall(text)
    for precedingMark, path in inclusions:
        text = _executeSimpleSlice(precedingMark, text, includeRE, writer)
        writer.include(path)
    # feature reference
    featureReferences = featureReferenceRE.findall(text)
    for precedingMark, featureTag in featureReferences:
        text = _executeSimpleSlice(precedingMark, text, featureReferenceRE, writer)
        writer.featureReference(featureTag)
    # lookup reference
    lookupReferences = lookupReferenceRE.findall(text)
    for precedingMark, lookupName in lookupReferences:
        text = _executeSimpleSlice(precedingMark, text, lookupReferenceRE, writer)
        writer.lookupReference(lookupName)
    # lookupflag
    lookupflags = lookupflagRE.findall(text)
    for precedingMark, lookupflagValues in lookupflags:
        text = _executeSimpleSlice(precedingMark, text, lookupflagRE, writer)
        _parseLookupFlag(writer, lookupflagValues)
    # subtable break
    subtables = subtableRE.findall(text)
    for precedingMark in subtables:
        text = _executeSimpleSlice(precedingMark, text, subtableRE, writer)
        writer.subtableBreak()
    ## extract all featureNames
    featureNames = featureNamesRE.findall(text)
    for precedingMark in featureNames:
        text = _executeSimpleSlice(precedingMark, text, featureNamesRE, writer)
    # empty instructions
    terminators = terminatorRE.findall(text)
    for terminator in terminators:
        text = _executeSimpleSlice(None, text, terminatorRE, writer)
        writer.rawText(terminator)
    text = text.strip()
    if text:
        raise FeaToolsParserSyntaxError("Invalid Syntax: %s" % text)

def _executeSimpleSlice(precedingMark, text, regex, writer):
    first = regex.search(text)
    start, end = first.span()
    precedingText = text[:start]
    if precedingMark:
        precedingText += precedingMark
    _parseUnknown(writer, precedingText)
    text = text[end:]
    return text

def _parseFeature(writer, name, feature):
    featureWriter = writer.feature(name)
    parsed = _parseUnknown(featureWriter, feature)

def _parseLookup(writer, name, lookup):
    lookupWriter = writer.lookup(name)
    parsed = _parseUnknown(lookupWriter, lookup)

def _parseTable(writer, name, table):
    tagValueTables = ["GDEF", "head", "hhea", "OS/2", "vhea"]
    # skip unknown tables
    if name not in tagValueTables:
        return
    _parseTagValueTable(writer, name, table)

def _parseTagValueTable(writer, name, table):
    valueTypes = {
        "GDEF" : {
            "GlyphClassDef" : str
        },
        "head" : {
            "FontRevision" : float
        },
        "hhea" : {
            "CaretOffset" : float,
            "Ascender"    : float,
            "Descender"   : float,
            "LineGap"     : float,
        },
        "OS/2" : {
            "FSType"        : int,
            "Panose"        : "listOfInts",
            "UnicodeRange"  : "listOfInts",
            "CodePageRange" : "listOfInts",
            "TypoAscender"  : float,
            "TypoDescender" : float,
            "TypoLineGap"   : float,
            "winAscent"     : float,
            "winDescent"    : float,
            "XHeight"       : float,
            "CapHeight"     : float,
            "WeightClass"   : float,
            "WidthClass"    : float,
            "Vendor"        : str
        },
        "vhea" : {
            "VertTypoAscender"  : float,
            "VertTypoDescender" : float,
            "VertTypoLineGap"   : float
        }
    }
    tableTypes = valueTypes[name]
    parsedTagValues = []
    for tag, value in tableTagValueRE.findall(table):
        tag = tag.strip()
        value = value.strip()
        if tag not in tableTypes:
            raise FeaToolsParserSyntaxError("Unknown Tag: %s" % tag)
        desiredType = tableTypes[tag]
        if desiredType == "listOfInts":
            v = []
            for line in value.splitlines():
                for i in line.split():
                    v.append(i)
            value = v
            values = []
            for i in value:
                try:
                    i = int(i)
                    values.append(i)
                except ValueError:
                    raise FeaToolsParserSyntaxError("Invalid Syntax: %s" % i)
            value = values
        elif not isinstance(value, desiredType):
            try:
                value = desiredType(value)
            except ValueError:
                raise FeaToolsParserSyntaxError("Invalid Syntax: %s" % i)
        parsedTagValues.append((tag, value))
    writer.table(name, parsedTagValues)

def _parseClass(writer, name, content):
    content = classContentRE.findall(content)
    writer.classDefinition(name, content)

def _parseSequence(sequence):
    parsed = []
    for content in sequenceInlineClassRE.findall(sequence):
        first = sequenceInlineClassRE.search(sequence)
        start, end = first.span()
        precedingText = sequence[:start]
        parsed.extend(_parseSequence(precedingText))
        parsed.append(_parseSequence(content))
        sequence = sequence[end:]
    content = [i for i in sequence.split(" ") if i]
    parsed.extend(content)
    return parsed

def _parseSubType1And2And4(writer, target, replacement):
    target = _parseSequence(target)
    replacement = _parseSequence(replacement)
    if len(target) > 1 and len(replacement) > 1:
        raise FeaToolsParserSyntaxError("many to many replacement are not allowed")
    if len(target) == 1 and len(replacement) == 1:
        # replacement will always be one item.
        # either a single glyph/class or a list
        # reresenting an inline class.
        target = target[0]
        replacement = replacement[0]
        writer.gsubType1(target, replacement)
    elif len(replacement) == 1:
        # target will always be a list representing a sequence.
        # the list may contain strings representing a single
        # glyph/class or a list representing an inline class.
        replacement = replacement[0]
        writer.gsubType4(target, replacement)
    else:
        target = target[0]
        writer.gsubType2(target, replacement)

def _parseSubType3(writer, target, replacement):
    # target will only be one item representing
    # a glyph/class name.
    target = classContentRE.findall(target)
    target = target[0]
    replacement = classContentRE.findall(replacement)
    writer.gsubType3(target, replacement)

def _parseSubType6(writer, target, replacement=None, ignore=False):
    # replacement will always be one item.
    # either a single glyph/class or a list
    # representing an inline class.
    # the only exception to this is if
    # this is an ignore substitution.
    # in that case, replacement will
    # be None.
    if not ignore:
        replacement = classContentRE.findall(replacement)
        if len(replacement) == 1:
            replacement = replacement[0]
    #
    targetText = target
    #
    precedingContext = ""
    targets = subType6TargetRE.findall(targetText)
    trailingContext = ""
    #
    targetCount = len(targets)
    counter = 1
    extractedTargets = []
    for target in targets:
        first = subType6TargetRE.search(targetText)
        start, end = first.span()
        if counter == 1:
            precedingContext = _parseSequence(targetText[:start])
        if counter == targetCount:
            trailingContext = _parseSequence(targetText[end:])
        # the target could be in a form like [o o.alt]
        # so it has to be broken down
        target = classContentRE.findall(target)
        if len(target) == 1:
            target = target[0]
        extractedTargets.append(target)
        counter += 1
        targetText = targetText[end:]
    writer.gsubType6(precedingContext, extractedTargets, trailingContext, replacement)

def _parsePosType1(writer, target, value):
    # target will only be one item representing
    # a glyph/class name
    value = tuple([float(i) for i in value.strip().split(" ")])
    writer.gposType1(target, value)

def _parsePosType2(writer, targetAndValue, needEnum=False):
    # the target and value will be coming
    # in as single string.
    target = " ".join(targetAndValue.split(" ")[:-1])
    value = targetAndValue.split(" ")[-1]
    # XXX this could cause a choke
    value = float(value)
    target = _parseSequence(target)
    writer.gposType2(target, value, needEnum)

def _parseLookupFlag(writer, values):
    values = values.replace(",", " ")
    values = [i for i in values.split(" ") if i]
    # lookupflag format B is not supported except for value 0
    if len(values) == 1:
        try:
            v = int(values[0])
            if v != 0:
                raise FeaToolsParserSyntaxError("lookupflag format B is not supported for any value other than 0")
            else:
                writer.lookupFlag()
                return
        except ValueError:
            pass
    rightToLeft = False
    ignoreBaseGlyphs = False
    ignoreLigatures = False
    ignoreMarks = False
    possibleValues = ["RightToLeft", "IgnoreBaseGlyphs", "IgnoreLigatures", "IgnoreMarks"]
    for value in values:
        if value not in possibleValues:
            raise FeaToolsParserSyntaxError("Unknown lookupflag value: %s" % value)
        if value == "RightToLeft":
            rightToLeft = True
        elif value == "IgnoreBaseGlyphs":
            ignoreBaseGlyphs = True
        elif value == "IgnoreLigatures":
            ignoreLigatures = True
        elif value == "IgnoreMarks":
            ignoreMarks = True
    writer.lookupFlag(rightToLeft=rightToLeft, ignoreBaseGlyphs=ignoreBaseGlyphs, ignoreLigatures=ignoreLigatures, ignoreMarks=ignoreMarks)

def parseFeatures(writer, text):
    # strip the strings.
    # (an alternative approach would be to escape the strings.
    # the problem is that a string could contain parsable text
    # that would fool the parsing algorithm.)
    text = stringRE.sub(r"", text)
    # strip the comments
    text = commentRE.sub(r"", text)
    # make sure there is a space after all ;
    # since it makes the text more digestable
    # for the regular expressions
    text = terminatorRE.sub(r"; ", text)
    _parseUnknown(writer, text)
