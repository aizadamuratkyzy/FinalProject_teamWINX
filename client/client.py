import argparse
import requests

MASTER_URL = "http://localhost:8080"


def upload(filename: str, data: str):
    response = requests.post(
        f"{MASTER_URL}/upload",
        params={
            "filename": filename,
            "data": data
        }
    )
    print(response.json())


def download(filename: str):
    response = requests.get(f"{MASTER_URL}/download/{filename}")
    print(response.json())


def delete(filename: str):
    response = requests.delete(f"{MASTER_URL}/delete/{filename}")
    print(response.json())


def list_files():
    response = requests.get(f"{MASTER_URL}/files")
    print(response.json())


def status():
    response = requests.get(f"{MASTER_URL}/")
    print(response.json())


def main():
    parser = argparse.ArgumentParser(description="Mini-GFS Client CLI")
    subparsers = parser.add_subparsers(dest="command")

    upload_parser = subparsers.add_parser("upload")
    upload_parser.add_argument("filename")
    upload_parser.add_argument("data")

    download_parser = subparsers.add_parser("download")
    download_parser.add_argument("filename")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("filename")

    subparsers.add_parser("list")
    subparsers.add_parser("status")

    args = parser.parse_args()

    if args.command == "upload":
        upload(args.filename, args.data)
    elif args.command == "download":
        download(args.filename)
    elif args.command == "delete":
        delete(args.filename)
    elif args.command == "list":
        list_files()
    elif args.command == "status":
        status()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()