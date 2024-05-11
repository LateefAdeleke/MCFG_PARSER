
from src.mcfg_parser.tree import MCFGTree
from src.mcfg_parser.grammar import MCFGRuleElement, MCFGRule, MCFGRuleElementInstance, MCFGGrammar
from typing import List, Tuple, Union, Set

DataType = str
Span = Tuple[int, int]
TreeList = Union[str, List[Union[str, List]]]
from typing import Literal
from functools import lru_cache
Mode = Literal["recognize", "parse"]
from collections import defaultdict, deque

class MCFGGrammarParser:
    """Parser for parsing sentences using a Multiple Context-Free Grammar (MCFG).

        Parameters
        ----------
        grammar

        Attributes
        ----------
        grammar
        chart
        agenda
        """
    def __init__(self, grammar: MCFGGrammar):
        self.grammar = grammar
        self.chart = defaultdict(list)
        self.agenda = deque()

    def parse(self, input_string: List[str]):
        """Parse a sentence using the Multiple Context-Free Grammar (MCFG).
                Parameters
                ----------
                sentence : str

                Returns
                -------
                Goal item: S
                """
        self.initialize_agenda(input_string)
        while self.agenda:
            current_item = self.agenda.popleft()
            self.process_item(current_item)
        return self.check_goal(input_string)

    def initialize_agenda(self, input_string):
        # logic for starting the agenda with potential axioms/rules applicable directly to the input
        for i, token in enumerate(input_string):
            for rule in self.grammar.get_rules_by_left_side(token):
                for r in rule.right_side:
                    if r.variable == token:
                        new_instance = MCFGRuleElementInstance(rule.left_side.variable, ((i, i+1),))
                        self.agenda.append(new_instance)
                        self.chart[i, i+1].append(new_instance)

    def process_item(self, item):
        # logic for processing the items with applicable rules
        for rule in self.grammar.rules:
            if item.variable in [r.variable for r in rule.right_side]:
                self.apply_rule(rule, item)

    def apply_rule(self, rule, item):
        if all(subitem in [i.variable for i in self.chart.values()] for subitem in rule.right_side):
            new_instance = MCFGRuleElementInstance(rule.left_side.variable, item.span_indices)
            self.chart[item.span_indices].append(new_instance)
            self.agenda.append(new_instance)

    def check_goal(self, input_string):
        # logic for checking if an item covers the entire input and match the start symbol
        goal_span = (0, len(input_string))
        return any(item for item in self.chart[goal_span] if item.variable == self.grammar.start_symbol)

    def construct_parse(self):
        # Start from the full span of the input and the start symbol
        goal_span = (0, len(self.input_string))
        goal_items = [item for item in self.chart[goal_span] if item.variable == self.grammar.start_symbol]
        if not goal_items:
            return None

        # Select the first complete parse (or handle ambiguities as needed)
        root_item = goal_items[0]
        return self.build_tree(root_item)

    def build_tree(self, item):
        """Recursively build the tree."""
        if not item.backpointers:
            return MCFGTree(item.variable, item.string_spans)

        children = []
        for bp in item.backpointers:
            child_item = self.chart[bp.span]
            children.append(self.build_tree(child_item))

        return MCFGTree(item.variable, item.string_spans, children)

