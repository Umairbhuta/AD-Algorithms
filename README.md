# AD Algo - Video Processor

## Overview
The AD Algo - Video Processor application is a Python-based GUI tool developed by "AD Algorithms" that allows users to add text-to-speech-generated audio to a video file. It leverages the following libraries:

- **moviepy**: For video and audio editing.
- **gTTS** (Google Text-to-Speech): To generate audio from text.
- **tkinter**: For creating a graphical user interface (GUI).

## Features
1. **Text-to-Speech Conversion**:
   - Converts user-inputted text into speech audio using Google Text-to-Speech (gTTS).
   
2. **Audio-Video Integration**:
   - Combines the generated audio with a selected video file using the MoviePy library.

3. **GUI-Based User Interaction**:
   - User-friendly interface to select input video files, specify output paths, and provide text for audio generation.

4. **Progress Feedback**:
   - Real-time progress updates displayed to the user via a progress bar and percentage label.

## How It Works
1. **Input Video File**:
   - Users browse and select a video file (supported formats: `.mp4`).

2. **Enter Text for Audio**:
   - Users input the text they want to convert to audio.

3. **Generate Audio**:
   - The entered text is converted to an audio file (`temp_audio.mp3`) using gTTS.

4. **Combine Audio and Video**:
   - The generated audio is added to the selected video, producing a new video file with the audio embedded.

5. **Save Output**:
   - Users can specify the output file path and save the final video.

## Requirements
- **Python 3.6+**
- Libraries:
  - `moviepy`
  - `gtts`
  - `tkinter` (pre-installed with Python)
- FFmpeg (required by MoviePy for video processing)

## How to Run
1. Install required Python libraries:
   ```
   pip install moviepy gtts
   ```
2. Ensure FFmpeg is installed and added to the system's PATH.
3. Run the script:
   ```
   python video_processor.py
   ```

## Files
- **`video_processor.py`**:
   - Main script containing all functions and GUI implementation.
- **`temp_audio.mp3`**:
   - Temporary audio file generated during processing (deleted after processing).

## Usage
1. Launch the application.
2. Select a video file using the "Browse" button.
3. Enter the text to be converted into speech.
4. Specify the output file path using the "Save As" button.
5. Click "Start Processing" to generate and save the video with the embedded audio.
6. View real-time progress updates on the progress bar.

## Error Handling
- Errors during audio generation or video processing are displayed via error messages.
- Warnings are shown if required fields are left empty.

## Credits
- **Google Text-to-Speech (gTTS)**: For text-to-speech functionality.
- **MoviePy**: For seamless video and audio editing.
- **Tkinter**: For creating an intuitive user interface.
- **AD Algorithms**: For designing and developing this application.

