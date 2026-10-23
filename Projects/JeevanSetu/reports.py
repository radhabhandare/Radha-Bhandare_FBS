import threading
from pathlib import Path

from database import execute_query
from operations import filter_high_priority, generate_request_titles


REPORT_FOLDER = Path('reports')


def export_requests():
    requests = execute_query(
        '''SELECT request_id, title, category, quantity,
                  location, priority, status
           FROM emergency_requests
           ORDER BY request_id''',
        fetch=True
    )

    if requests is None:
        return

    REPORT_FOLDER.mkdir(exist_ok=True)
    file_path = REPORT_FOLDER / 'emergency_requests.csv'

    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            if requests:
                writer = csv.DictWriter(
                    file, fieldnames=requests[0].keys()
                )
                writer.writeheader()
                writer.writerows(requests)
            else:
                file.write('No emergency requests found.\n')

        print('Report saved:', file_path)

    except (OSError, csv.Error) as error:
        print('Report error:', error)


def show_high_priority_report():
    requests = execute_query(
        '''SELECT request_id, title, category, quantity,
                  location, priority, status
           FROM emergency_requests''',
        fetch=True
    )

    if requests is None:
        return

    high_priority = filter_high_priority(requests)

    if not high_priority:
        print('No high-priority requests found.')
        return

    for request in high_priority:
        print(
            request['request_id'],
            request['title'],
            request['location'],
            request['status']
        )


def show_request_titles():
    requests = execute_query(
        'SELECT title FROM emergency_requests',
        fetch=True
    )

    if requests is None:
        return

    for title in generate_request_titles(requests):
        print(title)


def save_report_in_background():
    report_thread = threading.Thread(target=export_requests)
    report_thread.start()
    report_thread.join()

    print('Report task completed.')
