#!/usr/bin/python3
import sys


def print_statistics(total_file_size, status_counts):
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")


def main():
    total_file_size = 0
    status_counts = {}

    try:
        line_number = 0
        for line in sys.stdin:
            line_number += 1
            line = line.strip()

            # Parse the line in the given format: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
            parts = line.split()
            if len(parts) != 7 or parts[5][1:] not in ['200', '301', '400', '401', '403', '404', '405', '500']:
                continue

            status_code = parts[5][1:]
            file_size = int(parts[6])

            # Update total file size and status code counts
            total_file_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_number % 10 == 0:
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        # In case of CTRL + C, print the statistics gathered so far
        print_statistics(total_file_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
