#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Este script transcribe archivos de audio a texto utilizando el modelo Whisper de OpenAI.
# 
# Uso:
#   -i, --input: Ruta del archivo de entrada (formato MP4 o similar).
#   -o, --output: Ruta del archivo de texto de salida.
#   -m, --model: Modelo Whisper a utilizar (tiny, base, small, medium, large).
#   Ejemplo de uso:
#       python3 Oratio2.py -i first_meeting.mp4 -o salida12.txt -m base
#
# Dependencias necesarias:
#   - whisper: Para la transcripción (instalable con `pip install openai-whisper`).
#   - torch: Necesario para que Whisper funcione (instalable con `pip install torch`).
#   - tqdm: Para las barras de progreso (instalable con `pip install tqdm`).
# By Angelo Armijos Carrion
import argparse
import whisper
from tqdm import tqdm
import os
import logging
import torch

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transcribe_audio_whisper(model, audio_file, output_file):
    """Transcribe un archivo de audio usando Whisper y guarda el resultado en un archivo de texto."""
    try:
        # Usar tqdm para mostrar barra de progreso
        with tqdm(total=100, desc="Transcribiendo audio", ncols=100) as pbar:
            result = model.transcribe(audio_file)
            pbar.update(100)  # Actualizar la barra de progreso al 100% cuando termine la transcripción
        text = result['text']
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        logging.info(f"Transcripción completada y guardada en {output_file}")
    except Exception as e:
        logging.error(f"Error durante la transcripción: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description='Transcribe audio de MP4 a texto usando Whisper')
    parser.add_argument('-i', '--input', required=True, help='Ruta del archivo de audio de entrada (MP4, WAV, etc.)')
    parser.add_argument('-o', '--output', required=True, help='Ruta del archivo de texto de salida')
    parser.add_argument('-m', '--model', default='base', help='Modelo Whisper a utilizar (tiny, base, small, medium, large)')
    args = parser.parse_args()

    # Verificar que el archivo de entrada existe
    if not os.path.exists(args.input):
        logging.error(f"Error: El archivo de entrada no existe: {args.input}")
        return

    # Cargar el modelo de Whisper
    logging.info("Cargando modelo Whisper...")
    model = whisper.load_model(args.model, device="cuda" if torch.cuda.is_available() else "cpu")

    # Transcribir el audio
    logging.info("Iniciando transcripción del audio...")
    transcribe_audio_whisper(model, args.input, args.output)

if __name__ == "__main__":
    main()
