# 🚀 Transfer Protocol Efficiency: HTTP/1.1, HTTP/2, and BitTorrent

This project simulates file transfers using HTTP/1.1, HTTP/2, and BitTorrent protocols to analyze throughput, protocol overhead, and network efficiency. It compares peer-to-peer and client-server performance with automated transfers.

## 📂 Project Structure
- **http1_client.py**: HTTP/1.1 client for downloading files from the server.
- **http1_server.py**: HTTP/1.1 server serving files for download.
- **http2_client.py**: HTTP/2 client for downloading files using `httpx` with asynchronous support.
- **http2_server.py**: HTTP/2 server built with Quart and Hypercorn to serve files.
- **BitTorrent**: (Not implemented in this code snippet; suggested for comparison with HTTP protocols.)

## 📈 Key Features
- **Protocol Comparison**: Simulates file downloads using HTTP/1.1, HTTP/2, and BitTorrent to measure performance.
- **Throughput and Overhead**: Measures file transfer throughput and calculates protocol overhead for comparison.
- **Peer-to-Peer vs Client-Server**: Evaluates the difference in file transfer efficiency between peer-to-peer (BitTorrent) and client-server (HTTP) models.

## 🔧 Requirements
- Python 3.x
- Required libraries: `requests`, `httpx`, `quart`, `hypercorn`

You can install the required Python packages using pip:

```bash
pip install requests httpx quart hypercorn
```

## 🚀 Getting Started

### HTTP/1.1 Server
1. Navigate to the directory where `http1_server.py` is located.
3. Run the HTTP/1.1 server with the following command:
   ```bash
   python http1_server.py
   ```
### HTTP/1.1 Client
1. Make sure the HTTP/1.1 server is running.
2. Run the client script to download the file:
   ```bash
   python http1_client.py
   ```
### HTTP/2 Server
1. Navigate to the directory where http2_server.py is located.
2. Run the HTTP/2 server with the following command:
   ```bash
   python http2_server.py
   ```
### HTTP/2 Client
1. Make sure the HTTP/2 server is running.
2. Run the client script to download the file:
   ```bash
   python http2_client.py
   ```

### Measuring Results
The client scripts for HTTP/1.1 and HTTP/2 will output:
1. Total data transferred
2. Average throughput (bytes/sec)
3. Overhead (comparison of file size to total transferred data)

### 📊 Example Output
For HTTP/1.1 client:
```yaml
Completed 1/1 downloads.
Overall Throughput (all files): 1024 B/s
Total File Size Downloaded: 10485760 bytes
Total time taken: 10.5 seconds
```

For HTTP/2 client:
```yaml
Total Data Transferred: 10485760 bytes
Average Throughput: 1024000.00 bytes/sec
Overhead: 1.00
```

### How it works?
1. HTTP/1.1: A simple client-server download mechanism using Python's requests library to simulate the file transfer process.
2. HTTP/2: An asynchronous file download system using httpx to leverage HTTP/2's multiplexing feature for improved performance.
3. BitTorrent: Peer-to-peer file sharing can be implemented using a BitTorrent library (e.g., libtorrent), but is not covered in this code.

## 🚀 BitTorrent File Transfer

This part implements file transfers using **BitTorrent**, utilizing the `libtorrent` library for peer-to-peer file sharing. The project compares the efficiency of BitTorrent transfers with traditional client-server protocols such as HTTP/1.1 and HTTP/2.

### 📂 Project Structure

- **bittorrent_server.py**: BitTorrent server script that creates a torrent file and shares the file over the BitTorrent network.
- **bittorrent_client.py**: BitTorrent client script that downloads files using the BitTorrent protocol.

### 🔧 Requirements

To get started with BitTorrent file transfers, you need to install the **libtorrent** Python package:

```bash
pip install python-libtorrent
```

### 🚀 Getting Started
BitTorrent Server
1. Navigate to the directory where bittorrent_server.py is located.
2. Run the server to create a torrent file and start sharing the file:
  ```bash
  python bittorrent_server.py
  ```

BitTorrent Client
1. After the server has started and the torrent file is created, download the .torrent file from the server.
2. Navigate to the directory where bittorrent_client.py is located.
3. Run the client to start downloading the file:
   ```bash
   python bittorrent_client.py
   ```

### Example Output
For the BitTorrent Server:
``` yaml
Torrent file created at: B_10MB.torrent
Listening on port 6881
Starting torrent for: B_10MB
Now waiting for peers...

```
For the BitTorrent Client:
```yaml
Listening on port 6881
Starting download for: B_10MB.torrent
downloading: 75.12% complete (down: 512.0 kB/s up: 200.0 kB/s peers: 3 seeds: 2)
Download complete: B_10MB

```

### ⚙️ How It Works
1. BitTorrent Server (bittorrent_server.py):
    1.1 Creates a torrent file for the given file path using libtorrent.
    1.2 The server listens for peers, shares the torrent, and waits for download completion.

2. BitTorrent Client (bittorrent_client.py):
    2.1 Downloads the file from peers using the .torrent file created by the server.
    2.2 Displays the download progress, speed, and number of peers until the file is fully downloaded.

### Performance Metrics
1. Throughput: Measures download speed (bytes/sec).
2. Peer-to-Peer Efficiency: Assesses the distribution of file sharing across multiple peers.
3. Protocol Comparison: Helps compare BitTorrent performance against client-server file transfer protocols.





   




   

























