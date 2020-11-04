import sys

import pyperclip


def calc_analyse_points(points):
    return round(points * 0.15)


def calc_test_points(points):
    test_type = input('Writing test difficulty? [h]igh/[L]ow ') or 'l'

    if test_type.lower() == 'l':
        percentage = 0.25
    elif test_type.lower() == 'h':
        percentage = 0.40
    else:
        print('Invalid choice')
        sys.exit()

    return round(points * percentage)


def calc_review_points(points):
    return round(points * 0.35)


def calc_documentation_points(points):
    need_doc = input('Need to write a document? [N]o/[y]es ') or 'n'

    if need_doc.lower() == 'n':
        percentage = 0
    elif need_doc.lower() == 'y':
        percentage = 0.10
    else:
        print('Invalid choice')
        sys.exit()

    return round(points * percentage)


if __name__ == '__main__':
    task_points = int(input('Please enter your basic points estimation: '))
    analyse_points = calc_analyse_points(task_points)
    test_points = calc_test_points(task_points)
    review_points = calc_review_points(task_points)
    documentation_points = calc_documentation_points(task_points)

    output = f"""
    =========================
    Task Points:\t {task_points}
    Analyse Points:\t {analyse_points}
    Test Points:\t {test_points}
    Review Points:\t {review_points}
    Document Points:\t {documentation_points}
    -------------------------
    Total Points:\t {task_points + analyse_points + test_points + review_points + documentation_points}
    =========================
    """

    print(output)
    pyperclip.copy(output)
    print('Data copied to the clipboard!')
