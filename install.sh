#!/bin/bash

set -e

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git and try again."
    exit 1
fi

# Clone the repository
git clone https://github.com/davidmoore-io/transcribe.git ~/.transcribe

# Change to the transcribe directory
cd ~/.transcribe

# Create virtual environment
python3 -m venv ~/.transcribe_env

# Activate virtual environment
source ~/.transcribe_env/bin/activate

# Install required packages
pip install -r requirements.txt

# Create configuration file
cat > ~/.transcribe_config.yaml << EOL
output_directory: ~/Documents/Transcripts
EOL

# Create alias in .zshrc or .bash_profile
if [ -f ~/.zshrc ]; then
    SHELL_RC=~/.zshrc
elif [ -f ~/.bash_profile ]; then
    SHELL_RC=~/.bash_profile
else
    SHELL_RC=~/.bashrc
fi

echo "alias transcribe='source ~/.transcribe_env/bin/activate && python3 ~/.transcribe/transcribe.py'" >> $SHELL_RC

echo "Installation complete. Please restart your terminal or run 'source $SHELL_RC' to use the 'transcribe' command."
echo "IMPORTANT: Make sure to set your OpenAI API key in your environment variables:"
echo "export OPENAI_API_KEY='your-api-key-here'"
