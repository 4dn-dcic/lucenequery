// jrunscript -cp "/usr/local/Cellar/elasticsearch/1.7.2/libexec/lucene-queryparser-4.10.4.jar:/usr/local/Cellar/elasticsearch/1.7.2/libexec/lucene-core-4.10.4.jar" -f test_java_queryparser.js

function openJsonFile(path) {
    var data = java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(path));
    var str = new java.lang.String(data, 'utf-8');
    return JSON.parse(str);
}

qp = new org.apache.lucene.queryparser.flexible.standard.StandardQueryParser()
qp.setAllowLeadingWildcard(true);

var examples = openJsonFile('test_java_queryparser_examples.json')

var failures = 0;
var results = {};
for (var query in examples) {
    var expect = examples[query];
    var result;
    try {
        result = qp.parse(query, '_all').toString();
    } catch (exc) {
        result = null;
    }
    results[query] = result;
    if (result !== expect) {
        print('FAIL ' + JSON.stringify(query) + ' GOT ' + JSON.stringify(result) + ' EXPECTED ' + JSON.stringify(expect));
        failures++;
    }
}

print('Ran ' + Object.keys(examples).length + ' tests, ' + failures + ' failed.');

if (failures) {
    print(JSON.stringify(results, null, 4));
    throw 'failed';
}
