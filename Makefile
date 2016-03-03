all: ElasticsearchGrammar StandardLuceneGrammar

StandardLuceneGrammar:
	cd lucenequery && antlr4 StandardLuceneGrammar.g4

ElasticsearchGrammar: StandardLuceneGrammar
	cd lucenequery && antlr4 ElasticsearchGrammar.g4
