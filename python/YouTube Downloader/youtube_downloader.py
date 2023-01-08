import os
import time
import re

from pytube import YouTube

# Set the save location to the "downloads" folder in the same directory as the script.
save_location = os.path.join(os.path.dirname(__file__), 'downloads')

# Run a loop until the user selects a valid option.
while True:
    # Print the option menu.
    print('1: Start')
    print('2: Usage and about')
    print('3: Exit')

    # Get the user's choice.
    choice = input('Enter your choice: ')

    # Start the download process.
    if choice == '1':
        # Get the URL of the YouTube video from the user.
        url = input('Enter the URL of the YouTube video: ')

        # Create a YouTube object.
        yt = YouTube(url)

        # Run a loop until the user selects a valid option.
        while True:
            # Get the format choice from the user.
            choice = input('Enter 1 to download MP4, 2 to download MP3, or 3 to download both: ')

            # Download the MP4 video.
            if choice == '1':
                video_stream = yt.streams.filter(file_extension='mp4').first()
                video_name = f"{yt.title} [{time.strftime('%Y-%m-%d %H:%M:%S')}] [mp4]"
                # Sanitize the file name by removing any invalid characters.
                video_name = re.sub(r'[\\/:*?"<>|]', '', video_name)
                # Add the .mp4 file extension to the end of the file name.
                video_name += '.mp4'
                video_stream.download(save_location, filename=video_name)
                break
            # Download the MP3 audio.
            elif choice == '2':
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_name = f"{yt.title} [{time.strftime('%Y-%m-%d %H:%M:%S')}] [mp3]"
                # Sanitize the file name by removing any invalid characters.
                audio_name = re.sub(r'[\\/:*?"<>|]', '', audio_name)
                # Add the .mp3 file extension to the end of the file name.
                audio_name += '.mp3'
                audio_stream.download(save_location, filename=audio_name)
                break
            # Download both the MP4 video and the MP3 audio.
            elif choice == '3':
                video_stream = yt.streams.filter(file_extension='mp4').first()
                video_name = f"{yt.title} [{time.strftime('%Y-%m-%d %H:%M:%S')}] [mp4]"
                # Sanitize the file name by removing any invalid characters.
                video_name = re.sub(r'[\\/:*?"<>|]', '', video_name)
                # Add the .mp4 file extension to the end of the file name.
                video_name += '.mp4'
                video_stream.download(save_location, filename=video_name)
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_name = f"{yt.title} [{time.strftime('%Y-%m-%d %H:%M:%S')}] [mp3]"
                # Sanitize the file name by removing any invalid characters.
                audio_name = re.sub(r'[\\/:*?"<>|]', '', audio_name)
                # Add the .mp3 file extension to the end of the file name.
                audio_name += '.mp3'
                audio_stream.download(save_location, filename=audio_name)
                break
            # Print an error message if the user enters an invalid option.
            else:
                print('Invalid option. Please try again.')
    # Print the usage and about information.
    elif choice == '2':
        print('This script allows you to download YouTube videos in MP4 or MP3 format.')
        print('To use the script, enter the URL of the YouTube video that you want to download, and then select the format that you want to download.')
    # Exit the script.
    elif choice == '3':
        break
    # Print an error message if the user enters an invalid option.
    else:
        print('Invalid option. Please try again.')
