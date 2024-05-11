import pytest
from src.mcfg_parser.grammar import MCFGRuleElement, MCFGRule, MCFGRuleElementInstance, MCFGGrammar

#MCFGRuleElement
def test_rule_element_init():
    element = MCFGRuleElement('VP', (0,), (1,))
    assert element.variable == 'VP'
    assert element.string_variables == ((0,), (1,))
    assert str(element) == 'VP(0, 1)'
def test_rule_element_str():
    element = MCFGRuleElement('NP', (0,))
    assert str(element) == 'NP(0)'

def test_rule_element_eq():
    elem1 = MCFGRuleElement('NP', (0,))
    elem2 = MCFGRuleElement('NP', (0,))
    elem3 = MCFGRuleElement('VP', (0,))
    assert elem1 == elem2
    assert elem1 != elem3

def test_rule_element_to_tuple():
    element = MCFGRuleElement('VP', (0,), (1,))
    assert element.to_tuple() == ('VP', ((0,), (1,)))

def test_rule_element_unique_string_variables():
    element = MCFGRuleElement('VP', (0,), (1,), (2, 3))
    assert element.unique_string_variables == {0, 1, 2, 3}

#MCFGRuleElementInstance
def test_rule_element_instance_init():
    instance = MCFGRuleElementInstance('VP', (0, 1), (2, 3))
    assert instance.variable == 'VP'
    assert instance.string_spans == ((0, 1), (2, 3))

def test_rule_element_instance_str():
    instance = MCFGRuleElementInstance('NP', (0,))
    assert str(instance) == 'NP([0])'

def test_rule_element_instance_eq():
    inst1 = MCFGRuleElementInstance('VP', (0, 1), (2, 3))
    inst2 = MCFGRuleElementInstance('VP', (0, 1), (2, 3))
    inst3 = MCFGRuleElementInstance('NP', (0,))
    assert inst1 == inst2
    assert inst1 != inst3

def test_rule_element_instance_to_tuple():
    instance = MCFGRuleElementInstance('VP', (0, 1), (2, 3))
    assert instance.to_tuple() == ('VP', ((0, 1), (2, 3)))

#MCFGRule Tests
def test_rule_init():
    left = MCFGRuleElement('S', (0,), (1,))
    right1 = MCFGRuleElement('NP', (0,))
    right2 = MCFGRuleElement('VP', (1,))
    rule = MCFGRule(left, right1, right2)
    assert rule.left_side == left
    assert rule.right_side == (right1, right2)

def test_rule_eq():
    rule1 = MCFGRule.from_string('S(uv) -> NP(u) VP(v)')
    rule2 = MCFGRule.from_string('S(uv) -> NP(u) VP(v)')
    rule3 = MCFGRule.from_string('S(uv) -> VP(u) NP(v)')
    assert rule1 == rule2
    assert rule1 != rule3

def test_rule_instantiate_left_side():
    rule = MCFGRule.from_string('S(uv) -> NP(u) VP(v)')
    left_instance = rule.instantiate_left_side(
        MCFGRuleElementInstance('NP', (0, 1)),
        MCFGRuleElementInstance('VP', (1, 2))
    )
    assert str(left_instance) == 'S([0, 2])'

#MCFGGrammar
def test_mcfg_rule_creation():
    """Test if an MCFG rule can be created and is correctly formatted."""
    left_side = MCFGRuleElement('S', (0,), (1,), (2,))
    np_disloc_element = MCFGRuleElement('NPdisloc', (0,), (2,))
    vp_element = MCFGRuleElement('VP', (1,))
    rule = MCFGRule(left_side, np_disloc_element, vp_element)
    assert str(rule) == 'S(0, 1, 2) -> NPdisloc(0, 2) VP(1)'

def test_mcfg_grammar_creation():
    """Test if an MCFG grammar can be created with multiple rules."""
    rules = [
        MCFGRule(MCFGRuleElement('S', (0,), (1,)), MCFGRuleElement('NP', (0,)), MCFGRuleElement('VP', (1,))),
        MCFGRule(MCFGRuleElement('VP', (0,), (1,)), MCFGRuleElement('V', (0,)), MCFGRuleElement('NP', (1,)))
    ]
    grammar = MCFGGrammar(rules, 'S')
    assert grammar._start_symbol == 'S'
    assert len(grammar._rules) == 2


def sample_grammar():
    """Provide a sample MCFG grammar to other test functions."""
    rules = [
        MCFGRule(MCFGRuleElement('S', (0,), (1,)), MCFGRuleElement('NP', (0,)), MCFGRuleElement('VP', (1,))),
        MCFGRule(MCFGRuleElement('VP', (0,), (1,)), MCFGRuleElement('V', (0,)), MCFGRuleElement('NP', (1,)))
    ]
    return MCFGGrammar(rules, 'S')

def test_mcfg_grammar():
    rule1 = MCFGRule(
        MCFGRuleElement('S', (0,), (1,)),
        MCFGRuleElement('NP', (0,)),
        MCFGRuleElement('VP', (1,))
    )

    rule2 = MCFGRule(
        MCFGRuleElement('VP', (0,)),
        MCFGRuleElement('V', (0,))
    )

    grammar = MCFGGrammar([rule1, rule2], 'S')

    # Check starting symbol
    assert grammar.start_symbol == 'S'

    # Check all rules
    all_rules = grammar._rules
    assert len(all_rules) == 2


