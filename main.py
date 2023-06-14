import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

file = open("files/output_sample.wav", "rb")

transcript = openai.Audio.transcribe(
    model="whisper-1",
    file=file,
    response_format="srt"
)

# transcriptをテキストファイルに書き込む
output_file = "transcript.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(transcript)

# print(transcript)
