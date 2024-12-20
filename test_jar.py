from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    try:
        jar.deposit(10)  # Exceeding capacity
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for exceeding capacity"

def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4
    try:
        jar.withdraw(5)  # Withdrawing more than available
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for withdrawing more than available"
