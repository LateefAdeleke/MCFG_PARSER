# tests/test_grammar.py

import pytest
from src.mcfg_parser.grammar import MCFGRule, MCFGRuleElement, MCFGRuleElementInstance

@pytest.fixture
def test_grammar():
    """
    Provides a sample set of grammar rules to test the parser against.
    """
    return [
        'S(uv) -> NP(u) VP(v)',
        'VP(uv) -> Vpres(u) NP(v)',
        'NP(uv) -> D(u) N(v)',
        'D(the)',
        'N(greyhound)'
    ]

def test_rule_element():
    """
    Test the initialization and functionality of MCFGRuleElement.
    """
    elem = MCFGRuleElement('VP', (0,), (1,))
    assert str(elem) == 'VP(0, 1)'

def test_rule_element_instance():
    """
    Test the initialization and functionality of MCFGRuleElementInstance.
    """
    instance = MCFGRuleElementInstance('NP', (0, 2), (1,))
    assert str(instance) == 'NP([0, 2], [1])'

def test_mcfg_rule(test_grammar):
    """
    Test creating and manipulating MCFG rules.
    """
    rule = MCFGRule.from_string(test_grammar[0])
    assert str(rule) == 'S(uv) -> NP(u) VP(v)'
    assert rule.left_side.variable == 'S'
    assert rule.right_side[0].variable == 'NP'
    assert rule.right_side[1].variable == 'VP'
# Additional tests in tests/test_grammar.py

import pytest
from src.mcfg_parser.grammar import MCFGRule, MCFGRuleElement, MCFGRuleElementInstance

def test_empty_rule():
    """
    Test that creating an empty rule raises an appropriate error.
    """
    with pytest.raises(ValueError, match='right side'):
        MCFGRule.from_string('S()')

def test_invalid_format():
    """
    Test that a rule with invalid format raises an appropriate error.
    """
    invalid_rule = 'InvalidRule -> NP(u)'
    with pytest.raises(ValueError, match='variables duplicated'):
        MCFGRule.from_string(invalid_rule)

def test_multiple_non_terminals():
    """
    Test a rule with multiple non-terminals in the right side.
    """
    rule_str = 'S(uv, w) -> NP(u) VP(v) Aux(w)'
    rule = MCFGRule.from_string(rule_str)
    assert str(rule) == 'S(uv, w) -> NP(u) VP(v) Aux(w)'
    assert rule.left_side.variable == 'S'
    assert len(rule.right_side) == 3

def test_epsilon_rule():
    """
    Test an epsilon rule with an empty right-hand side.
    """
    epsilon_rule = 'EmptyRule()'
    rule = MCFGRule.from_string(epsilon_rule)
    assert rule.is_epsilon
    assert str(rule) == 'EmptyRule()'

def test_rule_element_equality():
    """
    Test equality checking for rule elements.
    """
    elem1 = MCFGRuleElement('VP', (0,), (1,))
    elem2 = MCFGRuleElement('VP', (0,), (1,))
    assert elem1 == elem2

    elem3 = MCFGRuleElement('NP', (0,), (1,))
    assert elem1 != elem3

def test_rule_element_instance_span_checking():
    """
    Test span checks for rule element instances.
    """
    instance1 = MCFGRuleElementInstance('NP', (0, 2), (1,))
    instance2 = MCFGRuleElementInstance('NP', (0, 2), (1,))
    instance3 = MCFGRuleElementInstance('VP', (0, 1), (2,))
    
    assert instance1 == instance2
    assert instance1 != instance3
