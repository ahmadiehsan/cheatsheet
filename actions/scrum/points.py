import sys

import pyperclip


def calc_analyse_points(points):
    result_points = round(points * 0.15)
    if result_points == 0:
        return 1
    return result_points


def calc_test_points(points):
    has_test = input('Has test? [Y]es/[n]o ') or 'y'
    if has_test == 'n':
        return 0
    elif has_test == 'y':
        test_type = input('Writing test difficulty? [h]igh/[L]ow ') or 'l'
        if test_type.lower() == 'l':
            percentage = 0.25
        elif test_type.lower() == 'h':
            percentage = 0.40
        else:
            print('Invalid choice')
            sys.exit()

        result_points = round(points * percentage)
        if result_points == 0:
            return 1
        return result_points
    else:
        print('Invalid choice')
        sys.exit()


def calc_review_points(points):
    need_review = input('Need to review? [Y]es/[n]o ') or 'y'

    if need_review.lower() == 'n':
        return 0
    elif need_review.lower() == 'y':
        percentage = 0.35
    else:
        print('Invalid choice')
        sys.exit()

    result_points = round(points * percentage)
    if result_points == 0:
        return 1
    return result_points


def calc_document_points(points):
    need_doc = input('Need to write a document? [N]o/[y]es ') or 'n'

    if need_doc.lower() == 'n':
        return 0
    elif need_doc.lower() == 'y':
        percentage = 0.10
    else:
        print('Invalid choice')
        sys.exit()
    result_points = round(points * percentage)
    if result_points == 0:
        return 1
    return result_points


if __name__ == '__main__':
    task_points = int(input('Task estimated points: '))
    analyse_points = calc_analyse_points(task_points)
    test_points = calc_test_points(task_points)
    review_points = calc_review_points(task_points)
    document_points = calc_document_points(task_points)

    output = f"""
    =========================
    Task Points:\t {task_points}
    Analyse Points:\t {analyse_points}
    Test Points:\t {test_points}
    Review Points:\t {review_points}
    Document Points:\t {document_points}
    -------------------------
    Total Points:\t {task_points + analyse_points + test_points + review_points + document_points}
    =========================
    """

    print(output)
    pyperclip.copy(output)
    print('Data copied to the clipboard!')
