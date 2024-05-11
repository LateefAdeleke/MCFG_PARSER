
# MCFG_PARSER: An Agender-based Parser Package for MCFG

## Overview
MCFG is a python package designed for parsing natural languages using multiple context_free grammars (MCFGs). It implements an agenda_based parser to efficiently handle complex syntactic structures. This project leverages agenda_based parser formalism nas contained in Shieber et al. 1995 and utilizes inference rules laid out in Kallmeyer 2013, making it relevant to academic research and applications in computational linguistics.

## Features
--Parsing with MCFGs to handle discontinous syntactic dependencies
--Agenda_based parser for efficient syntactic parsing
--Comprehensive test suite ensuring robustness and reliability

## Installation
Follow this steps to install MCFG_PARSER:

1. Clone the repository: 
git clone https://github.com/LateefAdeleke/MCFG_PARSER.git

2. Navigate to the project directory: cd "MCFG_Parser"

3. Install the package: pip install MCFG_PARSER


## Usage
Here is how you can use MCFG_Parser to parse sentence:
from MCFG_Parser.parser import Parser
from MCFG_Parser.grammar import load_grammar

# Load the grammar
grammar = load_grammar('/Users/lateefadeleke/Desktop/MCFG_Parser/src/mcfg_parser/grammar.py')

# Initialize the parser with the loaded grammar
parser = Parser(grammar)

# Parse a sentence
parsed_output = parser.parse("The man that killed the cat loves the dog that barks")
print(parsed_output)

## Contributing
Contributions to MyParser are welcome! Here are a few ways you can help:

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
## Contact
ladeleke@ur.rochester.edu