from project import create_sequence, check_answer

def test_create_sequence():
    assert len(create_sequence(["blue", "red", "yellow", "green", "purple", "orange"])) == 4
    assert type(create_sequence(["blue", "red", "yellow", "green", "purple", "orange"])[0]) == str

def test_check_answer():
    assert check_answer(["blue", "red", "green", "green"], ["blue", "red", "green", "green"]) == (4, 0)
    assert check_answer(["blue", "red", "red", "red"], ["blue", "red", "green", "green"]) == (2, 0)
    assert check_answer(["green", "green", "blue", "red"], ["blue", "red", "green", "green"]) == (0, 4)
    assert check_answer(["green", "green", "blue", "red"], ["yellow", "yellow", "purple", "orange"]) == (0, 0)
