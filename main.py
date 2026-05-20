import argparse
import os


def run_master():
    os.system(
        "uvicorn master.main:app --host 0.0.0.0 --port 8080 --reload"
    )


def run_chunkserver():
    os.system(
        "uvicorn chunkserver.main:app --host 0.0.0.0 --port 8001 --reload"
    )


def run_client():
    os.system(
        "python client/client.py"
    )


def run_ai_agent():
    os.system(
        "python ai_agent/agent.py"
    )


def run_tests():
    os.system(
        "python tests/test_system.py"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Mini-GFS Project Runner"
    )

    parser.add_argument(
        "service",
        choices=[
            "master",
            "chunkserver",
            "client",
            "ai",
            "tests"
        ],
        help="Choose service to run"
    )

    args = parser.parse_args()

    if args.service == "master":
        run_master()

    elif args.service == "chunkserver":
        run_chunkserver()

    elif args.service == "client":
        run_client()

    elif args.service == "ai":
        run_ai_agent()

    elif args.service == "tests":
        run_tests()


if __name__ == "__main__":
    main()