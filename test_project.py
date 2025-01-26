from project import create_sequence, check_answer, stats

def test_create_sequence():
    assert len(create_sequence(["blue", "red", "yellow", "green", "purple", "orange"])) == 4
    assert type(create_sequence(["blue", "red", "yellow", "green", "purple", "orange"])[0]) == str

def test_check_answer():
    assert check_answer(["blue", "red", "green", "green"], ["blue", "red", "green", "green"]) == (4, 0)
    assert check_answer(["blue", "red", "red", "red"], ["blue", "red", "green", "green"]) == (2, 0)
    assert check_answer(["green", "green", "blue", "red"], ["blue", "red", "green", "green"]) == (0, 4)
    assert check_answer(["green", "green", "blue", "red"], ["yellow", "yellow", "purple", "orange"]) == (0, 0)

def test_stats():
    assert stats(5, 4) == "Game won in 6 steps\n"
    assert stats(9, 4) == "Game won in 10 steps\n"
    assert stats(10, 0) == "Game lost\n"