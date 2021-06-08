import pytest


from src.task_1 import calculate


class Case:
    def __init__(self, name: str,
                 input_data: list,
                 status: int,
                 answer: float):
        self._name = name
        self.input_data = input_data
        self.status = status
        self.answer = answer

    def __str__(self) -> str:
        return 'calculate_test_{}'.format(self._name)


TEST_CASES = [

    Case(
        name='base positive test',
        input_data=[1, 1, 1, 1],
        status=1,
        answer=1
    ),

    Case(
        name='divide by zero',
        input_data=[1, 1, 1, -1],
        status=0,
        answer=-1
    ),

    Case(
        name='real numbers',
        input_data=[1.1, -0.1, 1.5, 2.5],
        status=1,
        answer=0.25
    ),

    Case(
        name='positive test, zero in numerator',
        input_data=[0, 0, 1, 0],
        status=1,
        answer=0
    ),

    Case(
        name='all zeros',
        input_data=[0, 0, 0, 0],
        status=0,
        answer=-1
    ),

]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_read_input_data(case: Case) -> None:

    res = calculate(case.input_data)

    assert (res['status'] == case.status) & (res['res'] == case.answer)
