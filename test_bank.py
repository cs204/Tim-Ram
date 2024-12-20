import bank

def test_value_zdravstvuyte():
    assert bank.value("здравствуйте, как ваши дела?") == 0

def test_value_z():
    assert bank.value("завтрак") == 20

def test_value_default():
    assert bank.value("Hello") == 100
