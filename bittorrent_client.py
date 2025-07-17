import libtorrent as lt
import time

def download_torrent(torrent_file):
    # Create a session
    ses = lt.session()
    ses.listen_on(6881, 6891)
    print("Listening on port 6881")

    # Load the torrent file
    info = lt.torrent_info(torrent_file)
    h = ses.add_torrent({'ti': info, 'save_path': './'})

    print(f"Starting download for: {torrent_file}")

    # Download the torrent
    while not h.is_seed():
        s = h.status()
        print(f'{s.state} {s.progress * 100:.2f}% complete (down: {s.download_rate / 1000:.1f} kB/s up: {s.upload_rate / 1000:.1f} kB/s peers: {s.num_peers} seeds: {s.num_seeds})')
        time.sleep(1)

    print(f"Download complete: {torrent_file}")

if __name__ == "__main__":
    torrent_file = "B_10MB.torrent"  # This should be the .torrent file created by the server
    download_torrent(torrent_file)
