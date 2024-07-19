# Transcribe

A Python application that transcribes M4A audio files, outputs the transcript to a specific directory structure, and includes additional features such as system integration and file tagging using OpenAI's GPT-3.5 model.

## Installation

1. Ensure you have Python 3 and Git installed on your system.

2. Run the following command in your terminal:

   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/davidmoore-io/transcribe/main/install.sh)"
   ```

   This will clone the repository, set up a virtual environment, install dependencies, and create necessary configuration files.

3. After installation, restart your terminal or run:

   ```bash
   source ~/.zshrc  # or ~/.bash_profile or ~/.bashrc, depending on your shell
   ```

4. Set your OpenAI API key in your environment:

   ```bash
   echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```

   Replace `your-api-key-here` with your actual OpenAI API key.

## Usage

To transcribe an audio file, use the following command:

```bash
transcribe /path/to/your/audio_file.m4a
```

The transcript will be saved in `~/Documents/Transcripts/[filename]/[filename]-[timestamp].txt`, and the directory will be opened automatically.

## Features

- High-quality transcription using the Whisper large model
- Automatic file tagging using OpenAI's GPT-3.5 model
- Convenient command-line interface
- Automatic directory opening after transcription

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License

Copyright (c) 2023 David Moore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

For more information, please visit [davidmoore.io](https://davidmoore.io).
