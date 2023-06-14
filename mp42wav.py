from moviepy.editor import VideoFileClip

def convert_mp4_to_wav(mp4_file, wav_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(wav_file, codec='pcm_s16le')

mp4_file = "files/input.mp4"
wav_file = "files/output.wav"

convert_mp4_to_wav(mp4_file, wav_file)