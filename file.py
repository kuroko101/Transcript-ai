# importing libraries 
from tkinter import N
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import PySimpleGUI as sg
import os.path
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from textwrap import wrap
import smtplib
from email.message import EmailMessage
def main():
    pathForConvert = str
    # First the window layout in 2 columns
    # First the window layout in 2 columns
    File_Choosing_Column = [
        [
            sg.Text("Audio Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]
    # For now will only show the name of the file that was chosen
    Transcript_Viewer = [
        [sg.Text("Choose an Audio file from the list on the left:")],
        [sg.InputText(key='text1')],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-WAVF-")],
    ]
    # ----- Full layout -----
    layout = [
        [
            [sg.Text("Transcript any audio (Must be in WAV format)")],
            [sg.Button("Exit"), sg.Button("Run")],
            [sg.Text("________________________________________________       _______________________________________________")],
            sg.Column(File_Choosing_Column),
            sg.VSeperator(),
            sg.Column(Transcript_Viewer),
        ]
    ]
    # Create the window
    window = sg.Window("Transcriptor", layout)
    # Create an event loop
    while True:
        event, values = window.read()
                # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".wav", ".mp3", ".aac", ".aiff", ".flac", ".m4a", ".ogg", ".pcm", ".wma"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                path = filename
            except:
                pass
        if event == "Exit":
            window.close()
            break
        if event == "Run":
            whole_text = RunIt(path)
            whole_text = wrap(whole_text, 58)
            eachInASeparateLine = "\n".join(whole_text)
            whole_text = eachInASeparateLine
            window["text1"].update(whole_text)
            # content
            sender = "NotifAccForPy@gmail.com"
            reciever = "clintfordcadio@gmail.com"
            password = "ldhjjzjcffqqdizu"
            msg_body = ("Here is your completed transcription: \n\n" + eachInASeparateLine)
            # action
            msg = EmailMessage()
            msg['subject'] = 'Text Transcription complete'   
            msg['from'] = sender
            msg['to'] = reciever
            msg.set_content(msg_body)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender,password)
                smtp.send_message(msg)
        elif event == sg.WIN_CLOSED:
            break
def RunIt(path):
    path = path.replace("\\", "/", 1)
    if path.endswith(".mp3"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".mp3",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal
    
    if path.endswith(".m4a"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".m4a",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal
    
    if path.endswith(".aac"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".aac",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal

    if path.endswith(".aiff"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".aiff",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal
    
    if path.endswith(".flac"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".flac",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal
    
    if path.endswith(".ogg"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".ogg",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal
    
    if path.endswith(".wma"):
        newPathList = path.split("\\")
        newPathString = newPathList[-1]                
        from os import path
        import pydub
        # files                                                                         
        src = newPathString
        newPathList2 = newPathString.split("/")
        newPathString2 = newPathList2[-1]
        newPathString2 = newPathString2.replace(".wma",".wav",1)
        del newPathList2[-1]
        newPathList2.append(newPathString2)
        newPathString3 = "/".join(newPathList2)
        newFilenameStringWAVFinal = newPathString3
        dst = newFilenameStringWAVFinal
        # convert wav to mp3                                                            
        sound = pydub.AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        path = newFilenameStringWAVFinal

    # create a speech recognition object
    r = sr.Recognizer()
    # a function that splits the audio file into chunks
    # and applies speech recognition
    # Splitting the large audio file into chunks
    # and apply speech recognition on each of these chunks
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = newPathString2
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language="fr")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text
main()