import whisper

model = whisper.load_model("base")  # или "small", "medium", "large"
result = model.transcribe("audio.mp3", language="russian")

print(result["text"])

with open("out.txt", 'w', encoding='utf-8') as file:
    file.write(result["text"])
