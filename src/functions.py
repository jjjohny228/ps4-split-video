import subprocess

from src.utils import get_video_duration


class Trimmer:
    @staticmethod
    def ps_vr_trim(input_file, output_file, start_second, end_second):
        """
        This function takes start and end trims and using them trim video
        """
        # Calculate start time and duration in seconds
        start_time = start_second
        duration = (end_second - start_second)

        # Build the ffmpeg command
        command = [
            'ffmpeg',
            '-ss', str(start_time),  # Start time in seconds
            '-i', input_file,  # Input file
            '-t', str(duration),  # Duration in seconds
            '-c:v', 'copy',  # Copy video codec (maintain quality)
            '-c:a', 'copy',  # Copy audio codec (maintain quality)
            '-y', output_file  # Output file
        ]

        # Run the command
        subprocess.run(command, check=True)

    def trim(self, input_file, result_folder):
        """
        This function splits the video into two-minute parts
        """
        start_trim = 0
        end_trim = 120
        file_number = 1
        duration = get_video_duration(input_file)
        while True:
            output_file = f'{result_folder}/{file_number}_180_sbs.mp4'
            self.ps_vr_trim(input_file, output_file, start_trim, end_trim)
            start_trim += 120
            end_trim += 120
            file_number += 1
            if int(end_trim - duration) == 120:
                return
            print(end_trim - duration)
            if end_trim > duration:
                end_trim = duration

    @staticmethod
    def convert_and_trim_video(self, input_file, output_file, start_minute, end_minute):
        """This function trims video using start and end time. Also, it changes the frame rate to 59.94.
        This frame rate is perfect for the PS4.
        """
        start_time = start_minute * 60
        duration = (end_minute - start_minute) * 60

        # Build the ffmpeg command
        command = [
            'ffmpeg',
            '-ss', str(start_time),  # Start time in seconds
            '-i', input_file,  # Input file
            '-t', str(duration),  # Duration in seconds
            '-r', '59.94',  # Set frame rate to 59.94 FPS
            '-c:v', 'libx264',  # Use libx264 codec to re-encode video
            '-preset', 'slow',  # Choose encoding speed vs quality (slow gives better quality)
            '-crf', '18',  # Set quality (lower is better, 18-23 is visually lossless)
            '-c:a', 'copy',  # Copy audio codec (no re-encoding)
            output_file  # Output file
        ]

        # Run the command
        subprocess.run(command, check=True)