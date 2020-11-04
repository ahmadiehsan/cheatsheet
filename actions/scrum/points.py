import math


def calc_test_points(points):
    return math.ceil(points / 4)


def calc_review_points(points):
    return math.ceil(points / 3)


if __name__ == '__main__':
    basic_points = int(input('Please enter your basic points estimation: '))
    basic_points += calc_test_points(basic_points)
    basic_points += calc_review_points(basic_points)
    print(f'Final points: {basic_points}')
