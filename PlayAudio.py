from playsound import playsound
import wave
from os import listdir
from os.path import isfile, join
import os
import shutil

filepath = os.getcwd()
filepath = filepath + '\\KsponSpeech_01_wav\\KsponSpeech_0001_wav'
files = [f for f in listdir(filepath) if isfile(join(filepath, f))]

files = [ x for x in files if x.find(".wav") != -1]
print(os.getcwd())
print(filepath)
for i in range(len(files)):
    new_file_name =''
    gender = 9
    age = 9
    emotion = 9
    while True:
        playsound(filepath + "\\" + files[i], True)
       
        gender = input('성별을 입력하시오 남자: 1 , 여자 : 2         ::: ')
        
        if gender == "1":
            print(" 성별 : 남자")
            print_gender = "남자"
            break
        elif  gender == "2":
            print(" 성별 : 여자")
            print_gender = "여자"
            break
        else:
            continue
    while True:
        print('나이대를 입력하시오 아이: 1 , 젊은사람 : 2 , 나이 많은 사람 : 3          :::  ', end="")
        age = input()
        if age == '1':
            print(" 아이 ")
            print_age = "아이"
            break
        elif  age == '2':
            print(" 젊은 사람")
            print_age = "젊은 사람"
            break
        elif age == '3':
            print(" 나이 많은 사람")
            print_age  = "나이 많은 사람"
            break
        else:
            continue
    while True:
        print('감정상태를 입력하시오  1: 암 생각 없음 2: 행복 3: 슬픔 4: 화남 5: 짜증 6: 놀람         ::: ', end="")
        emotion = input()
        if emotion == '1':
            print(" 아무 생각 없음 (일상) ")
            print_emotion = "아무생각 없음(일상)"
            break
        elif emotion == '2':
            print(" 행복")
            print_emotion = "행복"
            break
        elif emotion == '3':
            print(" 슬픔")
            print_emotion = "슬픔"
            break
        elif emotion == '4':
            print(" 화남")
            print_emotion = "화남"
            break
        elif emotion == '5': 
            print(" 짜증")
            print_emotion = "짜증"
            break
        elif emotion == '6':
            print( "놀람")
            print_emotion = "놀람"
            break
   
        else:
            continue
    print("성별 : ", print_gender , "나이 : ", print_age, "감정 : ", print_emotion,  end='')
    file_name = files[i]
    string_gender = '0' + str(gender)
    string_age = '0' + str(age)
    string_emotion = '0' + str(emotion)
    
    add_string = '-' + string_gender + '-'+ string_age + '-' + string_emotion + '.wav'
    new_file_name = file_name.replace('.wav', add_string)
    print("변경 전 파일명  : ", files[i])
    print("변경 후 파일명  : ", new_file_name)


    src_dir=  filepath +  "\\" + files[i]  
    dst_dir= os.getcwd() + "\\detect_speech_01\\detect_speech_0001" + new_file_name
    
    shutil.copy(src_dir,dst_dir)
