"""
    This file...
"""
import json, os

# get the download path from config.json
download_path = None
FILE_CONFIG = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'config.json'))
with open (FILE_CONFIG, "r") as file_config:
    download_path = json.load(file_config)["downloadPath"]

# declare & initialize a YoutubeService object
from ..services.YoutubeService import YoutubeService
youtube_service = YoutubeService(download_path)

# decalres & initializes a dictionary that maps arguments to functions
dispatch_table = {
    "1080p": youtube_service.download_1080p,
    "720p": youtube_service.download_720p,
    "360p": youtube_service.download_360p,
    "160kbps": youtube_service.download_160kpbs,
    "128kbps": youtube_service.download_128kpbs,
    "70kbps": youtube_service.download_70kpbs,
    "50kbps": youtube_service.download_50kpbs 
}

# dispatch mechanism
def process_arguments(argument, args):
    fn = dispatch_table.get(argument)
    fn(args)
    