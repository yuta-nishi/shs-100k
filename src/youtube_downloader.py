import csv
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

from util.logging_config import setup_logging

LIST_PATH = "/Users/yutanishi/shs-100k/src/list/list.tsv"
LOG_PATH = "/Users/yutanishi/shs-100k/src/log/youtube_downloader.log"

logger = setup_logging(LOG_PATH)


def file_exists(filename: str) -> bool:
    return os.path.isfile(filename)


def download_audio(url: str, count: str, song_id: str, version_id: str) -> None:
    filename_template = (
        f"/home/data/yutanishi/shs-100k/raw/{count}_{song_id}_{version_id}"
    )
    if file_exists(f"{filename_template}.wav"):
        logger.info(f"File {filename_template}.wav already exists. Skipping download.")
        return

    try:
        result = subprocess.run(
            ["yt-dlp", "-x", "--audio-format", "wav", "-o", filename_template, url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.stderr:
            logger.error(f"{result.stderr}")

    except Exception:
        logger.exception(f"Unexpected error occurred while downloading {url}")


max_workers = 10

with open(LIST_PATH, "r") as file:
    reader = csv.reader(file, delimiter="\t")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for count, row in enumerate(reader):
            video_url = row[4]  # YouTube URL is in the fifth column
            song_id = row[0]  # Song ID
            version_id = row[1]  # Version ID
            if video_url:
                count_str = str(count).zfill(6)
                logger.info(f"Initiating download {video_url}...")
                executor.submit(download_audio, video_url, count_str, song_id, version_id)

logger.info("All downloads initiated.")
