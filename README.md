# Oratio2: Audio to Text Transcription Tool

**Oratio2** is a Python-based script that allows you to convert audio files into text using OpenAI's Whisper model. This script is designed to be simple, fast, and user-friendly, providing a straightforward way to transcribe your audio into written text. Below you will find detailed instructions on how to use it, along with descriptions of all the parameters.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Parameters](#parameters)
6. [Recommendations](#recommendations)
7. [Example](#example)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

Oratio2 is built to transcribe MP4, WAV, and other supported audio formats into text. It uses OpenAI's Whisper, a state-of-the-art audio recognition model. The transcription is easy to use, customizable by selecting different Whisper models, and provides progress indicators to keep track of the transcription.

## Requirements

Before using **Oratio2**, make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- Whisper: To transcribe the audio (`pip install openai-whisper`)
- Torch: Required for Whisper (`pip install torch`)
- tqdm: For progress bars (`pip install tqdm`)

## Installation

To install the necessary packages, run the following commands:

```sh
pip install openai-whisper
pip install torch
pip install tqdm
```

These commands will ensure all dependencies are installed and ready to use with **Oratio2**.

## Usage

To use the **Oratio2** script, you will need to provide an audio file and specify an output file for the transcribed text. Below is the command syntax:

```sh
python3 Oratio2.py -i <input_audio_file> -o <output_text_file> -m <model>
```

### Example Command

```sh
python3 Oratio2.py -i first_meeting.mp4 -o transcription.txt -m base
```

This command will transcribe the audio file `first_meeting.mp4` into a text file named `transcription.txt` using the "base" Whisper model.

## Parameters

### `-i`, `--input`
- **Description**: Specifies the path of the input audio file to transcribe.
- **Format**: The audio file can be in MP4, WAV, or any other format supported by Whisper.
- **Required**: Yes.

### `-o`, `--output`
- **Description**: Specifies the path of the output text file where the transcription will be saved.
- **Format**: Provide a `.txt` file where you want the results.
- **Required**: Yes.

### `-m`, `--model`
- **Description**: Specifies which Whisper model to use.
- **Options**: `tiny`, `base`, `small`, `medium`, `large`.
  - **tiny**: Fastest, lower accuracy.
  - **base**: Good balance of speed and accuracy.
  - **small**: More accurate but slower.
  - **medium**: Better accuracy for larger files.
  - **large**: Highest accuracy but slowest.
- **Default**: `base`.

## Recommendations

1. **Model Selection**: Use `tiny` or `base` for fast transcriptions when high accuracy isn't crucial. Use `medium` or `large` for detailed and accurate transcriptions.
2. **Audio Quality**: For the best results, ensure your audio file is clear, with minimal background noise.
3. **Environment**: If you have a GPU available, Whisper can run significantly faster. Make sure your `torch` installation is configured to use CUDA if applicable.
4. **Output File Location**: Always provide a full path for the output file if running from different directories to avoid confusion.

## Example

The following is an example of how to use **Oratio2** to transcribe an audio file:

```sh
python3 Oratio2.py -i /path/to/audio.mp4 -o /path/to/output.txt -m large
```

This command will transcribe the given audio file with the `large` model for the best possible accuracy.

## Troubleshooting

- **File Not Found**: If you encounter an error stating "Error: The input file does not exist", verify the file path you provided for the input audio.
- **Slow Processing**: If the transcription is slow, consider using a smaller model (`tiny` or `base`) or running the script on a machine with a GPU.
- **Warnings**: If you see warnings about `FP16` not being supported on CPU, it is because the script defaults to FP32 when running on CPU. This warning is safe to ignore.

For any further questions or issues, feel free to open an issue on the GitHub repository.

---

**Enjoy using Oratio2 to easily convert your audio files to text!**

