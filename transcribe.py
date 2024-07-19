import os
import sys
import datetime
import subprocess
import logging
from pathlib import Path
import yaml
from openai import OpenAI
from pydub import AudioSegment
import xattr

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    config_path = Path.home() / '.transcribe_config.yaml'
    if not config_path.exists():
        raise FileNotFoundError("Configuration file not found. Please run the installation script.")
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)

def transcribe_audio(audio_path, client):
    logging.info(f"Transcribing {audio_path}")
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcript.text

def save_transcript(transcript, output_dir, filename):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = output_dir / f"{filename}-{timestamp}.txt"
    with open(output_path, 'w') as f:
        f.write(transcript)
    logging.info(f"Transcript saved to {output_path}")
    return output_path

def analyze_content(transcript, client):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates relevant tags for a given transcript."},
                {"role": "user", "content": f"Please generate 3-5 relevant tags for the following transcript, separated by commas:\n\n{transcript[:1000]}..."}
            ]
        )
        tags = response.choices[0].message.content.split(',')
        return [tag.strip() for tag in tags]
    except Exception as e:
        logging.error(f"Error using OpenAI API: {e}")
        return ["transcript"]

def add_tags(file_path, tags):
    for tag in tags:
        xattr.setxattr(file_path, f"user.tag.{tag}", b"")
    logging.info(f"Added tags: {', '.join(tags)}")

def main(audio_path):
    config = load_config()
    output_dir = Path(config['output_directory']) / 'transcripts' / Path(audio_path).stem
    output_dir.mkdir(parents=True, exist_ok=True)
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Convert M4A to WAV if necessary
    if audio_path.lower().endswith('.m4a'):
        wav_path = audio_path.rsplit('.', 1)[0] + '.wav'
        AudioSegment.from_file(audio_path, format="m4a").export(wav_path, format="wav")
        audio_path = wav_path

    transcript = transcribe_audio(audio_path, client)
    output_path = save_transcript(transcript, output_dir, Path(audio_path).stem)
    
    tags = analyze_content(transcript, client)
    add_tags(output_path, tags)

    # Open the directory containing the transcript
    subprocess.run(["open", output_dir])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: transcribe <audio_file_path>")
        sys.exit(1)
    
    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"Error: File '{audio_path}' not found.")
        sys.exit(1)

    main(audio_path)