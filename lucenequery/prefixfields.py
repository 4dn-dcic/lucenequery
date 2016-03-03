from . import parse
from .StandardLuceneGrammarListener import StandardLuceneGrammarListener
import antlr4


class PrefixFieldsListener(StandardLuceneGrammarListener):
    def __init__(self, prefix):
        super(PrefixFieldsListener, self).__init__()
        self.field_prefix = prefix

    def exitField(self, ctx):
        term = ctx.getChild(0)
        term.symbol.text = self.field_prefix + term.symbol.text


def prefixfields(prefix, query, dialect=None):
    clause = parse(query, dialect=dialect)
    walker = antlr4.ParseTreeWalker()
    walker.walk(PrefixFieldsListener(prefix), clause)
    return clause
