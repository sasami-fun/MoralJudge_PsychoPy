from psychopy import visual, core, event, gui
import random
import csv
import pathlib
import datetime
import textwrap
#import pandas as pd

subj_info = {"参加者ID":'', "年齢":'', "性別": ["男性", "女性", "その他", "未回答"]}

info_dlg = gui.DlgFromDict(subj_info)

if not info_dlg.OK:
   core.quit()


subjID = subj_info["参加者ID"]
age = subj_info["年齢"]
gender = subj_info["性別"]

sentence = []
with open('stims_v2.csv','r', encoding = 'utf-8-sig') as f:
    reader = csv.reader(f)
    header = reader.__next__()

with open('stims_v2.csv','r', encoding = 'utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        sentence.append(row)

win = visual.Window()

sentence_stim = visual.TextStim(win) 
random.shuffle(sentence)


current_folder = pathlib.Path(__file__).parent
new_filename = "{}_{}_{}_{}.csv".format(subjID,age,gender,subjID,datetime.date.today())
new_filepath = current_folder/"data"/new_filename

datafile = open(new_filepath, mode = 'a')
datafile.write('TimeStamp, Status/Key\n')

stopwatch = core.Clock()
timeStamped = stopwatch

for line in range(0,52):
    for column in range(1, 7):
        text = textwrap.wrap(sentence[line][column],20)
        sentence_stim = visual.TextStim(win, '\n'.join(text))
        sentence_stim.draw()
        win.flip()
        data = '{},{}-{}\n'.format(stopwatch.getTime(),sentence[line][0],header[column] )
        datafile.write(data)
        
        if column > 5:
            resp = event.waitKeys(keyList = ['right','left','escape'], timeStamped = stopwatch)
            key, rt = resp[0]
            if key == 'escape': 
                datafile.close() 
                core.quit()
            data = '{},{}\n'.format(rt, key)
            datafile.write(data)

        else:
            resp = event.waitKeys(keyList = ['space','escape'], timeStamped = stopwatch)
            data = '{},{}\n'.format(timeStamped,header[column])
            key, rt = resp[0]
            if key == 'escape': 
                datafile.close() 
                core.quit()
            data = '{},{}\n'.format(rt, key)
            datafile.write(data)

datafile.close()
win.close()