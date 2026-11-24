from python import round, hint, result

def main():
    test_hint()

def test_hint():
    assert hint(5, 2) == 'big'
    assert hint(2, 5) == 'small'
    assert hint(5, 5) == 'right'

def test_round():
    assert round(5, [] ) == True 

def test_result():
    assert result('small', []) == True
    assert result('big', []) == True
    assert result('right', []) == True


if __name__ == "__main__":
    main()
