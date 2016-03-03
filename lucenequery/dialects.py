from .StandardLuceneGrammarLexer import StandardLuceneGrammarLexer
from .StandardLuceneGrammarListener import StandardLuceneGrammarListener
from .StandardLuceneGrammarParser import StandardLuceneGrammarParser
from .ElasticsearchGrammarLexer import ElasticsearchGrammarLexer
from .ElasticsearchGrammarListener import ElasticsearchGrammarListener
from .ElasticsearchGrammarParser import ElasticsearchGrammarParser
from collections import namedtuple

Dialect = namedtuple('Dialect', ['lexer', 'listener', 'parser'])

standard = Dialect(
    lexer=StandardLuceneGrammarLexer,
    listener=StandardLuceneGrammarListener,
    parser=StandardLuceneGrammarParser,
)

elasticsearch = Dialect(
    lexer=ElasticsearchGrammarLexer,
    listener=ElasticsearchGrammarListener,
    parser=ElasticsearchGrammarParser,
)
