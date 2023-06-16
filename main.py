import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

# "files" フォルダ内の "output_" で始まる wav ファイルを取得
wav_files = [file for file in os.listdir("files") if file.startswith("output_") and file.endswith(".mp3")]

# "outputs" フォルダが存在しない場合は作成
output_folder = "outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for wav_file in wav_files:
    wav_path = os.path.join("files", wav_file)
    print(wav_path)
    
    with open(wav_path, "rb") as file:
        # wav ファイルを transcript
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=file,
            response_format="srt"
        )
        
    # テキストファイルに書き込む
    txt_file = os.path.join(output_folder, f"{os.path.splitext(wav_file)[0]}.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"Transcript generated for {wav_file}. Result saved in {txt_file}.")
