import time
import asyncio
import httpx

def measure_transfer_time(filename, num_downloads, server_ip):
    url = f"http://{server_ip}:8001/download/{filename}"
    results = []

    async def fetch():
        async with httpx.AsyncClient(http2=True, verify=False) as client:
            for _ in range(num_downloads):
                start_time = time.time()
                response = await client.get(url)
                end_time = time.time()

                if response.status_code == 200:
                    file_size = len(response.content)
                    transfer_time = end_time - start_time
                    throughput = file_size / transfer_time # Avoid division by zero
                    results.append((file_size, transfer_time, throughput))

                    # Save the file to disk, overwriting each time
                    with open(filename, "wb") as f:
                        f.write(response.content)
                    print(f"saved {filename}")

                else:
                    print(f"Failed to download {filename} (HTTP {response.status_code})")

    try:
        asyncio.run(fetch())  # Run the async function
    except RuntimeError:
        print("Event loop already running. Run this script outside of an interactive notebook.")

    # Print Results
    if results:
        total_data = sum(r[0] for r in results)
        avg_throughput = sum(r[2] for r in results) / len(results)
        overhead = total_data / (num_downloads * results[0][0])  # Use the first file size
        print(f"Total Data Transferred: {total_data} bytes")
        print(f"Average Throughput: {avg_throughput:.2f} bytes/sec")
        print(f"Overhead: {overhead:.2f}")
    else:
        print("No successful downloads, check the server.")

if __name__ == "__main__":
    filename = "B_10kB"  # Change this
    num_downloads = 1000 # Change this
    server_ip = "192.168.1.172"  # Change to server's IP
    measure_transfer_time(filename, num_downloads, server_ip)