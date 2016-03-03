import antlr4


def parse(query, dialect=None):
    if dialect is None:
        from . import dialects
        dialect = getattr(dialects, 'standard')
    lexer = dialect.lexer(antlr4.InputStream(query))
    stream = antlr4.CommonTokenStream(lexer)
    parser = dialect.parser(stream)
    parser._errHandler = antlr4.BailErrorStrategy()
    tree = parser.mainQ()
    return tree.clause
