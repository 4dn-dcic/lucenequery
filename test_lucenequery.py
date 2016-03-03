import pytest
import json
import os.path
here = os.path.abspath(os.path.dirname(__file__))
string_trees = json.load(open(os.path.join(here, 'string_trees.json')))


@pytest.fixture(params=['standard', 'elasticsearch'])
def dialect(request):
    from lucenequery import dialects
    return getattr(dialects, request.param)


@pytest.mark.parametrize(['query', 'result'], [
    (query, result)
    for entry, tests in string_trees.items()
    for query, result in tests.items()
    if type(result) is type(u'')
])
def test_string_tree(dialect, query, result):
    from lucenequery import parse
    clause = parse(query, dialect=dialect)
    assert clause.getText() == query.strip()
    # `result` is the antlr3 rewritten tree, so just check it parses for now.
    clause.toStringTree(recog=clause.parser)


@pytest.mark.parametrize('query', [
    query
    for entry, tests in string_trees.items()
    for query, result in tests.items()
    if result is False
])
def test_parse_fail(dialect, query):
    from antlr4 import IllegalStateException
    from lucenequery import parse
    with pytest.raises(IllegalStateException):
        parse(query, dialect=dialect)


@pytest.mark.parametrize('query', [
    query
    for entry, tests in string_trees.items()
    for query, result in tests.items()
    if result is True
])
def test_parse_ok(dialect, query):
    from lucenequery import parse
    clause = parse(query, dialect=dialect)
    assert clause.getText() == query.strip()


@pytest.mark.parametrize('query', [
    'age:<10',
    'age:>10',
    'age:<=10',
    'age:>=10',

])
def test_one_sided_range(query):
    from lucenequery import parse
    from lucenequery import dialects
    clause = parse(query, dialect=dialects.elasticsearch)
    assert clause.getText() == query


@pytest.mark.parametrize(['query', 'expect'], [
    ('foo:bar', 'prefix.foo:bar'),
    ('foo:bar baz', 'prefix.foo:bar baz'),
    ('foo:bar AND (a:b OR c:d)',
     'prefix.foo:bar AND (prefix.a:b OR prefix.c:d)'),
])
def test_prefixfields(dialect, query, expect):
    from lucenequery import dialects
    from lucenequery.prefixfields import prefixfields
    clause = prefixfields('prefix.', query, dialect=dialects.elasticsearch)
    assert clause.getText() == expect
