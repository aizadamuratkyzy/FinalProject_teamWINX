# Tests

Owner: [Lyudmila]

System tests for validating the Mini-GFS distributed file system.

---

## Purpose

This module checks whether the main system components are working correctly.

The tests verify:

- Master server availability
- Upload simulation
- Download simulation
- Replication simulation

---

## Test File

tests/test_system.py
---

## Run Tests

python tests/test_system.py
Or through the unified launcher:

python main.py tests
---

## Example Output

Running Mini-GFS tests...

✅ Master server is running
✅ Upload simulation test passed
✅ Download simulation test passed
✅ Replication simulation test passed

All tests completed.
---

## Technologies

- Python 3
- Requests
- FastAPI
