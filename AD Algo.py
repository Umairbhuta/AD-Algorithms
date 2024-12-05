import moviepy.editor as mp 
from gtts import gTTS
import os
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Function to generate audio from text
def generate_audio_from_text(text, audio_path, progress, progress_label):
    try:
        progress["value"] = 20
        progress_label.config(text="20%")
        tts = gTTS(text=text, lang="en")
        tts.save(audio_path)
        progress["value"] = 40
        progress_label.config(text="40%")
        root.update_idletasks()
    except Exception as e:
        messagebox.showerror("Error", f"Error in generating audio: {e}")
        return False
    return True

# Function to add audio to the video
def add_audio_to_video(input_video_path, audio_path, output_video_path, progress, progress_label):
    try:
        video = mp.VideoFileClip(input_video_path)
        progress["value"] = 60
        progress_label.config(text="60%")
        audio = mp.AudioFileClip(audio_path)
        video_with_audio = video.set_audio(audio)
        progress["value"] = 80
        progress_label.config(text="80%")
        root.update_idletasks()
        video_with_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
        progress["value"] = 100
        progress_label.config(text="100%")
        root.update_idletasks()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error in adding audio to video: {e}")
        return False

# Function to handle processing
def process_video():
    input_video_path = video_path.get()
    output_video_path = output_path.get()
    text_to_speech = text_entry.get("1.0", tk.END).strip()
    temp_audio_path = "temp_audio.mp3"

    if not input_video_path or not output_video_path or not text_to_speech:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    # Disable the start button and update its text to 'Processing...'
    start_button.config(state=tk.DISABLED, text="Processing...")

    progress["value"] = 0
    progress_label.config(text="0%")
    
    # Start processing in a separate thread
    threading.Thread(target=process_thread, args=(input_video_path, output_video_path, text_to_speech, temp_audio_path)).start()

def process_thread(input_video_path, output_video_path, text_to_speech, temp_audio_path):
    if generate_audio_from_text(text_to_speech, temp_audio_path, progress, progress_label):
        if add_audio_to_video(input_video_path, temp_audio_path, output_video_path, progress, progress_label):
            os.remove(temp_audio_path)  # Cleanup temp audio file
            messagebox.showinfo("Success", "Video processing completed!")

            # Re-enable the button and reset its text
            start_button.config(state=tk.NORMAL, text="Start Processing")

# Function to browse files
def browse_file(entry, filetypes):
    path = filedialog.askopenfilename(filetypes=filetypes)
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def save_file(entry):
    path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

# GUI setup
root = tk.Tk()
root.title("AD Algo - Video Processor")
root.geometry("600x500")
root.config(bg="#282c34")

# Heading
heading = tk.Label(root, text="AD Algo - Video Processor", font=("Arial", 18, "bold", "italic"), bg="#61afef", fg="white", pady=10)
heading.pack(fill=tk.X)

# Video input
frame1 = tk.Frame(root, bg="#282c34")
frame1.pack(pady=10, fill=tk.X)
video_label = tk.Label(frame1, text="Video File:", font=("Arial", 12), bg="#282c34", fg="white")
video_label.pack(side=tk.LEFT, padx=10)
video_path = tk.Entry(frame1, font=("Arial", 12), width=40)
video_path.pack(side=tk.LEFT, padx=10)
browse_button = tk.Button(frame1, text="Browse", command=lambda: browse_file(video_path, [("Video files", "*.mp4")]), bg="#61afef", fg="white")
browse_button.pack(side=tk.LEFT)

# Output path
frame2 = tk.Frame(root, bg="#282c34")
frame2.pack(pady=10, fill=tk.X)
output_label = tk.Label(frame2, text="Output File:", font=("Arial", 12), bg="#282c34", fg="white")
output_label.pack(side=tk.LEFT, padx=10)
output_path = tk.Entry(frame2, font=("Arial", 12), width=40)
output_path.pack(side=tk.LEFT, padx=10)
save_button = tk.Button(frame2, text="Save As", command=lambda: save_file(output_path), bg="#61afef", fg="white")
save_button.pack(side=tk.LEFT)

# Text to speech
frame3 = tk.Frame(root, bg="#282c34")
frame3.pack(pady=10, fill=tk.X)
text_label = tk.Label(frame3, text="Text to Convert:", font=("Arial", 12), bg="#282c34", fg="white")
text_label.pack(anchor=tk.W, padx=10)
text_entry = tk.Text(frame3, font=("Arial", 12), height=5, width=60)
text_entry.pack(padx=10, pady=5)

# Progress bar and label
progress_frame = tk.Frame(root, bg="#282c34")
progress_frame.pack(pady=20)
progress = ttk.Progressbar(progress_frame, orient="horizontal", length=400, mode="determinate")
progress.pack()
progress_label = tk.Label(progress_frame, text="0%", font=("Arial", 12), bg="#282c34", fg="white")
progress_label.pack()

# Start button
start_button = tk.Button(root, text="Start Processing", command=process_video, font=("Arial", 12), bg="#98c379", fg="white")
start_button.pack(pady=10)

# Footer
footer_frame = tk.Frame(root, bg="#282c34")
footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
footer_label = tk.Label(footer_frame, text="AD Algo - Copyright 2024 | All rights reserved", font=("Arial", 10), bg="#282c34", fg="white")
footer_label.pack()

root.mainloop()