from typing import List, Tuple, Union

DataType = str
Span = Tuple[int, int]
TreeList = Union[str, List[Union[str, List]]]

class MCFGTree:
    def __init__(self, data: DataType, spans: List[Span], children: List['MCFGTree'] = []):
        """
        Initialize an MCFG tree node.

        Parameters
        ----------
        data : str
            The symbol or value represented by this node.
        spans : list of (int, int)
            The list of spans representing the discontinuous yield.
        children : list of MCFGTree
            The children of this node in the parse tree.
        """
        self._data = data
        self._spans = spans
        self._children = children
        self._validate()

    def to_tuple(self) -> Tuple[DataType, Tuple[Span, ...], Tuple['MCFGTree', ...]]:
        return self._data, tuple(self._spans), tuple(c.to_tuple() for c in self._children)

    def __hash__(self) -> int:
        return hash(self.to_tuple())

    def __eq__(self, other: 'MCFGTree') -> bool:
        return self.to_tuple() == other.to_tuple()

    def __repr__(self) -> str:
        return self.to_string()

    def to_string(self, depth=0) -> str:
        """
        Generate a string representation of the parse tree.
        """
        prefix = ' ' * (depth * 2) + ('--' if depth > 0 else '')
        s = f"{prefix}{self._data} (spans: {self._spans})\n"
        for c in self._children:
            s += c.to_string(depth + 1)
        return s

    def _validate(self) -> None:
        """
        Validate that all children are of type MCFGTree.
        """
        try:
            assert all(isinstance(c, MCFGTree) for c in self._children)
        except AssertionError:
            raise TypeError('All children must be MCFGTree objects')

    @property
    def data(self) -> DataType:
        return self._data

    @property
    def spans(self) -> List[Span]:
        return self._spans

    @property
    def children(self) -> List['MCFGTree']:
        return self._children

    @classmethod
    def from_list(cls, tree_list: TreeList) -> 'MCFGTree':
        """
        Create an MCFGTree from a nested list representation.
        """
        if isinstance(tree_list, str):
            return cls(tree_list, [(0, 0)])
        else:
            # Internal node
            data = tree_list[0]
            children = [cls.from_list(child) for child in tree_list[1:] if isinstance(child, list)]
            return cls(data, [(0, 0)], children)