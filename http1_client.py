import requests
import time

SERVER_URL = "http://192.168.1.172:8080/"
FILENAME = "B_10MB"
NUM_DOWNLOADS = 1

def download_file(filename):
    start_time = time.time()
    response = requests.get(SERVER_URL + filename, stream=True)
    end_time = time.time()

    if response.status_code == 200:
        file_size = 0
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    file_size += len(chunk)

        transfer_time = end_time - start_time
        throughput = file_size / transfer_time if transfer_time > 0 else 0
        return throughput, file_size, transfer_time
    else:
        return None, None, None

def run_downloads(num_downloads):
    total_file_size = 0
    total_transfer_time = 0
    successful_downloads = 0

    for _ in range(num_downloads):
        throughput, file_size, transfer_time = download_file(FILENAME)
        if throughput is not None:
            total_file_size += file_size
            total_transfer_time += transfer_time
            successful_downloads += 1
        else:
            print("Download failed.")

    if successful_downloads > 0:
        overall_throughput = total_file_size / total_transfer_time if total_transfer_time >0 else 0;
        print(f"Completed {successful_downloads}/{num_downloads} downloads.")
        print(f"Overall Throughput (all files): {overall_throughput} B/s")
        print(f"Total File Size Downloaded: {total_file_size} bytes")
        print(f"Total time taken: {total_transfer_time} seconds")
    else:
        print("All downloads failed.")

run_downloads(NUM_DOWNLOADS)