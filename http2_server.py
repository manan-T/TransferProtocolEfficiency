import os
from quart import Quart, send_file
import hypercorn.asyncio
import asyncio

app = Quart(__name__)  # Corrected __name__
UPLOAD_FOLDER = "my_folder_name"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/download/<filename>")
async def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        return await send_file(file_path)
    return "File not found", 404

if __name__ == "__main__":

    config = hypercorn.Config()
    config.bind = ["0.0.0.0:8001"]  # Listen on all interfaces

    # Run the Quart app using Hypercorn properly
    asyncio.run(hypercorn.asyncio.serve(app, config))