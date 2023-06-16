from pydub import AudioSegment, silence

input_file = "files/output.wav"
output_prefix = "files/output"

# 分割後のファイルの秒数
max_length = 1000
# 無音の長さ（ミリ秒）
min_silence_len = 1000
# 無音判定の閾値
silence_thresh = -50

# 入力ファイルを読み込んで無音部分を検出する
audio = AudioSegment.from_file(input_file)
silences = silence.detect_silence(audio, min_silence_len, silence_thresh, 100)

# 分割点を決定
split_points = []
prev_time_start = 0
prev_time_end = 0
for i in range(len(silences) - 1):
    # 閾値以上の無音時間があるか
    if silences[i][1] - silences[i][0] >= min_silence_len:
        # 前回の分割ポイントから分割時間に収まってるか
        if silences[i][1] - prev_time_end < max_length * 1000:
            continue

        # 前回の分割ポイントから分割時間を超えているので
        if len(split_points) <= 1:
            prev_time_start = 0
            prev_time_end = min(silences[i][0] + 100, len(audio))
        else:
            prev_time_start = prev_time_end + 500
            prev_time_end = min(prev_time_start + max_length * 1000, len(audio))

    # 分割ポイントを配列に格納
    split_points.append(prev_time_start)
    split_points.append(prev_time_end)

# 末尾も配列に格納
if split_points[-1] != len(audio):
    split_points.append(len(audio))

print(list(split_points))

# ファイルを書き込む
for i in range(len(split_points) - 1):
    start = split_points[i]
    end = split_points[i + 1]
    segment = audio[start:end]
    print(f"start: {start}, end: {end}")

    output_file = f"{output_prefix}_{format(i+1)}.mp3"
    segment.export(output_file, format="mp3")
    print("export:" + output_file)
