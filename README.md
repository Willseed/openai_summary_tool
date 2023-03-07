# Text summarization tool

> [正體中文版請點我](./README_zh-TW.md)

## Installation before use

> "Since downloading YouTube audio files requires FFmpeg as the underlying conversion package, FFmpeg needs to be installed and the environment variables need to be configured first."

### Windows installation instructions

[Reference for installation](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)

### MacOs installation instructions

```bash
brew install ffmpeg
```

### Linux installation instructions

#### Ubuntu

```bash
sudo apt update && sudo apt upgrade
```

```bash
sudo apt install ffmpeg
```

#### Fedora or RHEL

[Installation reference](https://computingforgeeks.com/how-to-install-ffmpeg-on-centos-rhel-8/)

## Apply for API keys on the OpenAI official website

[Click here to apply](https://platform.openai.com/account/api-keys)

After obtaining the key, create a text file key.txt and place the key in key.txt.

## Install Python-related packages

This project uses poetry as a Python management package, so poetry needs to be installed.

[Official installation document](https://python-poetry.org/docs/)

> Execute the following command to install all packages.

```bash
poetry install
```

> Enter the poetry virtual environment

```bash
poetry shell
```

## Summary source

### Set the YouTube URL in main.py

> Set the YouTube link you want to download.

```python
url = 'https://youtu.be/fPBNGLghVLU'
prefix = 'audio'
suffix = '.mp3'
```

> Run the main program

```bash
python main.py
```
