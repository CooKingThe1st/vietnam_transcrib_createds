import speech_recognition as sr

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--speech_corpus', type=str,
                        required=True, help='input audio to cut')
    parser.add_argument('--output_name', type=str,
                        required=False, help='output base name')
    parser.add_argument('--silence', type=int, default=600,
                        required=False, help='silence detect')
    parser.add_argument('--chunk_limit', type=int, default=15,
                        required=False, help='max len chunk')
    parser.add_argument('--pad', type=int, default=300,
                        required=False, help='chunk padding')
    args = parser.parse_args()

    #reading from audio mp3 file
    import pathlib
    audio_suffix = pathlib.Path(args.speech_corpus).suffix
    if (audio_suffix == '.wav'):
        sound = AudioSegment.from_wav(args.speech_corpus)
    elif (audio_suffix == '.mp3'):
        sound = AudioSegment.from_mp3(args.speech_corpus)
    elif (audio_suffix == '.ogg'):
        sound = AudioSegment.from_mp3(args.speech_corpus)
    else:
        print("UNKNOWN AUDIO EXTENSION, QUITTING ....")
        exit()

    # spliting audio files
    CHUNK_SIZE = args.chunk_limit
    SILENCE_SIZE = args.silence
    audio_chunks = split_on_silence(sound, min_silence_len=SILENCE_SIZE, silence_thresh=-40 )
    #loop is used to iterate over the output list
    small_pad = AudioSegment.silent(duration = args.pad)
    silence_pad =  AudioSegment.silent(duration = SILENCE_SIZE)
    current = small_pad
    counter = 0

    base_dir = os.path.dirname(args.speech_corpus)
    output_name = os.path.splitext(os.path.basename(args.speech_corpus))[0] + '_split'
    if args.output_name is not None:
        output_name = args.output_name

    for i, chunk in enumerate(audio_chunks):
        if (current.duration_seconds + chunk.duration_seconds) <= CHUNK_SIZE:
            if (counter == 0): 
                current = current + chunk
            else:
                current = current + silence_pad + chunk
        else:
            output_file = "{2}/{1}_{0:04d}.wav".format(counter, output_name, base_dir)
            counter += 1
            current = current + small_pad
            current.export(output_file, format="wav")

            current = small_pad + chunk

    output_file = "{2}/{1}_{0:04d}.wav".format(counter, output_name, base_dir)
    counter += 1
    current = current + small_pad
    current.export(output_file, format="wav")