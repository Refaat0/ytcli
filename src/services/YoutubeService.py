"""
    This file defines a service object that handles downloading a Youtube video
"""
import json, os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, VideoPrivate


class YoutubeService:
    def __init__(self, download_path) -> None:
        self.download_path = download_path
        self.ITAG_1080P="137"
        self.ITAG_720P="22"
        self.ITAG_360P="18"
        self.ITAG_160kbps="251"
        self.ITAG_128kbps="140"
        self.ITAG_70kbps="250"
        self.ITAG_50kbps="249"

    # This method downloads a Youtube video from the specified link at the 1080p resolution
    def download_1080p(self, link):
        try:
            print(link)
            YouTube(link).streams.get_by_itag(self.ITAG_1080P).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 1080p")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}")
        except Exception as e:
            print("Error: Something unexpected happened :(")
            
    # This method downloads a Youtube video from the specified link at the 720p resolution
    def download_720p(self, link):
        try:
            YouTube(link).streams.get_by_itag(self.ITAG_720P).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 720p")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}")
        except Exception as e:
            print("Error: Something unexpected happened :(")

    # This method downloads a Youtube video from the specified link at the 360p resolution
    def download_360p(self, link):
        try:
            YouTube(link).streams.get_by_itag(self.ITAG_360P).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 360p")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}")
        except Exception as e:
            print("Error: Something unexpected happened :(")

    #
    def download_160kpbs(self, link):
        try:
            YouTube(link).streams.get_by_itag(self.ITAG_160kbps).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 128kbps")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}")
        except Exception as e:
            print("Error: Something unexpected happened :(")

    #
    def download_128kpbs(self, link):
        try:
            YouTube(link).streams.get_by_itag(self.ITAG_128kbps).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 128kbps")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}")
        except Exception as e:
            print("Error: Something unexpected happened :(")

    #
    def download_70kpbs(self, link):
        try:
            YouTube(link).streams.get_by_itag(self.ITAG_70kbps).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 128kbps")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}")
        except Exception as e:
            print("Error: Something unexpected happened :(")

    #
    def download_50kpbs(self, link):
        try:
            YouTube(link).streams.get_by_itag(self.ITAG_50kbps).download(output_path=self.download_path)
        except RegexMatchError:
            print(f"Error: Could not find a Youtube video with the link: '{link}'")
        except VideoUnavailable:
            print("Error: This video is unavailable")
        except AttributeError:
            print(f"Error: This video is not available in 128kbps")
        except PermissionError:
            print(f"Error: Unable to write to {self.download_path}. Your privileges are insufficient.")
        except Exception as e:
            print("Error: Something unexpected happened :(")