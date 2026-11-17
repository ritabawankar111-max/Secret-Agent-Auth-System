# Secret Agent Authentication & Audit System

A Python-based command-line security system built to track agent logins, silently trap unauthorized intruders, and maintain timestamped audit logs.

## Features
- **3-Attempt Security Lockout:** Limits login attempts to 3 tries before triggering a silent trap.
- **Silent Intruder Logging:** Records unauthorized access attempts in the background without alerting the user.
- **Live Audit Trail:** Uses Python's `datetime` module to log exact timestamps for every successful and failed login.
- **Admin Backdoor:** Secret command (`admin@view`) to view complete security logs directly in the terminal.
- 
