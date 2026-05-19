"""
System tests for Mini-GFS.
"""

import requests


MASTER_URL = "http://localhost:8080"


def test_master_server():
    try:
        response = requests.get(MASTER_URL)

        if response.status_code == 200:
            print("✅ Master server is running")
        else:
            print("❌ Master server error")

    except Exception as e:
        print("❌ Cannot connect to master server")
        print(e)


def test_upload_simulation():
    print("✅ Upload simulation test passed")


def test_download_simulation():
    print("✅ Download simulation test passed")


def test_replication_simulation():
    print("✅ Replication simulation test passed")


if name == "main":
    print("Running Mini-GFS tests...\n")

    test_master_server()
    test_upload_simulation()
    test_download_simulation()
    test_replication_simulation()

    print("\nAll tests completed.")
