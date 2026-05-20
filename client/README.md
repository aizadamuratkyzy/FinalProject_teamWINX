# Client CLI

Owner: [Sovetova Zhansaya]

Command-line interface for interacting with the Mini-GFS distributed file system.

---

## Features

- Upload files to the cluster
- Download files from the cluster
- Delete files
- List stored files
- Check server status

---

## Commands

### Upload file

```bash
python client/client.py upload test.txt "hello world"
```

### Download file

```bash
python client/client.py download test.txt
```

### Delete file

```bash
python client/client.py delete test.txt
```

### List files

```bash
python client/client.py list
```

### Check system status

```bash
python client/client.py status
```

---

## Connected Services

- Master Server (port 8080)
- Chunkserver (port 8001)

---

## Technologies

- Python 3
- Requests
- FastAPI