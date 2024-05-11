import pytest
from src.mcfg_parser.tree import MCFGTree
from typing import Set
from src.mcfg_parser.grammar import MCFGRuleElement, MCFGRule, MCFGRuleElementInstance, MCFGGrammar
#test continuous_tree
def test_mcftree_basic():
    # Simple tree creation
    tree = MCFGTree('S', [(0, 6)], [
        MCFGTree('NP', [(0, 3)], []),
        MCFGTree('VP', [(4, 6)], [])
    ])
    assert tree.data == 'S'
    assert tree.spans == [(0, 6)]
    assert len(tree.children) == 2

    # Verify string representation
    expected_str = """S (spans: [(0, 6)])"""

    # Verify equality and hashing
    tree_clone = MCFGTree('S', [(0, 6)], [        MCFGTree('NP', [(0, 3)], []),
        MCFGTree('VP', [(4, 6)], [])
    ])
    assert tree == tree_clone
    assert hash(tree) == hash(tree_clone)

    # Ensure inequality with a different structure
    different_tree = MCFGTree('S', [(0, 6)], [        MCFGTree('NP', [(0, 3)], []),
        MCFGTree('VP', [(3, 6)], [])
    ])
    assert tree != different_tree

def test_mcftree_from_list():
    # Test from_list method
    tree = MCFGTree.from_list(['S', ['NP'], ['VP']])
    assert tree.data == 'S'
    assert len(tree.children) == 2
    assert tree.children[0].data == 'NP'
    assert tree.children[1].data == 'VP'


#test_discontinous_tree
def test_discontinuous_tree():
    # Define the rule
    rule = MCFGRule.from_string('A(w1u, x1v) -> B(w1, x1) C(u, v)')

    # Instantiate the left side with discontinuous spans
    instantiated = rule.instantiate_left_side(
        MCFGRuleElementInstance("B", (1, 2), (5, 7)),
        MCFGRuleElementInstance("C", (2, 4), (7, 8))
    )

    # Create a tree using the instantiated left side
    tree = MCFGTree(
        instantiated.variable,  # 'A'
        list(instantiated.string_spans),  # [(1, 4), (5, 8)]
        [
            MCFGTree("B", [(1, 2), (5, 7)], []),
            MCFGTree("C", [(2, 4), (7, 8)], [])
        ]
    )

    # Verify the properties of the tree
    assert tree.data == 'A'
    assert tree.spans == [(1, 4), (5, 8)]
    assert len(tree.children) == 2

    # Verify string representation
    expected_str = """A (spans: [(1, 4), (5, 8)])
  --B (spans: [(1, 2), (5, 7)])
  --C (spans: [(2, 4), (7, 8)])
    """
    tree_str = tree.to_string().strip()
    expected_str = expected_str.strip()
    assert tree_str == expected_str
    print("Test passed!")

