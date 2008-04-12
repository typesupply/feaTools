import re


class FeaToolsParserSyntaxError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# used for removing all comments
commentRE = re.compile("#.*")

# used for finding all strings
stringRE = re.compile(
    "\""         # "
    "([^\"]*)"   # anything but "
    "\""         # "
)

# used for removing all comments
terminatorRE = re.compile(";")

# used for finding all feature names.
feature_findAll_RE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "feature\s+"           # feature
        "([\w\d]{4})"          # name
        "\s*{"                 # {
        )

# used for finding the content of features.
# this regular expression will be compiled
# for each feature name found.
featureContentRE = [
        "([\s;\{\}]|^)",       # whitepace, ; {, } or start of line
        "feature\s+",          # feature
        # feature name         # name
        "\s*\{",               # {
        "([\S\s]*)",           # content
        "}\s*",                # }
        # feature name         # name
        "\s*;"                 # ;
        ]

# used for finding all lookup names.
lookup_findAll_RE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "lookup\s+"            # lookup
        "([\w\d_.]+)"          # name
        "\s*{"                 # {
        )

# used for finding the content of lookups.
# this regular expression will be compiled
# for each lookup name found.
lookupContentRE = [
        "([\s;\{\}]|^)",       # whitepace, ; {, } or start of line
        "lookup\s+",           # lookup
        # lookup name          # name
        "\s*\{",               # {
        "([\S\s]*)",           # content
        "}\s*",                # }
        # lookup name          # name
        "\s*;"                 # ;
        ]

# used for finding all table names.
table_findAll_RE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "table\s+"             # table
        "([\w\d]{4})"          # name
        "\s*{"                 # {
        )

# used for finding the content of tables.
# this regular expression will be compiled
# for each table name found.
tableContentRE = [
        "([\s;\{\}]|^)",       # whitepace, ; {, } or start of line
        "table\s+",            # feature
        # table name           # name
        "\s*\{",               # {
        "([\S\s]*)",           # content
        "}\s*",                # }
        # table name           # name
        "\s*;"                 # ;
        ]

# used for finding all class definitions.
classDefinitionRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "@"                    # @
        "([\w\d_.]+)"          # name
        "\s*=\s*"              #  = 
        "\["                   # [
        "([\w\d\s_.@]+)"       # content
        "\]"                   # ]
        "\s*;"                 # ;
        , re.M
        )

# used for getting the contents of a class definition
classContentRE = re.compile(
        "([\w\d_.@]+)"
        )

# used for finding inline classes within a sequence
sequenceInlineClassRE = re.compile(
        "\["                   # [
        "([\w\d\s_.@]+)"       # content
        "\]"                   # ]
        )

# used for finding all substitution type 1
subType1And4RE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "substitute|sub\s+"    # sub
        "([\w\d\s_.@\[\]]+)"   # target
        "\s+by\s+"             #  by
        "([\w\d\s_.@\[\]]+)"   # replacement
        "\s*;"                 # ;
        )

# used for finding all substitution type 3
subType3RE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "substitute|sub\s+"    # sub
        "([\w\d\s_.@\[\]]+)"   # target
        "\s+from\s+"           #  from
        "([\w\d\s_.@\[\]]+)"   # replacement
        "\s*;"                 # ;
        )

# used for finding all substitution type 6
# XXX see failing unit test
subType6RE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "substitute|sub\s+"    # sub
        "([\w\d\s_.@\[\]']+)"  # preceding context, target, trailing context
        "\s+by\s+"             #  by
        "([\w\d\s_.@\[\]]+)"   # replacement
        "\s*;"                 # ;
        )

subType6TargetRE = re.compile(
        "(\["                  # [
        "[\w\d\s_.@]+"         # content
        "\]"                   # ]'
        "|"                    # <or>
        "[\w\d_.@]+)'"         # content
        )

subType6TargetExtractRE = re.compile(
        "([\w\d_.@]*)"       # glyph or class names
        )

# used for finding positioning type 1
posType1RE = re.compile(
    "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
    "position|pos\s+"      # pos
    "([\w\d\s_.@\[\]]+)"   # target
    "\s+<"                 # <
    "([-\d\s]+)"           # value
    "\s*>\s*;"             # >;
    )

# used for finding positioning type 2
posType2RE = re.compile(
    "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
    "(enum\s+|\s*)"        # enum
    "(position|pos\s+)"    # pos
    "([-\w\d\s_.@\[\]]+)"  # left, right, value
    "\s*;"                 # ;
    )

# used for finding all languagesystem
languagesystemRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "languagesystem\s+"    # languagesystem
        "([\w\d]+)"            # script tag
        "\s+"                  #
        "([\w\d]+)"            # language tag
        "\s*;"                 # ;
        )

# use for finding all script
scriptRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "script\s+"            # script
        "([\w\d]+)"            # script tag
        "\s*;"                 # ;
        )

# used for finding all language
languageRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "language\s+"          # language
        "([\w\d]+)"            # language tag
        "\s*"                  # 
        "([\w\d]*)"            # include_dflt or exclude_dflt or nothing
        "\s*;"                 # ;
        )

# use for finding all includes
includeRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "include\s*"           # include
        "\(\s*"                # (
        "([^\)]+)"             # anything but )
        "\s*\)"                # )
        "\s*;{0,1}"            # ; which will occur zero or one times (ugh!)
        )

# used for finding subtable breaks
subtableRE = re.compile(
    "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
    "subtable\s*"          # subtable
    "\s*;"                 # ;
)

# used for finding feature references
featureReferenceRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "feature\s+"           # feature
        "([\w\d]{4})"          # name
        "\s*;"                 # {
        )

# used for finding lookup references
lookupReferenceRE = re.compile(
        "([\s;\{\}]|^)"        # whitepace, ; {, } or start of line
        "lookup\s+"            # lookup
        "([\w\d]+)"            # name
        "\s*;"                 # {
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
    featureNames = feature_findAll_RE.findall(text)
    for precedingMark, featureName in featureNames:
        # a regular expression specific to this lookup must
        # be created so that nested lookups are safely handled
        thisFeatureContentRE = list(featureContentRE)
        thisFeatureContentRE.insert(2, featureName)
        thisFeatureContentRE.insert(6, featureName)
        thisFeatureContentRE = re.compile("".join(thisFeatureContentRE))
        found = thisFeatureContentRE.search(text)
        featureText = found.group(2)
        start, end = found.span()
        precedingText = text[:start]
        if precedingMark:
            precedingText += precedingMark
        _parseUnknown(writer, precedingText)
        _parseFeature(writer, featureName, featureText)
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
    subType1s = subType1And4RE.findall(text)
    for precedingMark, target, replacement in subType1s:
        text = _executeSimpleSlice(precedingMark, text, subType1And4RE, writer)
        _parseSubType1And4(writer, target, replacement)
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
        _parsePosType2(writer, targetAndValue)
    ## extract other data
    # XXX look at FDK spec. sometimes a language tag of dflt will be passed
    # it should be handled differently than the other tags.
    # languagesystem
    languagesystems = languagesystemRE.findall(text)
    for precedingMark, scriptTag, languageTag in languagesystems:
        text = _executeSimpleSlice(precedingMark, text, languagesystemRE, writer)
        writer.languageSystem(scriptTag, languageTag)
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
    for precedingMark, featureName in featureReferences:
        text = _executeSimpleSlice(precedingMark, text, featureReferenceRE, writer)
        writer.featureReference(featureName)
    # lookup reference
    lookupReferences = lookupReferenceRE.findall(text)
    for precedingMark, lookupName in lookupReferences:
        text = _executeSimpleSlice(precedingMark, text, lookupReferenceRE, writer)
        writer.lookupReference(lookupName)
    # subtable
    subtables = subtableRE.findall(text)
    for precedingMark in subtables:
        text = _executeSimpleSlice(precedingMark, text, subtableRE, writer)
        writer.subtableBreak()
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
    # this could parse table secific data.
    # for now, simply ignore the text.
    pass

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

def _parseSubType1And4(writer, target, replacement):
    target = _parseSequence(target)
    # replacement will always be one item.
    # either a single glyph/class or a list
    # reresenting an inline class.
    replacement = _parseSequence(replacement)
    replacement = replacement[0]
    if len(target) == 1:
        target = target[0]
        writer.gsubType1(target, replacement)
    else:
        # target will always be a list representing a sequence.
        # the list may contain strings representing a single
        # glyph/class or a list representing an inline class.
        writer.gsubType4(target, replacement)

def _parseSubType3(writer, target, replacement):
    # target will only be one item representing
    # a glyph/class name.
    target = classContentRE.findall(target)
    target = target[0]
    replacement = classContentRE.findall(replacement)
    writer.gsubType3(target, replacement)

def _parseSubType6(writer, target, replacement):
    # replacement will always be one item.
    # either a single glyph/class or a list
    # reresenting an inline class.
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

def _parsePosType2(writer, targetAndValue):
    # the target and value will be coming
    # in as single string.
    target = " ".join(targetAndValue.split(" ")[:-1])
    value = targetAndValue.split(" ")[-1]
    # XXX this could cause a choke
    value = float(value)
    target = _parseSequence(target)
    writer.gposType2(target, value)

def _parsePosType2WithEnum(writer, targetAndValue):
    # the target and value will be coming
    # in as single string.
    target = " ".join(targetAndValue.split(" ")[:-1])
    value = targetAndValue.split(" ")[-1]
    # XXX this could cause a choke
    value = float(value)
    target = _parseSequence(target)
    writer.gposType2(target, value)

def parseFeatures(writer, text):
    # strip the strings.
    # (an alternative approach would be to escape the strings.
    # the problem is that a string could contain parsable text
    # that would fool the parsing algorithm.)
    text = stringRE.sub("", text)
    # strip the comments
    text = commentRE.sub("", text)
    # make sure there is a space after all ;
    # since it makes the text more digestable
    # for the regular expressions
    text = terminatorRE.sub("; ", text)
    _parseUnknown(writer, text)
