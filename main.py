from psychopy import visual, core, event, gui
import random
import pathlib
import datetime

subj_info = {"参加者ID":'', "年齢":'', "性別": ["男性", "女性", "その他", "未回答"]}

info_dlg = gui.DlgFromDict(subj_info)

if not info_dlg.OK:
   core.quit()


subjID = subj_info["参加者ID"]
age = subj_info["年齢"]
gender = subj_info["性別"]

win = visual.Window()

letter_stim = visual.ImageStim(win) 
letter_pos = [["stim1.png",0]]


current_folder = pathlib.Path(__file__).parent
new_filename = "{}_{}.csv".format(subjID,datetime.date.today()) 
new_filepath = current_folder/"data"/new_filename

datafile = open(new_filepath, mode = 'a')
datafile.write('ID, age, gender, trialID, stim, pos, respKey, respTime\n')

trialID = 0

stopwatch = core.Clock()

for letter, x_axis in letter_pos:
    photo = visual.ImageStim(win,"stim1.png")
    letter_stim.setPos([x_axis, 0])
    photo.draw()
    win.flip()

    stopwatch.reset()
    resp = event.waitKeys(keyList = ['left', 'right', 'escape'], timeStamped = stopwatch)

    key, rt = resp[0]
    if key == 'escape': 
        datafile.close() 
        core.quit()

    data = '{},{},{},{},{},{},{},{}\n'.format(subjID, age, gender, trialID, letter, x_axis, key, rt) # subjID, age, sexを追加
    datafile.write(data)

    trialID = trialID + 1

datafile.close()
win.close()