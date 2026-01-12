import sounddevice as sd
from scipy.io import wavfile
import numpy as np

# Parámetros de audio
samplerate = 16000  # Hz
duration = 5        # segundos
channels = 1
output_file = "audio_autorizacion.wav"

try:
    print("🔊 Configurando grabación de audio...")
    print("Hable claro y con la menor interferencia posible.")
    print("🎧 Grabando audio...")

    # Grabar audio
    audio = sd.rec(int(duration * samplerate),
                   samplerate=samplerate,
                   channels=channels,
                   dtype='int16',device=1)
    sd.wait()

    print("✅ Grabación finalizada.")
    print(f"Forma de onda capturada: {audio.shape}")

    # Convertir a mono si hay más de un canal
    if audio.ndim > 1 and audio.shape[1] > 1:
        print("🔄 Convirtiendo a mono...")
        audio = np.mean(audio, axis=1).astype('int16')

    # Guardar archivo
    wavfile.write(output_file, samplerate, audio)
    print(f"💾 Archivo guardado como: {output_file}")

except sd.PortAudioError as e:
    print("❌ Error al acceder al dispositivo de audio:", e)
except Exception as e:
    print("⚠️ Ocurrió un error inesperado:", e)
