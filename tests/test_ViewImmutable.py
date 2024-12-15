from ViewObj import View

def test_ViewImmutable1():
    view = View(1)
    assert id(view) == id(View(1))
    assert view + 1 == 2
    assert view - 1 == 0
    assert view < 2
    assert view <= 1
    assert view == 1
    assert view != 2
    assert view > 0
    assert view >= 1
    assert view & 1 == 1
    assert view | 1 == 1
    assert view ^ 1 == 0
    assert view >> 1 == 0
    assert view << 1 == 2
    assert view * 2 == 2
    assert view / 2 == 0.5
    assert view // 2 == 0
    assert view % 2 == 1
    assert view ** 2 == 1
    assert not view == False
    assert bool(view)
    assert id(int(view)) == id(1)

def test_ViewImmutable2():
    view = View(1.0)
    assert id(view) == id(View(1.0))
    assert view.get + 1.0 == 2.0
    assert view.get - 1.0 == 0.0
    assert view.get < 2.0
    assert view.get <= 1.0
    assert view.get == 1.0
    assert view.get != 2.0
    assert view.get > 0.0
    assert view.get >= 1.0
    assert float(view) == 1.0
    assert not view == False
    assert bool(view)

def test_ViewImmutable3():
    view = View('1')
    assert id(view) == id(View('1'))
    assert view.get + '1' == '11'
    assert view.get < '2'
    assert view.get <= '1'
    assert view.get == '1'
    assert view.get != '2'
    assert view.get > ''
    assert view.get >= '1'
    assert not view == (not '1')
    assert bool(view)

def test_ViewImmutable4():
    view = View((1, 2, 3))
    assert id(view) == id(View((1, 2, 3)))
    assert view.get + (1, 2, 3) == (1, 2, 3, 1, 2, 3)
    assert view.get < (1, 2, 3, 4)
    assert view.get <= (1, 2, 3)
    assert view.get == (1, 2, 3)
    assert view.get != (1, 2, 3, 4)
    assert view.get > ()
    assert view.get >= (1, 2, 3)
    assert not view == False
    assert bool(view)
    assert view.get[0] == 1
    assert view.get[1] == 2
    assert view.get[2] == 3
