#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on August 12, 2022, at 23:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

'''
This BART is created by Jonanthan Peirce and made available on OSF https://osf.io/jfxsr/.
Date created: 2016-05-04 03:49 AM | Last Updated: 2019-09-12 02:32 AM

Category:  Project

Description: A simple version of the Balloon Analog Risk Task (BART) written in PsychoPy.

Evaluation of a behavioral measure of risk taking: The Balloon Analogue Risk Task (BART).
Lejuez, C. W.; Read, J. P.; Kahler, C. W.; Richards, J. B.; Ramsey, S. E.; Stuart, G. L.; Strong, D. R.; Brown, R. A.
Journal of Experimental Psychology: Applied, Vol 8(2), Jun 2002, 75-84. http://dx.doi.org/10.1037/1076-898X.8.2.75

It is later edited by Xi Yang for Oregon Sleep Lab from 3/30/22 to 8/12/22. 
Xi incorporated more ideas from the version used in Dr. Brant Hasler's lab (including the stimuli list and cashing out animation and sound effects). 

'''


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'BART'  # from the Builder filename that created this script
expInfo = {'participant': '', 'visit': '001/002'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\OSLadmin\\Desktop\\220330_BART\\220812_OSL_BART.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "start"
startClock = core.Clock()
start_text = visual.TextStim(win=win, name='start_text',
    text='BART',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_key_resp = keyboard.Keyboard()
start_text2 = visual.TextStim(win=win, name='start_text2',
    text='Press a to advance',
    font='Open Sans',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text="Now you're going to see 30 balloons, one after another, on the screen. For each balloon, you will press the SPACE key to pump up the balloon. Each press on the SPACE key pumps the balloon up a little more.\n\nBUT remember, balloons pop if you pump them up too much. It is up to you to decide how much to pump up each balloon. Some of these balloons might pop after just one pump. Others might not pop until they fill the whole screen.\n\nYou get MONEY for every pump. Each pump earns 1 cent. But if a balloon pops, you lose the money you earned on that balloon. To keep the money from a balloon, stop pumping before it pops and press the ENTER key to collect the cash for this balloon.\n\nAfter each time you collect the cash or pop a balloon, a new balloon will appear. \n\nAt the end of the experiment, you will be paid the amount earned on the game.\n\nPress a to advance.",
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_resp = keyboard.Keyboard()

# Initialize components for Routine "example_instruction"
example_instructionClock = core.Clock()
example_instruction_text = visual.TextStim(win=win, name='example_instruction_text',
    text="Let's see an example of task.\nAsk the experimenter any questions you have!\n\nPress a to advance this page.",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
example_instruction_key_resp = keyboard.Keyboard()

# Initialize components for Routine "example_instructions"
example_instructionsClock = core.Clock()
example_instructions_resp = keyboard.Keyboard()
bankedMsg_example = visual.TextStim(win=win, name='bankedMsg_example',
    text='',
    font='Arial',
    pos=[-.5, 0.8], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
reminderMsg_example = visual.TextStim(win=win, name='reminderMsg_example',
    text='Press SPACE to pump the balloon\nPress ENTER to collect this sum',
    font='Arial',
    pos=[.5, 0.8], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
example_instructions_image = visual.ImageStim(
    win=win,
    name='example_instructions_image', 
    image='redBalloon.png', mask=None, anchor='center',
    ori=270.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
example_instruction_text3 = visual.TextStim(win=win, name='example_instruction_text3',
    text='When you finish viewing the example, press a to advance.',
    font='Open Sans',
    pos=(0, -.8), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "check_instructions"
check_instructionsClock = core.Clock()
check_instructions_key_resp = keyboard.Keyboard()
check_instructioins_text = visual.TextStim(win=win, name='check_instructioins_text',
    text='You just saw an example of the task.\nIf you have no questions and are ready to begin the task,\npress a to advance. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
bankedEarnings=0.0
lastBalloonEarnings=0.0
thisBalloonEarnings=0.0
balloonSize=0.08
balloonMsgHeight=0.01
balloonBody = visual.ImageStim(
    win=win,
    name='balloonBody', 
    image='blueBalloon.png', mask=None, anchor='center',
    ori=270, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
reminderMsg = visual.TextStim(win=win, name='reminderMsg',
    text='Press SPACE to pump the balloon\nPress ENTER to collect this sum',
    font='Arial',
    pos=[.5, .8], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
bankedMsg = visual.TextStim(win=win, name='bankedMsg',
    text='',
    font='Arial',
    pos=[-.5, 0.8], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
bankButton = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbackText=""
display_value = 0
#from psychopy import sound
#bang = sound.Sound("bang_22050Hz.wav")
#coin = sound.Sound("coin_22050Hz.wav")
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
bang_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='bang_sound')
bang_sound.setVolume(1.0)
coin_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='coin_sound')
coin_sound.setVolume(1.0)

# Initialize components for Routine "finalScore"
finalScoreClock = core.Clock()
finalScore_2 = visual.TextStim(win=win, name='finalScore_2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
doneKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
start_key_resp.keys = []
start_key_resp.rt = []
_start_key_resp_allKeys = []
# keep track of which components have finished
startComponents = [start_text, start_key_resp, start_text2]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        start_text.setAutoDraw(True)
    
    # *start_key_resp* updates
    waitOnFlip = False
    if start_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_key_resp.frameNStart = frameN  # exact frame index
        start_key_resp.tStart = t  # local t and not account for scr refresh
        start_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_key_resp, 'tStartRefresh')  # time at next scr refresh
        start_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_key_resp.getKeys(keyList=['a'], waitRelease=False)
        _start_key_resp_allKeys.extend(theseKeys)
        if len(_start_key_resp_allKeys):
            start_key_resp.keys = _start_key_resp_allKeys[-1].name  # just the last key pressed
            start_key_resp.rt = _start_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *start_text2* updates
    if start_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text2.frameNStart = frameN  # exact frame index
        start_text2.tStart = t  # local t and not account for scr refresh
        start_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text2, 'tStartRefresh')  # time at next scr refresh
        start_text2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_text.started', start_text.tStartRefresh)
thisExp.addData('start_text.stopped', start_text.tStopRefresh)
# check responses
if start_key_resp.keys in ['', [], None]:  # No response was made
    start_key_resp.keys = None
thisExp.addData('start_key_resp.keys',start_key_resp.keys)
if start_key_resp.keys != None:  # we had a response
    thisExp.addData('start_key_resp.rt', start_key_resp.rt)
thisExp.addData('start_key_resp.started', start_key_resp.tStartRefresh)
thisExp.addData('start_key_resp.stopped', start_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('start_text2.started', start_text2.tStartRefresh)
thisExp.addData('start_text2.stopped', start_text2.tStopRefresh)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instruction_resp.keys = []
instruction_resp.rt = []
_instruction_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instruction_text, instruction_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        instruction_text.setAutoDraw(True)
    
    # *instruction_resp* updates
    waitOnFlip = False
    if instruction_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_resp.frameNStart = frameN  # exact frame index
        instruction_resp.tStart = t  # local t and not account for scr refresh
        instruction_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_resp, 'tStartRefresh')  # time at next scr refresh
        instruction_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruction_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruction_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruction_resp.status == STARTED and not waitOnFlip:
        theseKeys = instruction_resp.getKeys(keyList=['a'], waitRelease=False)
        _instruction_resp_allKeys.extend(theseKeys)
        if len(_instruction_resp_allKeys):
            instruction_resp.keys = _instruction_resp_allKeys[-1].name  # just the last key pressed
            instruction_resp.rt = _instruction_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text.started', instruction_text.tStartRefresh)
thisExp.addData('instruction_text.stopped', instruction_text.tStopRefresh)
# check responses
if instruction_resp.keys in ['', [], None]:  # No response was made
    instruction_resp.keys = None
thisExp.addData('instruction_resp.keys',instruction_resp.keys)
if instruction_resp.keys != None:  # we had a response
    thisExp.addData('instruction_resp.rt', instruction_resp.rt)
thisExp.addData('instruction_resp.started', instruction_resp.tStartRefresh)
thisExp.addData('instruction_resp.stopped', instruction_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "example_instruction"-------
continueRoutine = True
# update component parameters for each repeat
example_instruction_key_resp.keys = []
example_instruction_key_resp.rt = []
_example_instruction_key_resp_allKeys = []
# keep track of which components have finished
example_instructionComponents = [example_instruction_text, example_instruction_key_resp]
for thisComponent in example_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
example_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "example_instruction"-------
while continueRoutine:
    # get current time
    t = example_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=example_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_instruction_text* updates
    if example_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_instruction_text.frameNStart = frameN  # exact frame index
        example_instruction_text.tStart = t  # local t and not account for scr refresh
        example_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_instruction_text, 'tStartRefresh')  # time at next scr refresh
        example_instruction_text.setAutoDraw(True)
    
    # *example_instruction_key_resp* updates
    waitOnFlip = False
    if example_instruction_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_instruction_key_resp.frameNStart = frameN  # exact frame index
        example_instruction_key_resp.tStart = t  # local t and not account for scr refresh
        example_instruction_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_instruction_key_resp, 'tStartRefresh')  # time at next scr refresh
        example_instruction_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(example_instruction_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(example_instruction_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if example_instruction_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = example_instruction_key_resp.getKeys(keyList=['a'], waitRelease=False)
        _example_instruction_key_resp_allKeys.extend(theseKeys)
        if len(_example_instruction_key_resp_allKeys):
            example_instruction_key_resp.keys = _example_instruction_key_resp_allKeys[-1].name  # just the last key pressed
            example_instruction_key_resp.rt = _example_instruction_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "example_instruction"-------
for thisComponent in example_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('example_instruction_text.started', example_instruction_text.tStartRefresh)
thisExp.addData('example_instruction_text.stopped', example_instruction_text.tStopRefresh)
# check responses
if example_instruction_key_resp.keys in ['', [], None]:  # No response was made
    example_instruction_key_resp.keys = None
thisExp.addData('example_instruction_key_resp.keys',example_instruction_key_resp.keys)
if example_instruction_key_resp.keys != None:  # we had a response
    thisExp.addData('example_instruction_key_resp.rt', example_instruction_key_resp.rt)
thisExp.addData('example_instruction_key_resp.started', example_instruction_key_resp.tStartRefresh)
thisExp.addData('example_instruction_key_resp.stopped', example_instruction_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "example_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "example_instructions"-------
continueRoutine = True
# update component parameters for each repeat
example_instructions_resp.keys = []
example_instructions_resp.rt = []
_example_instructions_resp_allKeys = []
# keep track of which components have finished
example_instructionsComponents = [example_instructions_resp, bankedMsg_example, reminderMsg_example, example_instructions_image, example_instruction_text3]
for thisComponent in example_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
example_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "example_instructions"-------
while continueRoutine:
    # get current time
    t = example_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=example_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_instructions_resp* updates
    waitOnFlip = False
    if example_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_instructions_resp.frameNStart = frameN  # exact frame index
        example_instructions_resp.tStart = t  # local t and not account for scr refresh
        example_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        example_instructions_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(example_instructions_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(example_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if example_instructions_resp.status == STARTED and not waitOnFlip:
        theseKeys = example_instructions_resp.getKeys(keyList=['a'], waitRelease=False)
        _example_instructions_resp_allKeys.extend(theseKeys)
        if len(_example_instructions_resp_allKeys):
            example_instructions_resp.keys = _example_instructions_resp_allKeys[-1].name  # just the last key pressed
            example_instructions_resp.rt = _example_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *bankedMsg_example* updates
    if bankedMsg_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bankedMsg_example.frameNStart = frameN  # exact frame index
        bankedMsg_example.tStart = t  # local t and not account for scr refresh
        bankedMsg_example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bankedMsg_example, 'tStartRefresh')  # time at next scr refresh
        bankedMsg_example.setAutoDraw(True)
    if bankedMsg_example.status == STARTED:  # only update if drawing
        bankedMsg_example.setText("You have collected:\n $%.2f" %bankedEarnings, log=False)
    
    # *reminderMsg_example* updates
    if reminderMsg_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        reminderMsg_example.frameNStart = frameN  # exact frame index
        reminderMsg_example.tStart = t  # local t and not account for scr refresh
        reminderMsg_example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reminderMsg_example, 'tStartRefresh')  # time at next scr refresh
        reminderMsg_example.setAutoDraw(True)
    
    # *example_instructions_image* updates
    if example_instructions_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_instructions_image.frameNStart = frameN  # exact frame index
        example_instructions_image.tStart = t  # local t and not account for scr refresh
        example_instructions_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_instructions_image, 'tStartRefresh')  # time at next scr refresh
        example_instructions_image.setAutoDraw(True)
    
    # *example_instruction_text3* updates
    if example_instruction_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_instruction_text3.frameNStart = frameN  # exact frame index
        example_instruction_text3.tStart = t  # local t and not account for scr refresh
        example_instruction_text3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_instruction_text3, 'tStartRefresh')  # time at next scr refresh
        example_instruction_text3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "example_instructions"-------
for thisComponent in example_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if example_instructions_resp.keys in ['', [], None]:  # No response was made
    example_instructions_resp.keys = None
thisExp.addData('example_instructions_resp.keys',example_instructions_resp.keys)
if example_instructions_resp.keys != None:  # we had a response
    thisExp.addData('example_instructions_resp.rt', example_instructions_resp.rt)
thisExp.addData('example_instructions_resp.started', example_instructions_resp.tStartRefresh)
thisExp.addData('example_instructions_resp.stopped', example_instructions_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('bankedMsg_example.started', bankedMsg_example.tStartRefresh)
thisExp.addData('bankedMsg_example.stopped', bankedMsg_example.tStopRefresh)
thisExp.addData('reminderMsg_example.started', reminderMsg_example.tStartRefresh)
thisExp.addData('reminderMsg_example.stopped', reminderMsg_example.tStopRefresh)
thisExp.addData('example_instructions_image.started', example_instructions_image.tStartRefresh)
thisExp.addData('example_instructions_image.stopped', example_instructions_image.tStopRefresh)
thisExp.addData('example_instruction_text3.started', example_instruction_text3.tStartRefresh)
thisExp.addData('example_instruction_text3.stopped', example_instruction_text3.tStopRefresh)
# the Routine "example_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "check_instructions"-------
continueRoutine = True
# update component parameters for each repeat
check_instructions_key_resp.keys = []
check_instructions_key_resp.rt = []
_check_instructions_key_resp_allKeys = []
# keep track of which components have finished
check_instructionsComponents = [check_instructions_key_resp, check_instructioins_text]
for thisComponent in check_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
check_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "check_instructions"-------
while continueRoutine:
    # get current time
    t = check_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=check_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *check_instructions_key_resp* updates
    waitOnFlip = False
    if check_instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        check_instructions_key_resp.frameNStart = frameN  # exact frame index
        check_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        check_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(check_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        check_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(check_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(check_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if check_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = check_instructions_key_resp.getKeys(keyList=['a'], waitRelease=False)
        _check_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_check_instructions_key_resp_allKeys):
            check_instructions_key_resp.keys = _check_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            check_instructions_key_resp.rt = _check_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *check_instructioins_text* updates
    if check_instructioins_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        check_instructioins_text.frameNStart = frameN  # exact frame index
        check_instructioins_text.tStart = t  # local t and not account for scr refresh
        check_instructioins_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(check_instructioins_text, 'tStartRefresh')  # time at next scr refresh
        check_instructioins_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in check_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "check_instructions"-------
for thisComponent in check_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if check_instructions_key_resp.keys in ['', [], None]:  # No response was made
    check_instructions_key_resp.keys = None
thisExp.addData('check_instructions_key_resp.keys',check_instructions_key_resp.keys)
if check_instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('check_instructions_key_resp.rt', check_instructions_key_resp.rt)
thisExp.addData('check_instructions_key_resp.started', check_instructions_key_resp.tStartRefresh)
thisExp.addData('check_instructions_key_resp.stopped', check_instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('check_instructioins_text.started', check_instructioins_text.tStartRefresh)
thisExp.addData('check_instructioins_text.stopped', check_instructioins_text.tStopRefresh)
# the Routine "check_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    balloonSize=0.08
    popped=False
    nPumps=0
    bankButton.keys = []
    bankButton.rt = []
    _bankButton_allKeys = []
    # keep track of which components have finished
    trialComponents = [balloonBody, reminderMsg, bankedMsg, bankButton]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        thisBalloonEarnings=nPumps*0.01
        balloonSize=0.1+nPumps*0.015
        
        # *balloonBody* updates
        if balloonBody.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balloonBody.frameNStart = frameN  # exact frame index
            balloonBody.tStart = t  # local t and not account for scr refresh
            balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
            balloonBody.setAutoDraw(True)
        if balloonBody.status == STARTED:  # only update if drawing
            balloonBody.setPos([0, -.5+balloonSize/2], log=False)
            balloonBody.setSize(balloonSize, log=False)
        
        # *reminderMsg* updates
        if reminderMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminderMsg.frameNStart = frameN  # exact frame index
            reminderMsg.tStart = t  # local t and not account for scr refresh
            reminderMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminderMsg, 'tStartRefresh')  # time at next scr refresh
            reminderMsg.setAutoDraw(True)
        
        # *bankedMsg* updates
        if bankedMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bankedMsg.frameNStart = frameN  # exact frame index
            bankedMsg.tStart = t  # local t and not account for scr refresh
            bankedMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bankedMsg, 'tStartRefresh')  # time at next scr refresh
            bankedMsg.setAutoDraw(True)
        if bankedMsg.status == STARTED:  # only update if drawing
            bankedMsg.setText("You have collected:\n $%.2f" %bankedEarnings, log=False)
        if event.getKeys(['space']):
          nPumps=nPumps+1
          if nPumps>maxPumps:
            popped=True
            continueRoutine=False
        
        # *bankButton* updates
        waitOnFlip = False
        if bankButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bankButton.frameNStart = frameN  # exact frame index
            bankButton.tStart = t  # local t and not account for scr refresh
            bankButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bankButton, 'tStartRefresh')  # time at next scr refresh
            bankButton.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bankButton.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bankButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bankButton.status == STARTED and not waitOnFlip:
            theseKeys = bankButton.getKeys(keyList=['return'], waitRelease=False)
            _bankButton_allKeys.extend(theseKeys)
            if len(_bankButton_allKeys):
                bankButton.keys = _bankButton_allKeys[-1].name  # just the last key pressed
                bankButton.rt = _bankButton_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #calculate cash 'earned'
    if popped:
      thisBalloonEarnings=0.0
      lastBalloonEarnings=0.0
    else:   lastBalloonEarnings=thisBalloonEarnings
    bankedEarnings = bankedEarnings+lastBalloonEarnings
    #save data
    trials.addData('nPumps', nPumps)
    trials.addData('size', balloonSize)
    trials.addData('earnings', thisBalloonEarnings)
    trials.addData('popped', popped)
    
    
    trials.addData('balloonBody.started', balloonBody.tStartRefresh)
    trials.addData('balloonBody.stopped', balloonBody.tStopRefresh)
    trials.addData('reminderMsg.started', reminderMsg.tStartRefresh)
    trials.addData('reminderMsg.stopped', reminderMsg.tStopRefresh)
    trials.addData('bankedMsg.started', bankedMsg.tStartRefresh)
    trials.addData('bankedMsg.stopped', bankedMsg.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    display_value = 0
    if popped==True:
        feedbackText="Oops! Lost that one!"
    else:
        feedbackText="You collected $%.2f." %display_value
    bang_sound.setSound('bang_22050Hz.wav', hamming=True)
    bang_sound.setVolume(1.0, log=False)
    coin_sound.setSound('coin_22050Hz_long.wav', hamming=True)
    coin_sound.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedbackComponents = [feedbackMsg, bang_sound, coin_sound]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if popped==False:
            if display_value < lastBalloonEarnings:
                display_value = 0.01 + display_value
                feedbackText="You collected $%.2f." %display_value
            else:
                coin_sound.stop()
                feedbackText="You collected $%.2f." %lastBalloonEarnings
        
        if t >= 2.5:
            continueRoutine = False
        
        # *feedbackMsg* updates
        if feedbackMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackMsg.frameNStart = frameN  # exact frame index
            feedbackMsg.tStart = t  # local t and not account for scr refresh
            feedbackMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(True)
        if feedbackMsg.status == STARTED:  # only update if drawing
            feedbackMsg.setText(feedbackText, log=False)
        # start/stop bang_sound
        if bang_sound.status == NOT_STARTED and popped==True:
            # keep track of start time/frame for later
            bang_sound.frameNStart = frameN  # exact frame index
            bang_sound.tStart = t  # local t and not account for scr refresh
            bang_sound.tStartRefresh = tThisFlipGlobal  # on global time
            bang_sound.play(when=win)  # sync with win flip
        # start/stop coin_sound
        if coin_sound.status == NOT_STARTED and popped==False:
            # keep track of start time/frame for later
            coin_sound.frameNStart = frameN  # exact frame index
            coin_sound.tStart = t  # local t and not account for scr refresh
            coin_sound.tStartRefresh = tThisFlipGlobal  # on global time
            coin_sound.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    bang_sound.stop()  # ensure sound has stopped at end of routine
    trials.addData('bang_sound.started', bang_sound.tStartRefresh)
    trials.addData('bang_sound.stopped', bang_sound.tStopRefresh)
    coin_sound.stop()  # ensure sound has stopped at end of routine
    trials.addData('coin_sound.started', coin_sound.tStartRefresh)
    trials.addData('coin_sound.stopped', coin_sound.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finalScore"-------
continueRoutine = True
# update component parameters for each repeat
finalScore_2.setText("Congratulations!\nYou have earned $%.2f.\nPlease let the experimenter know that you have finished this part." %bankedEarnings)
doneKey.keys = []
doneKey.rt = []
_doneKey_allKeys = []
# keep track of which components have finished
finalScoreComponents = [finalScore_2, doneKey]
for thisComponent in finalScoreComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalScoreClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finalScore"-------
while continueRoutine:
    # get current time
    t = finalScoreClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalScoreClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finalScore_2* updates
    if finalScore_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalScore_2.frameNStart = frameN  # exact frame index
        finalScore_2.tStart = t  # local t and not account for scr refresh
        finalScore_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalScore_2, 'tStartRefresh')  # time at next scr refresh
        finalScore_2.setAutoDraw(True)
    
    # *doneKey* updates
    waitOnFlip = False
    if doneKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        doneKey.frameNStart = frameN  # exact frame index
        doneKey.tStart = t  # local t and not account for scr refresh
        doneKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(doneKey, 'tStartRefresh')  # time at next scr refresh
        doneKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(doneKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(doneKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if doneKey.status == STARTED and not waitOnFlip:
        theseKeys = doneKey.getKeys(keyList=['a'], waitRelease=False)
        _doneKey_allKeys.extend(theseKeys)
        if len(_doneKey_allKeys):
            doneKey.keys = _doneKey_allKeys[-1].name  # just the last key pressed
            doneKey.rt = _doneKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finalScore"-------
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finalScore_2.started', finalScore_2.tStartRefresh)
thisExp.addData('finalScore_2.stopped', finalScore_2.tStopRefresh)
# check responses
if doneKey.keys in ['', [], None]:  # No response was made
    doneKey.keys = None
thisExp.addData('doneKey.keys',doneKey.keys)
if doneKey.keys != None:  # we had a response
    thisExp.addData('doneKey.rt', doneKey.rt)
thisExp.addData('doneKey.started', doneKey.tStartRefresh)
thisExp.addData('doneKey.stopped', doneKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "finalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
