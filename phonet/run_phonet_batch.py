import os
from app import main

for root, dirs, files in os.walk("pcgita"):
    for file in files:
        if file.endswith(".wav"):
            audio_path = os.path.join(root, file)
            result_path = os.path.join(root, file.replace(".wav", ".csv"))
            data = main(audio_path)
            data.to_csv(result_path, index=False)
            print(f"File {file} processed and saved to {result_path}")