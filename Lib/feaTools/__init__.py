"""
Tools for reading and writing FDK syntax OpenType feature definitions.
Warning:
This is relatively stable, but the API could change.
Not all of the FDK syntax is supported yet.

------
USAGE:
------

Parsing uses a concept similar to the FontTools/RoboFab pen concept.
You create a "writer" object and pass that, along with the text to parse,
to a parser function. For example, to output FDK syntax from a file
(Yes, I know this is a silly example):

    writer = FDKSyntaxFeatureWriter()
    parseFeatures(myFeatureText, writer)
    myNewFeatureText = writer.write()

Writers can be used inpendently of the parse function:

    writer = FDKSyntaxFeatureWriter()
    saltWriter = writer.feature("salt")
    saltWriter.classDefinition("@A", ["A", "A.alt"])
    saltWriter.gsubType1("@A", "A.alt2")
    myFeatureText = writer.write()

------
TO DO:
------

Parser:
- need tests:
  classes
  languagesystem
  language
- gsub type 6 needs to support the future format
  sub f' o o b" a r by f.alt, b.alt;
  perhaps this could be done by returning a list
  of tuples:
  [(precede, target, trail), (precede, target, trail)]
  [(None, [f], [o, o]), (None, [b], [a, r])]
  along with a list of matching replacements
  [replacement1, replacement2]
  [f.alt, b.alt]
  better idea:
  always return a multiple of three
  1 = precede 2 = target 3 = trail, etc.
  ([], [f], [o, o], [], [b], [a, r])
  even better idea:
  make no distincition about precede, target and trail
  (context, target, context, target, context, ...)
  ([], [f], [o, o], [b], [a, r])
- lookupflag format b - how are the numbers calculated?
- useExtension
- check on dflt
- future gpos formats
- size
- ranges for class definition
- need to throw up a meaningful error for bad syntax

Writer:
- write tests
"""