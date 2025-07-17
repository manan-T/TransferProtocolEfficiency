import libtorrent as lt
import time
import os

def create_torrent(file_path):
    # Create a torrent file for the given file path
    fs = lt.file_storage()
    lt.add_files(fs, file_path)
    t = lt.create_torrent(fs)
    t.set_creator("Python BitTorrent")
    
    # Save the .torrent file
    torrent_path = file_path + ".torrent"
    with open(torrent_path, 'wb') as f:
        f.write(lt.bencode(t.generate()))
    
    print(f"Torrent file created at: {torrent_path}")
    return torrent_path

def start_torrent_server(file_path):
    # Create torrent file
    torrent_file = create_torrent(file_path)

    # Create a session
    ses = lt.session()
    ses.listen_on(6881, 6891)
    print("Listening on port 6881")

    # Add the torrent to the session
    info = lt.torrent_info(torrent_file)
    h = ses.add_torrent({'ti': info, 'save_path': './'})
    
    print(f"Starting torrent for: {file_path}")
    
    # Start the torrent
    print(f"Downlod link: {torrent_file}")
    print("Now waiting for peers...")
    while not h.is_seed():
        s = h.status()
        print(f'{s.state} {s.progress * 100:.2f}% complete (down: {s.download_rate / 1000:.1f} kB/s up: {s.upload_rate / 1000:.1f} kB/s peers: {s.num_peers} seeds: {s.num_seeds})')
        time.sleep(1)

    print(f"Download complete: {file_path}")

if __name__ == "__main__":
    file_path = "B_10MB"  # Change this to your file
    start_torrent_server(file_path)
