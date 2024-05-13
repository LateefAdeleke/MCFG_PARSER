
# MCFG_Parser: An Agender-based Parser Package for MCFG

## Overview
MCFG_Parser is a python package designed for parsing natural languages using multiple context_free grammars (MCFGs). It implements an agenda_based parser to efficiently handle complex syntactic structures such as discontinuous categories observed in human langugage. This project leverages agenda_based parser formalism as contained in Shieber et al. 1995 and utilizes inference rules laid out in Kallmeyer 2013, making it relevant for academic research and applications in computational linguistics.

## Features
-- Parsing with MCFGs to handle discontinous syntactic dependencies
-- Agenda_based parser for efficient syntactic parsing
-- Deductive parsing
-- Comprehensive test suite ensuring robustness and reliability

## Installation
Follow this steps to install MCFG_Parser:

1. Clone the repository: 
git clone https://github.com/LateefAdeleke/MCFG_PARSER_LATEEF.git

2. Navigate to the project directory: cd "MCFG_Parser"

3. Install the package: pip install MCFG_Parser

##Environments

| Package | Version |
| ------- | ------- |
| iniconfig | 2.0.0 |
| packaging | 24.0 |
| pluggy | 1.5.0 |
| pytest | 8.2.0 |
## Usage
Here is how you can use MCFG_Parser to parse sentence:
from MCFG_Parser.parser import MCFGGrammarParser
from MCFG_Parser.grammar import MCFGGrammar, MCFGRule, MCFGRuleElement, MCFGRuleElementInstance
from MCFG_Parser.tree import tree

# Load the grammar
grammar = MCFGGrammar(grammar_rule, 'S')

# Initialize the parser with the loaded grammar
parser = MCFGGrammarParser(grammar)

Example for parsing a sentence: 
parser = MCFGGrammarParser(grammar)
    sentence = ['the', 'greyhound', 'believes']
    parse_tree = parser.parse(sentence)
    assert parse_tree is not None 
    

## Contributing
Contributions to MCFG_Parser are welcome! Here are a few ways you can help:

Report bugs and issues on the GitHub issues page.
Suggest new features or improvements.
Improve the documentation.
Submit pull requests with bug fixes or new features.
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to Shieber et al. 1995 and Kallmeyer 2013 for the foundational concepts and methodologies utilized in this project.
Special thanks to Aaron for an amazing introduction to computational linguistics.
Big thanks to Daniel Chaves, who we worked together on this project.
## Contact
ladeleke@ur.rochester.edu
