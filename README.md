# Python Port Scanner

A beginner-friendly Python port scanner that scans open ports on a target using socket programming.

## Features

- Scan ports on a target
- Detect open ports
- Identify common services
- Fast scanning using timeouts
- Simple and beginner-friendly

## Technologies Used

- Python
- Socket Programming
## Installation

1. Clone the repository

```bash
git clone https://github.com//port-scanner.git
```

2. Navigate to the project folder

```bash
cd port-scanner
```

3. Run the scanner

```bash
python scanner.py
```

---

## Example Usage

```text
Enter target: scanme.nmap.org

----------------------------------------
Scanning Target: scanme.nmap.org
Scanning started...
----------------------------------------

Port 22 is OPEN (ssh)
Port 80 is OPEN (http)

----------------------------------------
Scan completed
----------------------------------------
```

## What I Learned

While building this project, I learned:

- Basics of socket programming
- How TCP connections work
- How port scanning works
- Difference between open and closed ports
- Using Python functions
- Error handling using try/except
- Using timeouts for faster scanning
- Writing cleaner and structured Python code

## Future Improvements

- Scan custom port ranges
- Add multithreading for faster scanning
- Add banner grabbing
- Add colored terminal output
- Export scan results to a file