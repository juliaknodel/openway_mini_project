import pytest


from src.task_1 import read_data


class Case:
    def __init__(self, name: str,
                 input_data: str,
                 answer: int):
        self._name = name
        self.input_data = input_data
        self.answer = answer

    def __str__(self) -> str:
        return 'read_input_data_test_{}'.format(self._name)


TEST_CASES = [

    Case(
        name='base positive test',
        input_data="1 2 3 4",
        answer=1
    ),

    Case(
        name='positive test, same digits',
        input_data="1 1 1 1",
        answer=1
    ),

    Case(
        name='positive test, one negative digit',
        input_data="-1 2 3 4",
        answer=1
    ),

    Case(
        name='positive test, all negatives',
        input_data="-1 -2 -3 -4",
        answer=1
    ),


    Case(
        name='empty string',
        input_data="",
        answer=0
    ),

    Case(
        name='only 3 digits',
        input_data="2 3 4",
        answer=0
    ),

    Case(
        name='more than 4 digits',
        input_data="2 3 4 5 6",
        answer=0
    ),

    Case(
        name='positive test, more than 1 space btw digits',
        input_data="1   2   3        4",
        answer=1
    ),

    Case(
        name='positive test, real digit',
        input_data="1.1 2 3 4",
        answer=1
    ),

    Case(
        name='positive test, all real',
        input_data="1.1 2.2837823 3.1 4.09",
        answer=1
    ),

    Case(
        name='real with , as separator',
        input_data="1,1 2 3 4",
        answer=0
    ),

    Case(
        name='few . in real digit',
        input_data="1..1 2 3.2 4",
        answer=0
    ),

    Case(
        name='combine . and ,',
        input_data="1.,1 2 3 4",
        answer=0
    ),

    Case(
        name='combine . and ,',
        input_data="1,.1 2 3 4",
        answer=0
    ),

    Case(
        name='positive test, real negative',
        input_data="1.1 2.0002 -3.12 4.0",
        answer=1
    ),

    Case(
        name='letters',
        input_data="1 2b 3 4",
        answer=0
    ),

    Case(
        name='check one of the invalid characters',
        input_data="1 2 3 4~",
        answer=0
    ),

    Case(
        name='check one of the invalid characters',
        input_data="1.1 2/3 4 4",
        answer=0
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_read_input_data(case: Case) -> None:

    res, check = read_data(case.input_data)

    assert check['status'] == case.answer
