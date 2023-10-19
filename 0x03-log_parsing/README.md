# Log Parsing

## Tasks

### 0. Log parsing
**Mandatory**

Write a script that reads stdin line by line and computes metrics:

- **Input format**: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

- Total file size: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>` as per the input format above)
- Number of lines by status code:
  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
  - If a status code doesn’t appear or is not an integer, don’t print anything for this status code
  - Format: `<status code>: <number>`
  - Status codes should be printed in ascending order

**Warning**: In this sample, you will have random values - it’s normal to not have the same output as this one.

## Usage

```bash
# Example usage with provided scripts

./0-generator.py | ./0-stats.py
```

## Repository Details

* GitHub repository: [alx-interview](./https://github.com/gebretewodros73/alx-interview)
* Directory: [0x03-log_parsing](./0x03-log_parsing)
* File: [0-stats.py](./0-stats.py)
