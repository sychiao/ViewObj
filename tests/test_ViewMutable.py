import re
import pytest
from ViewObj import View


def test_ViewObject():
    class A:
        pass

    view = View(A())
    with pytest.raises(Exception):
        view.get.a = 123

    with pytest.raises(Exception):
        del view.get.a

    x = view.copy()

def test_ViewMutable():
    view = View([1, 2, 3])
    x = [1, 2, 3]
    view2 = View(x)
    uiid = id(view)
    with pytest.raises(Exception):
        view.get.append(1)

    with pytest.raises(Exception):
        view.get.extend([1, 2, 3])

    with pytest.raises(Exception):
        view.get.insert(0, 1)

    with pytest.raises(Exception):
        view.get.remove(1)

    with pytest.raises(Exception):
        view.get.pop()

    with pytest.raises(Exception):
        view.get.clear()

    #view.get.append(1) # Error?
    view.get.count(1)
    assert id(view) != id(View([1, 2, 3])) # list is totolly different
    assert id(view) != id(view2)
    x.append(2)
    assert view2.get == [1, 2, 3, 2] # only view is immutable, not the object
    assert view.get + [1, 2, 3] == [1, 2, 3, 1, 2, 3]
    assert view.get < [1, 2, 3, 4]
    assert view.get <= [1, 2, 3]
    assert view.get == [1, 2, 3]
    assert view.get != [1, 2, 3, 4]
    assert view.get > []
    assert view.get >= [1, 2, 3]
    assert not view == (not [1, 2, 3])
    assert bool(view)
    assert uiid == id(view)
    assert [i for i in view.get] == [1, 2, 3]

def test_ViewDict():
    view = View({'a': 1, 'b': 2})
    uiid = id(view)
    with pytest.raises(Exception):
        view.get['a'] = 123

    with pytest.raises(Exception):
        del view.get['a']

    with pytest.raises(Exception):
        view['a'] = 123

    with pytest.raises(Exception):
        del view['a']

    assert uiid == id(view)
    assert view.get | {'c': 3} == {'a': 1, 'b': 2, 'c': 3}
    assert 'a' in view.get
    assert len(view.get) == 2

def testViewObject():
    class A:

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def vget(self):
            return self.a

        def vset(self, v):
            self.a = v

        def __hash__(self) -> int:
            return hash(self.a + self.b)

        def __repr__(self) -> str:
            return f"A({self.a}, {self.b})"

    view = View(A(1, 2))
    assert view.get.a == 1
    assert view.get.b == 2

    assert f'{view.get}' == 'A(1, 2)'
    assert repr(view.get) == 'A(1, 2)'

    with pytest.raises(Exception):
        view.get.a = 123

    with pytest.raises(Exception):
        del view.get.a

    view.get.vget()

    with pytest.raises(Exception):
        view.get.vset(123)

    assert hash(view) == hash(A(1, 2))

def testViewVIEW():
    view = View(View(1))
    assert id(view) == id(View(1))