import re
import sys

levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']
levels_param = [level.lower() for level in levels]

def display_log_counts(counts: dict[str, int]) -> None:
    print("Рівень логування | Кількість\n-----------------|----------")

    for level, count in counts.items():
        # level followed by whitespace offset and then count
        print(f"{level}{' ' * (17 - len(level))}| {counts[level]}")

def count_logs_by_level(logs: list[dict[str, str]]) -> dict[str, int]:
    counts = {level: 0 for level in levels}

    for log in logs:
        counts[log['level']] = counts[log['level']] + 1

    return counts

def display_filtered_logs(logs: list, level: str) -> None:
    filtered_logs = filter_logs_by_level(logs, level)

    print(f"Деталі логів для рівня '{level}':")

    for log in filtered_logs:
        print(f"{log['instant']} - {log['message']}")

def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list:
    return [log for log in logs if log['level'] == level]

def load_logs(file_path: str) -> list[dict[str, str]] | IOError:
    lines = load_log_lines(file_path)

    if isinstance(lines, IOError):
        return lines

    return [parse_log_line(line) for line in lines]

# separate function to load logs
# we don't need to hold file open while we process lines,
# so reading and processing are separated
def load_log_lines(file_path: str) -> list | IOError:
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            return f.readlines()
    except IOError as e:
        return e

def parse_log_line(line: str) -> dict | None:
    # matches format "YYYY-MM-DD hh:mm:ss"
    match_instant = "(?P<instant>\d{4}-\d{2}-\d{2} ([01]\d|2[0-3]):[0-5]\d:[0-5]\d)"
    # matches either one of the levels uppercased: INFO, DEBUG, etc
    match_level = f"(?P<level>{'|'.join([level.upper() for level in levels])})"
    # matches any characters left to make a message
    match_message = f"(?P<message>.+)"

    pattern = f"^{match_instant} {match_level} {match_message}$"

    match = re.match(pattern, line)

    if match is None:
        return None

    return {
        "instant": match.group('instant'),
        "level": match.group('level'),
        "message": match.group('message'),
    }

def main(argv: list[str]) -> None:
    # checking arguments
    if len(argv) != 2 and len(argv) != 3:
        print('Invalid arguments: must be <path> [<log_level>]')
        exit(1)

    if len(argv) == 3 and argv[2] not in levels_param:
        print(f"Invalid 2nd argument ({argv[2]}) argument: must be one of {','.join(levels_param)}")
        exit(1)

    file_path = argv[1]

    logs = load_logs(file_path)

    # if loading logs failed, logs will be equal to the error
    if isinstance(logs, IOError):
        print(f'Could not read file {file_path}: {logs.errno}')
        exit(1)

    # if any of the lines did not match the pattern, we will have None
    if None in logs:
        print(f'File contains invalid lines')
        exit(1)

    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if len(argv) == 3:
        # empty string
        print()

        display_filtered_logs(logs, argv[2].upper())

if __name__ == '__main__':
    main(sys.argv)
