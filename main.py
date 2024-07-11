import pygame
import time

# Khởi tạo pygame và thiết lập mixer
pygame.init()
pygame.mixer.init()

# Định nghĩa đường dẫn tệp âm thanh
audio_path = "./Piano/"

# Tạo từ điển ánh xạ từ nốt nhạc sang tên file
note_files = {f"{note}": f"{i}.mp3" for i, note in enumerate(
    ["A0", "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1",
     "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3",
     "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4",
     "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6",
     "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6", "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7",
     "G#7", "A7", "A#7", "B7", "C8"], 1)}

# Tải và lưu trữ các âm thanh
sounds = {note: pygame.mixer.Sound(audio_path + file) for note, file in note_files.items()}

# Số lượng kênh âm thanh cố định
num_channels = 8
channels = [pygame.mixer.Channel(i) for i in range(num_channels)]

# Hàm phát một nốt nhạc trên kênh riêng biệt
def play_note(note, channel_index):
    sound = sounds.get(note)
    if sound:
        channels[channel_index].play(sound)

def play_song(song, delays):
    start_time = time.time() * 1000
    next_play_time = start_time

    for i, (note, delay) in enumerate(zip(song, delays)):
        next_play_time += delay
        while time.time() * 1000 < next_play_time:
            time.sleep(0.01)
        play_note(note, i % num_channels)

song = ["G4", "A4", "G4", "E5", "C5", "D5", "E5", "D5", "C5", "C5", "D5", "E5", "D5", "C5",
        "A4", "G4", "E5", "D5", "C5", "D5", "G4", "A4", "C5", "A4", "E5", "D5", "D5", "E5", "D5", "C5",
        "D5", "E5", "D5", "C5", "A4", "E5", "D5", "C5", "E5", "D5", "E5", "D5",
        "C5", "A4", "C5", "G4", "C5", "D5", "E5", "E5", "D5", "E5", "D5", "C5", "A4", "C5", "G4", "C5", "D5", "D5"]

delays = [350, 350, 350, 350, 1400, 250, 350, 350, 350, 1400, 250, 350, 350, 350,
          700, 700, 350, 350, 350, 350, 1700, 250, 350, 350, 350, 1400, 250, 350, 350, 350,
          1700, 350, 350, 350, 700, 1050, 350, 350, 350, 700, 700, 700,
          700, 350, 350, 350, 350, 350, 700, 1050, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350]

play_song(song, delays)
