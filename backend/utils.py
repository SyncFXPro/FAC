#Utils, taking the audio and putting inside a tensor for  the model to interpert!

import librosa #maybe this is needed?

import numpy
FILE_PATH = "assets/audio/test.mp3"
def load_audio_file(file_path):
    print("Nothing yet!")
    pass

import kagglehub
def download_dataset():
    print("Nothing yet!")
# Download latest version
try:
    path = kagglehub.dataset_download("mohammedabdeldayem/the-fake-or-real-dataset", output_dir="H:/FAC/Dataset", force_download=True)
    print("Path to dataset files:", path)
except Exception as e:
    print("Error downloading dataset:", e)
    pass
    pass

def main():
    try:
        download_dataset()
    except Exception as e:
        print("Error downloading dataset:", e)
        pass
    pass

if __name__ == "__main__":
    main()