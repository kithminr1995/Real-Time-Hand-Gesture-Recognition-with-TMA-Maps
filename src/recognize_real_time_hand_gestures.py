"""
The MIT License (MIT)
Copyright (c) 2020, Ashwin De Silva and Malsha Perera

Other Contributors : Asma Naim, Kithmin Wickramasinghe, Thilina
Lalitharatne, Simon Kappel

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

objective : Execute real-time hand gesture recognition using TMA maps of
multi-channel sEMG signals. Currently, this version of the code supports
only MyoArm Band (Thalamic Labs, Canada)

The code is based on the following paper :
[1] A. D. Silva, M. V. Perera, K. Wickramasinghe, A. M. Naim,
    T. Dulantha Lalitharatne and S. L. Kappel, "Real-Time Hand Gesture
    Recognition Using Temporal Muscle Activation Maps of Multi-Channel
    Semg Signals," ICASSP 2020 - 2020 IEEE International Conference
    on Acoustics, Speech and Signal Processing (ICASSP), Barcelona,
    Spain, 2020, pp. 1299-1303.
"""

from tma.models.real_time_prediction import *

model_path = 'models/subject_1001_Ashwin/model/cnn_model.h5'
myo.init('path/to/myo/sdk')  # enter the path of the sdk/myo.famework/myo
hub = myo.Hub()
el = EmgLearn(fs=200,
              no_channels=8,
              obs_dur=0.400)
listener = EmgCollector(n=512)

gesture_dict = {
        0 : 'Middle_Flexion',
        1 :'Ring_Flexion',
        2 : 'Hand_Closure',
        3 : 'V_Flexion',
        4 : 'Pointer',
        5 : 'Neutral',
        6 : 'No_Gesture'
    }

live = Predict(listener=listener,
               emgLearn=el,
               gesture_dict=gesture_dict,
               cnn_model_path=model_path)

with hub.run_in_background(listener.on_event):
    live.main()

print("Closing...")
