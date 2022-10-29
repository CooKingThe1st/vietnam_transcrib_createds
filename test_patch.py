import re
import time
from datetime import datetime
from bisect import bisect_left
import glob
import speech_recognition as sr
import MED
import os

from pydub import AudioSegment
from pydub.playback import play

alarm_song =AudioSegment.from_mp3('beep.mp3') 
exit_song = AudioSegment.from_mp3('exit.mp3')

class GenTranscribe:
    def __init__(self, gold_path, corpus_base_name):
        self.gold_path = gold_path

        self.gold_corpus = self.clean_text(self.read(self.gold_path, is_corpus = 1))
        self.gold_array_corpus = self.gold_corpus.split(' ')
        self.gold_limit = len(self.gold_array_corpus)
        # print(self.gold_corpus)

        self.speech_corpus_list = glob.glob(corpus_base_name)
        self.speech_corpus_list.sort()
        # print(self.speech_corpus_list)

        self.recog = sr.Recognizer()

    def google_noise_text(self, audio_path):
        with sr.AudioFile(audio_path) as source:
            audio = self.recog.record(source)  # read the entire audio file
        return self.recog.recognize_google(audio, language = 'vi-VN').split()

    def read(self, path, is_corpus):
        tmp_buffer = ""
        with open(path, encoding='utf-8') as f:
            tmp_buffer = [line.strip().split('\n') for line in f]
        if not (is_corpus): return tmp_buffer
        corpus = ""
        for line in tmp_buffer:
            if (len(line[0]) == 0):
                corpus += " "
            else:
                corpus += str(line[0])

        return corpus

    def clean_text(self, input_text):
        _pre_ = re.sub('\W+\s*', ' ', input_text)
        # print(input_text + '\n' + _pre_)

        regex_sub = re.sub(r"\s+", ' ', _pre_)  # Replaces any number of spaces with one space
        # print(regex_sub)  # looks good
        return regex_sub

    def auto_gen_transcrib(self):
        check_point = 0
        estimate_length = 200 # 15sec, each sec 3 word
        pad = 10
        bad_conscecutive_counter = 0
        if (check_point == 0): estimate_length = 600 # head start

        for speech_corpus in self.speech_corpus_list:
            noisies = self.google_noise_text(speech_corpus)
            pre_result = MED.med_para(self.gold_array_corpus[max(0, check_point): min(check_point + estimate_length, len(self.gold_array_corpus))], noisies, allow_delete = 1)

            suffix = "_raw"
            if (pre_result[2] > 10):
                print("UHHH OHHHH")
                print("WITH OVERLOAD ", ' '.join(pre_result[0]))
                play(alarm_song)
                suffix = "_error"
                bad_conscecutive_counter += 1
                estimate_length = 500
                if (bad_conscecutive_counter >= 3):
                    play(exit_song)
                    print("BIG UH OHHHHHHHHHHHHHHHHHHhh")
                    break
            else:
                estimate_length = 200
                bad_conscecutive_counter = 0
                if (pre_result[2] == 0): suffix = "_good"
                elif (pre_result[2] < 4): suffix = "_raw_small"
                
            result = MED.med_para(self.gold_array_corpus[max(0, check_point): min(check_point + estimate_length, len(self.gold_array_corpus))], noisies, allow_delete = 0)
            base_name = os.path.basename(speech_corpus)
            transcrib_file = os.path.join(os.path.dirname(speech_corpus),  os.path.splitext(base_name)[0] + suffix + ".txt")
            print("Google get ", ' '.join(noisies))
            print("From check point " ,check_point, " get ",  ' '. join(self.gold_array_corpus[max(0, check_point): min(check_point + estimate_length, len(self.gold_array_corpus))]))
            print("ESTIMATED ", speech_corpus, " with error ", result[2], " at index ", result[1], " and save at ", transcrib_file)  
        

            check_point += result[1] - pad
            with open(transcrib_file, 'w') as transcrib:
                transcrib.write('  '.join(result[0])) 


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--gold_corpus_path', type=str,
                        required=True, help='input gold corpus path')
    parser.add_argument('--speech_corpus_base_name', type=str,
                        required=True, help='input speech corpus name')
    # parser.add_argument('--forced_google', type=int, 
    #                     required=True, help='forced using google when too wrong')

    args = parser.parse_args()

    module = GenTranscribe(args.gold_corpus_path, args.speech_corpus_base_name)
    module.auto_gen_transcrib()
