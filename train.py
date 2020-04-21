from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
import Leap, sys, thread, time
import numpy as np
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import math

class GenerateTrainingSet(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    words_to_define = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    NUM_TRAINING_EXAMPLES = 10
    NUM_FRAME_GRABS = 10
    

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def doTheThing(self, controller):
        word=raw_input("enter sign name you want to record")
        
        writeFile = open("trainingSet.csv", "a")
        for i in xrange(0, self.NUM_TRAINING_EXAMPLES):
            print("Make gesture now for %s" % word)
            time.sleep(1)
            result = self.captureGesture(controller)
            writeFile.write(result +word+ '\n')
            print("Gesture successfully recorded. That was time #%d Next one starts on enter..." % (i+1))
            
            raw_input("Press Enter to continue...")

    def captureGesture(self, controller):
        frames = []
        trainingSet=[]
        finalAns=""
        ans = ""
        for i in range(0, self.NUM_FRAME_GRABS):
            frameGrab = controller.frame()
            frames.append(frameGrab);
            print frameGrab
            time.sleep(0.1)
        sumHands = 0
        sumFingers = 0
        sumTranlsationX = 0
        sumTranslationY = 0
        sumTranslationZ = 0
        rotationAxisX = 0
        rotationAxisY = 0
        rotationAxisZ = 0
        rotationAngle = 0

        hand1Type = 0
        hand1DirectionX = 0
        hand1DirectionY = 0
        hand1DirectionZ = 0
        hand1PalmPositionX = 0
        hand1PalmPositionY = 0
        hand1PalmPositionZ = 0
        hand1GrabStrength = 0
        hand1PinchStrength = 0
        hand1Confidence = 0
        yaw1=0


        hand2Type = 0
        hand2DirectionX = 0
        hand2DirectionY = 0
        hand2DirectionZ = 0
        hand2PalmPositionX = 0
        hand2PalmPositionY = 0
        hand2PalmPositionZ = 0
        hand2GrabStrength = 0
        hand2PinchStrength = 0
        hand2Confidence = 0
        hand2ArmDirectionX = 0
        hand2ArmDirectionY = 0
        hand2ArmDirectionZ = 0
        hand2ArmCenterX = 0
        hand2ArmCenterY = 0
        hand2ArmCenterZ = 0
        hand2ArmUpVectorX = 0
        hand2ArmUpVectorY = 0
        hand2ArmUpVectorZ = 0
        hand2TranslationX = 0
        hand2TranslationY = 0
        hand2TranslationZ = 0
        hand2RotationAxisX = 0
        hand2RotationAxisY = 0
        hand2RotationAxisZ = 0
        hand2RotationAngle = 0

        ## Hand 1 Finger 1 begins here ##
        hand1Finger1DirectionX = 0
        hand1Finger1DirectionY = 0
        hand1Finger1DirectionZ = 0
        hand1Finger1Extended = 0
        # attributes of finger 1 metacarpals
        hand1Finger1MetacarpalCenterX = 0
        hand1Finger1MetacarpalCenterY = 0
        hand1Finger1MetacarpalCenterZ = 0
        

        # attributes of finger 1 proximal phalanx bone
        hand1Finger1ProximalPhalanxBoneCenterX = 0
        hand1Finger1ProximalPhalanxBoneCenterY = 0
        hand1Finger1ProximalPhalanxBoneCenterZ = 0
        

        # attributes of finger 1 intermediate phalanx bone
        hand1Finger1IntermediatePhalanxBoneCenterX = 0
        hand1Finger1IntermediatePhalanxBoneCenterY = 0
        hand1Finger1IntermediatePhalanxBoneCenterZ = 0
        
        # attributes of finger 1 distal phalanx bone
        hand1Finger1DistalPhalanxBoneCenterX = 0
        hand1Finger1DistalPhalanxBoneCenterY = 0
        hand1Finger1DistalPhalanxBoneCenterZ = 0
       
        hand1Finger1TipPositionX = 0
        hand1Finger1TipPositionY = 0
        hand1Finger1TipPositionZ = 0

        ## Hand 1 Finger 2 Begins Here ##

        hand1Finger2DirectionX = 0
        hand1Finger2DirectionY = 0
        hand1Finger2DirectionZ = 0
        hand1Finger2Extended = 0
        # attributes of finger 2 metacarpals
        hand1Finger2MetacarpalCenterX = 0
        hand1Finger2MetacarpalCenterY = 0
        hand1Finger2MetacarpalCenterZ = 0
        
        # attributes of finger 2 proximal phalanx bone
        hand1Finger2ProximalPhalanxBoneCenterX = 0
        hand1Finger2ProximalPhalanxBoneCenterY = 0
        hand1Finger2ProximalPhalanxBoneCenterZ = 0
       
        # attributes of finger 2 intermediate phalanx bone
        hand1Finger2IntermediatePhalanxBoneCenterX = 0
        hand1Finger2IntermediatePhalanxBoneCenterY = 0
        hand1Finger2IntermediatePhalanxBoneCenterZ = 0
       

        # attributes of finger 2 distal phalanx bone
        hand1Finger2DistalPhalanxBoneCenterX = 0
        hand1Finger2DistalPhalanxBoneCenterY = 0
        hand1Finger2DistalPhalanxBoneCenterZ = 0
       

        hand1Finger2TipPositionX = 0
        hand1Finger2TipPositionY = 0
        hand1Finger2TipPositionZ = 0

        ## Hand 1 Finger 3 Begins Here ##

        hand1Finger3DirectionX = 0
        hand1Finger3DirectionY = 0
        hand1Finger3DirectionZ = 0
        hand1Finger3Extended = 0
        # attributes of Finger 3 metacarpals
        hand1Finger3MetacarpalCenterX = 0
        hand1Finger3MetacarpalCenterY = 0
        hand1Finger3MetacarpalCenterZ = 0
        hand1Finger3MetacarpalDirectionX = 0
        hand1Finger3MetacarpalDirectionY = 0
        hand1Finger3MetacarpalDirectionZ = 0
        hand1Finger3MetacarpalUpVectorX = 0
        hand1Finger3MetacarpalUpVectorY = 0
        hand1Finger3MetacarpalUpVectorZ = 0
        # attributes of Finger 3 proximal phalanx bone
        hand1Finger3ProximalPhalanxBoneCenterX = 0
        hand1Finger3ProximalPhalanxBoneCenterY = 0
        hand1Finger3ProximalPhalanxBoneCenterZ = 0
        hand1Finger3ProximalPhalanxBoneDirectionX = 0
        hand1Finger3ProximalPhalanxBoneDirectionY = 0
        hand1Finger3ProximalPhalanxBoneDirectionZ = 0
        hand1Finger3ProximalPhalanxBoneUpVectorX = 0
        hand1Finger3ProximalPhalanxBoneUpVectorY = 0
        hand1Finger3ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 3 intermediate phalanx bone
        hand1Finger3IntermediatePhalanxBoneCenterX = 0
        hand1Finger3IntermediatePhalanxBoneCenterY = 0
        hand1Finger3IntermediatePhalanxBoneCenterZ = 0
        hand1Finger3IntermediatePhalanxBoneDirectionX = 0
        hand1Finger3IntermediatePhalanxBoneDirectionY = 0
        hand1Finger3IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger3IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger3IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger3IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 3 distal phalanx bone
        hand1Finger3DistalPhalanxBoneCenterX = 0
        hand1Finger3DistalPhalanxBoneCenterY = 0
        hand1Finger3DistalPhalanxBoneCenterZ = 0
        hand1Finger3DistalPhalanxBoneDirectionX = 0
        hand1Finger3DistalPhalanxBoneDirectionY = 0
        hand1Finger3DistalPhalanxBoneDirectionZ = 0
        hand1Finger3DistalPhalanxBoneUpVectorX = 0
        hand1Finger3DistalPhalanxBoneUpVectorY = 0
        hand1Finger3DistalPhalanxBoneUpVectorZ = 0
        hand1Finger3TipPositionX = 0
        hand1Finger3TipPositionY = 0
        hand1Finger3TipPositionZ = 0

        ## Hand 1 Finger 4 Begins Here ##

        hand1Finger4DirectionX = 0
        hand1Finger4DirectionY = 0
        hand1Finger4DirectionZ = 0
        hand1Finger4Extended = 0
        # attributes of Finger 4 metacarpals
        hand1Finger4MetacarpalCenterX = 0
        hand1Finger4MetacarpalCenterY = 0
        hand1Finger4MetacarpalCenterZ = 0
        hand1Finger4MetacarpalDirectionX = 0
        hand1Finger4MetacarpalDirectionY = 0
        hand1Finger4MetacarpalDirectionZ = 0
        hand1Finger4MetacarpalUpVectorX = 0
        hand1Finger4MetacarpalUpVectorY = 0
        hand1Finger4MetacarpalUpVectorZ = 0
        # attributes of Finger 4 proximal phalanx bone
        hand1Finger4ProximalPhalanxBoneCenterX = 0
        hand1Finger4ProximalPhalanxBoneCenterY = 0
        hand1Finger4ProximalPhalanxBoneCenterZ = 0
        hand1Finger4ProximalPhalanxBoneDirectionX = 0
        hand1Finger4ProximalPhalanxBoneDirectionY = 0
        hand1Finger4ProximalPhalanxBoneDirectionZ = 0
        hand1Finger4ProximalPhalanxBoneUpVectorX = 0
        hand1Finger4ProximalPhalanxBoneUpVectorY = 0
        hand1Finger4ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 4 intermediate phalanx bone
        hand1Finger4IntermediatePhalanxBoneCenterX = 0
        hand1Finger4IntermediatePhalanxBoneCenterY = 0
        hand1Finger4IntermediatePhalanxBoneCenterZ = 0
        hand1Finger4IntermediatePhalanxBoneDirectionX = 0
        hand1Finger4IntermediatePhalanxBoneDirectionY = 0
        hand1Finger4IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger4IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger4IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger4IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 4 distal phalanx bone
        hand1Finger4DistalPhalanxBoneCenterX = 0
        hand1Finger4DistalPhalanxBoneCenterY = 0
        hand1Finger4DistalPhalanxBoneCenterZ = 0
        hand1Finger4DistalPhalanxBoneDirectionX = 0
        hand1Finger4DistalPhalanxBoneDirectionY = 0
        hand1Finger4DistalPhalanxBoneDirectionZ = 0
        hand1Finger4DistalPhalanxBoneUpVectorX = 0
        hand1Finger4DistalPhalanxBoneUpVectorY = 0
        hand1Finger4DistalPhalanxBoneUpVectorZ = 0
        hand1Finger4TipPositionX = 0
        hand1Finger4TipPositionY = 0
        hand1Finger4TipPositionZ = 0

        ## Hand 1 Finger 5 Begins Here ##

        hand1Finger5DirectionX = 0
        hand1Finger5DirectionY = 0
        hand1Finger5DirectionZ = 0
        hand1Finger5Extended = 0
        # attributes of Finger 5 metacarpals
        hand1Finger5MetacarpalCenterX = 0
        hand1Finger5MetacarpalCenterY = 0
        hand1Finger5MetacarpalCenterZ = 0
        
        # attributes of Finger 5 proximal phalanx bone
        hand1Finger5ProximalPhalanxBoneCenterX = 0
        hand1Finger5ProximalPhalanxBoneCenterY = 0
        hand1Finger5ProximalPhalanxBoneCenterZ = 0
        
        # attributes of Finger 5 intermediate phalanx bone
        hand1Finger5IntermediatePhalanxBoneCenterX = 0
        hand1Finger5IntermediatePhalanxBoneCenterY = 0
        hand1Finger5IntermediatePhalanxBoneCenterZ = 0
        
        # attributes of Finger 5 distal phalanx bone
        hand1Finger5DistalPhalanxBoneCenterX = 0
        hand1Finger5DistalPhalanxBoneCenterY = 0
        hand1Finger5DistalPhalanxBoneCenterZ = 0
        
        hand1Finger5TipPositionX = 0
        hand1Finger5TipPositionY = 0
        hand1Finger5TipPositionZ = 0

        pitch1=0
        roll1=0

        hand1ProximalFinger1Finger2=0
        hand1ProximalFinger2Finger3=0
        hand1ProximalFinger3Finger4=0
        hand1ProximalFinger4Finger5=0

        hand1IntermediateFinger1Finger2=0
        hand1IntermediateFinger2Finger3=0
        hand1IntermediateFinger3Finger4=0
        hand1IntermediateFinger4Finger5=0

        hand1DistalFinger1Finger2=0
        hand1DistalFinger2Finger3=0
        hand1DistalFinger3Finger4=0
        hand1DistalFinger4Finger5=0

        hand1TipFinger1Finger2=0
        hand1TipFinger2Finger3=0
        hand1TipFinger3Finger4=0
        hand1TipFinger4Finger5=0

        hand1finger1CentreTip=0
        hand1finger2CentreTip=0
        hand1finger3CentreTip=0
        hand1finger4CentreTip=0
        hand1finger5CentreTip=0
        
        


        for frame in frames:
            sumHands += len(frame.hands)
            sumFingers += len(frame.fingers)
            if ( frame.hands[0] is not None):
                hand1 = frame.hands[0]
                hand1GrabStrength += hand1.grab_strength
                hand1PinchStrength += hand1.pinch_strength
                hand1Confidence += hand1.confidence
                pitch1 = hand1.direction.pitch
                yaw1 = hand1.direction.yaw
                roll1 = hand1.palm_normal.roll
                hand1PalmPositionVector = hand1.palm_position
                hand1PalmPositionX += hand1PalmPositionVector[0]
                hand1PalmPositionY += hand1PalmPositionVector[1]
                hand1PalmPositionZ += hand1PalmPositionVector[2]
                #thumb
                if(frame.hands[0].fingers[0] is not None):
                    hand1Finger1 = frame.hands[0].fingers[0]
                    #metacarphal
                    hand1Finger1MetacarpalCenter = hand1Finger1.bone(0).center
                    hand1Finger1MetacarpalCenterX += hand1Finger1MetacarpalCenter[0]
                    hand1Finger1MetacarpalCenterY += hand1Finger1MetacarpalCenter[1]
                    hand1Finger1MetacarpalCenterZ += hand1Finger1MetacarpalCenter[2]
                    #proximal
                    hand1Finger1ProximalPhalanxBoneCenter = hand1Finger1.bone(1).center
                    hand1Finger1ProximalPhalanxBoneCenterX += hand1Finger1ProximalPhalanxBoneCenter[0]
                    hand1Finger1ProximalPhalanxBoneCenterY += hand1Finger1ProximalPhalanxBoneCenter[1]
                    hand1Finger1ProximalPhalanxBoneCenterZ += hand1Finger1ProximalPhalanxBoneCenter[2]
                    #intermediate
                    hand1Finger1IntermediatePhalanxBoneCenter = hand1Finger1.bone(2).center
                    hand1Finger1IntermediatePhalanxBoneCenterX += hand1Finger1IntermediatePhalanxBoneCenter[0]
                    hand1Finger1IntermediatePhalanxBoneCenterY += hand1Finger1IntermediatePhalanxBoneCenter[1]
                    hand1Finger1IntermediatePhalanxBoneCenterZ += hand1Finger1IntermediatePhalanxBoneCenter[2]
                    #distal
                    hand1Finger1DistalPhalanxBoneCenter = hand1Finger1.bone(3).center
                    hand1Finger1DistalPhalanxBoneCenterX += hand1Finger1DistalPhalanxBoneCenter[0]
                    hand1Finger1DistalPhalanxBoneCenterY += hand1Finger1DistalPhalanxBoneCenter[1]
                    hand1Finger1DistalPhalanxBoneCenterZ += hand1Finger1DistalPhalanxBoneCenter[2]
                    #tip
                    hand1Finger1TipPositionX += hand1Finger1.joint_position(3)[0]
                    hand1Finger1TipPositionY += hand1Finger1.joint_position(3)[1]
                    hand1Finger1TipPositionZ += hand1Finger1.joint_position(3)[2]
                
                #index
                if(frame.hands[0].fingers[1] is not None):
                    hand1Finger2 = frame.hands[0].fingers[1]
                   
                    # attributes of finger 2 metacarpals
                    hand1Finger2MetacarpalCenter = hand1Finger2.bone(0).center
                    hand1Finger2MetacarpalCenterX += hand1Finger2MetacarpalCenter[0]
                    hand1Finger2MetacarpalCenterY += hand1Finger2MetacarpalCenter[1]
                    hand1Finger2MetacarpalCenterZ += hand1Finger2MetacarpalCenter[2]
                    
                    # attributes of finger 2 proximal phalanx bone
                    hand1Finger2ProximalPhalanxBoneCenter = hand1Finger2.bone(1).center
                    hand1Finger2ProximalPhalanxBoneCenterX += hand1Finger2ProximalPhalanxBoneCenter[0]
                    hand1Finger2ProximalPhalanxBoneCenterY += hand1Finger2ProximalPhalanxBoneCenter[1]
                    hand1Finger2ProximalPhalanxBoneCenterZ += hand1Finger2ProximalPhalanxBoneCenter[2]
                    
                    # attributes of finger 2 intermediate phalanx bone
                    hand1Finger2IntermediatePhalanxBoneCenter = hand1Finger2.bone(2).center
                    hand1Finger2IntermediatePhalanxBoneCenterX += hand1Finger2IntermediatePhalanxBoneCenter[0]
                    hand1Finger2IntermediatePhalanxBoneCenterY += hand1Finger2IntermediatePhalanxBoneCenter[1]
                    hand1Finger2IntermediatePhalanxBoneCenterZ += hand1Finger2IntermediatePhalanxBoneCenter[2]
                    
                    # attributes of finger 2 distal phalanx bone
                    hand1Finger2DistalPhalanxBoneCenter = hand1Finger2.bone(3).center
                    hand1Finger2DistalPhalanxBoneCenterX += hand1Finger2DistalPhalanxBoneCenter[0]
                    hand1Finger2DistalPhalanxBoneCenterY += hand1Finger2DistalPhalanxBoneCenter[1]
                    hand1Finger2DistalPhalanxBoneCenterZ += hand1Finger2DistalPhalanxBoneCenter[2]
                    
                    #tip
                    hand1Finger2TipPositionX += hand1Finger2.joint_position(3)[0]
                    hand1Finger2TipPositionY += hand1Finger2.joint_position(3)[1]
                    hand1Finger2TipPositionZ += hand1Finger2.joint_position(3)[2]

                # it is for middle finger
                if(frame.hands[0].fingers[2] is not None):
                    ## Set Hand 1 Finger 3 ##
                    hand1Finger3 = frame.hands[0].fingers[2]
                    
                    # attributes of finger 3 metacarpals
                    hand1Finger3MetacarpalCenter = hand1Finger3.bone(0).center
                    hand1Finger3MetacarpalCenterX += hand1Finger3MetacarpalCenter[0]
                    hand1Finger3MetacarpalCenterY += hand1Finger3MetacarpalCenter[1]
                    hand1Finger3MetacarpalCenterZ += hand1Finger3MetacarpalCenter[2]
                    
                    # attributes of finger 3 proximal phalanx bone
                    hand1Finger3ProximalPhalanxBoneCenter = hand1Finger3.bone(1).center
                    hand1Finger3ProximalPhalanxBoneCenterX += hand1Finger3ProximalPhalanxBoneCenter[0]
                    hand1Finger3ProximalPhalanxBoneCenterY += hand1Finger3ProximalPhalanxBoneCenter[1]
                    hand1Finger3ProximalPhalanxBoneCenterZ += hand1Finger3ProximalPhalanxBoneCenter[2]
                    
                    # attributes of finger 3 intermediate phalanx bone
                    hand1Finger3IntermediatePhalanxBoneCenter = hand1Finger3.bone(2).center
                    hand1Finger3IntermediatePhalanxBoneCenterX += hand1Finger3IntermediatePhalanxBoneCenter[0]
                    hand1Finger3IntermediatePhalanxBoneCenterY += hand1Finger3IntermediatePhalanxBoneCenter[1]
                    hand1Finger3IntermediatePhalanxBoneCenterZ += hand1Finger3IntermediatePhalanxBoneCenter[2]
                    
                    # attributes of finger 3 distal phalanx bone
                    hand1Finger3DistalPhalanxBoneCenter = hand1Finger3.bone(3).center
                    hand1Finger3DistalPhalanxBoneCenterX += hand1Finger3DistalPhalanxBoneCenter[0]
                    hand1Finger3DistalPhalanxBoneCenterY += hand1Finger3DistalPhalanxBoneCenter[1]
                    hand1Finger3DistalPhalanxBoneCenterZ += hand1Finger3DistalPhalanxBoneCenter[2]
                    
                    #tip
                    hand1Finger3TipPositionX += hand1Finger3.joint_position(3)[0]
                    hand1Finger3TipPositionY += hand1Finger3.joint_position(3)[1]
                    hand1Finger3TipPositionZ += hand1Finger3.joint_position(3)[2]
                #it is for ring finger
                if(frame.hands[0].fingers[3] is not None):
                    ## Set Hand 1 Finger 4 ##
                    hand1Finger4 = frame.hands[0].fingers[3]
                    
                    # attributes of finger 4 metacarpals
                    hand1Finger4MetacarpalCenter = hand1Finger4.bone(0).center
                    hand1Finger4MetacarpalCenterX += hand1Finger4MetacarpalCenter[0]
                    hand1Finger4MetacarpalCenterY += hand1Finger4MetacarpalCenter[1]
                    hand1Finger4MetacarpalCenterZ += hand1Finger4MetacarpalCenter[2]
                   
                    # attributes of finger 4 proximal phalanx bone
                    hand1Finger4ProximalPhalanxBoneCenter = hand1Finger4.bone(1).center
                    hand1Finger4ProximalPhalanxBoneCenterX += hand1Finger4ProximalPhalanxBoneCenter[0]
                    hand1Finger4ProximalPhalanxBoneCenterY += hand1Finger4ProximalPhalanxBoneCenter[1]
                    hand1Finger4ProximalPhalanxBoneCenterZ += hand1Finger4ProximalPhalanxBoneCenter[2]
                    
                    # attributes of finger 4 intermediate phalanx bone
                    hand1Finger4IntermediatePhalanxBoneCenter = hand1Finger4.bone(2).center
                    hand1Finger4IntermediatePhalanxBoneCenterX += hand1Finger4IntermediatePhalanxBoneCenter[0]
                    hand1Finger4IntermediatePhalanxBoneCenterY += hand1Finger4IntermediatePhalanxBoneCenter[1]
                    hand1Finger4IntermediatePhalanxBoneCenterZ += hand1Finger4IntermediatePhalanxBoneCenter[2]
                    
                    # attributes of finger 4 distal phalanx bone
                    hand1Finger4DistalPhalanxBoneCenter = hand1Finger4.bone(3).center
                    hand1Finger4DistalPhalanxBoneCenterX += hand1Finger4DistalPhalanxBoneCenter[0]
                    hand1Finger4DistalPhalanxBoneCenterY += hand1Finger4DistalPhalanxBoneCenter[1]
                    hand1Finger4DistalPhalanxBoneCenterZ += hand1Finger4DistalPhalanxBoneCenter[2]
                   
                    #tip
                    hand1Finger4TipPositionX += hand1Finger4.joint_position(3)[0]
                    hand1Finger4TipPositionY += hand1Finger4.joint_position(3)[1]
                    hand1Finger4TipPositionZ += hand1Finger4.joint_position(3)[2]
                #it is for pinky finger
                if(frame.hands[0].fingers[4] is not None):
                    ## Set Hand 1 Finger 5 ##
                    hand1Finger5 = frame.hands[0].fingers[4]
                    
                    # attributes of finger 5 metacarpals
                    hand1Finger5MetacarpalCenter = hand1Finger5.bone(0).center
                    hand1Finger5MetacarpalCenterX += hand1Finger5MetacarpalCenter[0]
                    hand1Finger5MetacarpalCenterY += hand1Finger5MetacarpalCenter[1]
                    hand1Finger5MetacarpalCenterZ += hand1Finger5MetacarpalCenter[2]
                    
                    # attributes of finger 5 proximal phalanx bone
                    hand1Finger5ProximalPhalanxBoneCenter = hand1Finger5.bone(1).center
                    hand1Finger5ProximalPhalanxBoneCenterX += hand1Finger5ProximalPhalanxBoneCenter[0]
                    hand1Finger5ProximalPhalanxBoneCenterY += hand1Finger5ProximalPhalanxBoneCenter[1]
                    hand1Finger5ProximalPhalanxBoneCenterZ += hand1Finger5ProximalPhalanxBoneCenter[2]
                    
                    # attributes of finger 5 intermediate phalanx bone
                    hand1Finger5IntermediatePhalanxBoneCenter = hand1Finger5.bone(2).center
                    hand1Finger5IntermediatePhalanxBoneCenterX += hand1Finger5IntermediatePhalanxBoneCenter[0]
                    hand1Finger5IntermediatePhalanxBoneCenterY += hand1Finger5IntermediatePhalanxBoneCenter[1]
                    hand1Finger5IntermediatePhalanxBoneCenterZ += hand1Finger5IntermediatePhalanxBoneCenter[2]
                    
                    # attributes of finger 5 distal phalanx bone
                    hand1Finger5DistalPhalanxBoneCenter = hand1Finger5.bone(3).center
                    hand1Finger5DistalPhalanxBoneCenterX += hand1Finger5DistalPhalanxBoneCenter[0]
                    hand1Finger5DistalPhalanxBoneCenterY += hand1Finger5DistalPhalanxBoneCenter[1]
                    hand1Finger5DistalPhalanxBoneCenterZ += hand1Finger5DistalPhalanxBoneCenter[2]
                    
                    #tip
                    hand1Finger5TipPositionX += hand1Finger5.joint_position(3)[0]
                    hand1Finger5TipPositionY += hand1Finger5.joint_position(3)[1]
                    hand1Finger5TipPositionZ += hand1Finger5.joint_position(3)[2]

                hand1finger1CentreTip+=math.sqrt(((hand1Finger1TipPositionX-hand1PalmPositionX)*(hand1Finger1TipPositionX-hand1PalmPositionX))+((hand1Finger1TipPositionY-hand1PalmPositionY)*(hand1Finger1TipPositionY-hand1PalmPositionY))+((hand1Finger1TipPositionZ-hand1PalmPositionZ)*(hand1Finger1TipPositionZ-hand1PalmPositionZ)))
                hand1finger2CentreTip+=math.sqrt(((hand1Finger2TipPositionX-hand1PalmPositionX)*(hand1Finger2TipPositionX-hand1PalmPositionX))+((hand1Finger2TipPositionY-hand1PalmPositionY)*(hand1Finger2TipPositionY-hand1PalmPositionY))+((hand1Finger2TipPositionZ-hand1PalmPositionZ)*(hand1Finger2TipPositionZ-hand1PalmPositionZ)))
                hand1finger3CentreTip+=math.sqrt(((hand1Finger3TipPositionX-hand1PalmPositionX)*(hand1Finger3TipPositionX-hand1PalmPositionX))+((hand1Finger3TipPositionY-hand1PalmPositionY)*(hand1Finger3TipPositionY-hand1PalmPositionY))+((hand1Finger3TipPositionZ-hand1PalmPositionZ)*(hand1Finger3TipPositionZ-hand1PalmPositionZ)))
                hand1finger4CentreTip+=math.sqrt(((hand1Finger4TipPositionX-hand1PalmPositionX)*(hand1Finger4TipPositionX-hand1PalmPositionX))+((hand1Finger4TipPositionY-hand1PalmPositionY)*(hand1Finger4TipPositionY-hand1PalmPositionY))+((hand1Finger4TipPositionZ-hand1PalmPositionZ)*(hand1Finger4TipPositionZ-hand1PalmPositionZ)))
                hand1finger5CentreTip+=math.sqrt(((hand1Finger5TipPositionX-hand1PalmPositionX)*(hand1Finger5TipPositionX-hand1PalmPositionX))+((hand1Finger5TipPositionY-hand1PalmPositionY)*(hand1Finger5TipPositionY-hand1PalmPositionY))+((hand1Finger5TipPositionZ-hand1PalmPositionZ)*(hand1Finger5TipPositionZ-hand1PalmPositionZ)))
            
                hand1ProximalFinger1Finger2+=math.sqrt(((hand1Finger1ProximalPhalanxBoneCenterX- hand1Finger2ProximalPhalanxBoneCenterX)*(hand1Finger1ProximalPhalanxBoneCenterX- hand1Finger2ProximalPhalanxBoneCenterX))
                                                        +((hand1Finger1ProximalPhalanxBoneCenterY- hand1Finger2ProximalPhalanxBoneCenterY)*(hand1Finger1ProximalPhalanxBoneCenterY- hand1Finger2ProximalPhalanxBoneCenterY))
                                                        +((hand1Finger1ProximalPhalanxBoneCenterZ- hand1Finger2ProximalPhalanxBoneCenterZ)*(hand1Finger1ProximalPhalanxBoneCenterZ- hand1Finger2ProximalPhalanxBoneCenterZ)))
                
                hand1ProximalFinger2Finger3+=math.sqrt(((hand1Finger2ProximalPhalanxBoneCenterX- hand1Finger3ProximalPhalanxBoneCenterX)*(hand1Finger2ProximalPhalanxBoneCenterX- hand1Finger3ProximalPhalanxBoneCenterX))
                                                        +((hand1Finger2ProximalPhalanxBoneCenterY- hand1Finger3ProximalPhalanxBoneCenterY)*(hand1Finger2ProximalPhalanxBoneCenterY- hand1Finger3ProximalPhalanxBoneCenterY))
                                                        +((hand1Finger2ProximalPhalanxBoneCenterZ- hand1Finger3ProximalPhalanxBoneCenterZ)*(hand1Finger2ProximalPhalanxBoneCenterZ- hand1Finger3ProximalPhalanxBoneCenterZ)))
                
                hand1ProximalFinger3Finger4+=math.sqrt(((hand1Finger3ProximalPhalanxBoneCenterX- hand1Finger4ProximalPhalanxBoneCenterX)*(hand1Finger3ProximalPhalanxBoneCenterX- hand1Finger4ProximalPhalanxBoneCenterX))
                                                        +((hand1Finger3ProximalPhalanxBoneCenterY- hand1Finger4ProximalPhalanxBoneCenterY)*(hand1Finger3ProximalPhalanxBoneCenterY- hand1Finger4ProximalPhalanxBoneCenterY))
                                                        +((hand1Finger3ProximalPhalanxBoneCenterZ- hand1Finger4ProximalPhalanxBoneCenterZ)*(hand1Finger3ProximalPhalanxBoneCenterZ- hand1Finger4ProximalPhalanxBoneCenterZ)))

                hand1ProximalFinger4Finger5+=math.sqrt(((hand1Finger4ProximalPhalanxBoneCenterX- hand1Finger5ProximalPhalanxBoneCenterX)*(hand1Finger4ProximalPhalanxBoneCenterX- hand1Finger5ProximalPhalanxBoneCenterX))
                                                        +((hand1Finger4ProximalPhalanxBoneCenterY- hand1Finger5ProximalPhalanxBoneCenterY)*(hand1Finger4ProximalPhalanxBoneCenterY- hand1Finger5ProximalPhalanxBoneCenterY))
                                                        +((hand1Finger4ProximalPhalanxBoneCenterZ- hand1Finger5ProximalPhalanxBoneCenterZ)*(hand1Finger4ProximalPhalanxBoneCenterZ- hand1Finger5ProximalPhalanxBoneCenterZ)))


                #next
                hand1IntermediateFinger1Finger2 +=math.sqrt(((hand1Finger1IntermediatePhalanxBoneCenterX- hand1Finger2IntermediatePhalanxBoneCenterX)*(hand1Finger1IntermediatePhalanxBoneCenterX- hand1Finger2IntermediatePhalanxBoneCenterX))
                                                        +((hand1Finger1IntermediatePhalanxBoneCenterY- hand1Finger2IntermediatePhalanxBoneCenterY)*(hand1Finger1IntermediatePhalanxBoneCenterY- hand1Finger2IntermediatePhalanxBoneCenterY))
                                                        +((hand1Finger1IntermediatePhalanxBoneCenterZ- hand1Finger2IntermediatePhalanxBoneCenterZ)*(hand1Finger1IntermediatePhalanxBoneCenterZ- hand1Finger2IntermediatePhalanxBoneCenterZ)))
                
                hand1IntermediateFinger2Finger3+=math.sqrt(((hand1Finger2IntermediatePhalanxBoneCenterX- hand1Finger3IntermediatePhalanxBoneCenterX)*(hand1Finger2IntermediatePhalanxBoneCenterX- hand1Finger3IntermediatePhalanxBoneCenterX))
                                                        +((hand1Finger2IntermediatePhalanxBoneCenterY- hand1Finger3IntermediatePhalanxBoneCenterY)*(hand1Finger2IntermediatePhalanxBoneCenterY- hand1Finger3IntermediatePhalanxBoneCenterY))
                                                        +((hand1Finger2IntermediatePhalanxBoneCenterZ- hand1Finger3IntermediatePhalanxBoneCenterZ)*(hand1Finger2IntermediatePhalanxBoneCenterZ- hand1Finger3IntermediatePhalanxBoneCenterZ)))
                
                hand1IntermediateFinger3Finger4+=math.sqrt(((hand1Finger3IntermediatePhalanxBoneCenterX- hand1Finger4IntermediatePhalanxBoneCenterX)*(hand1Finger3IntermediatePhalanxBoneCenterX- hand1Finger4IntermediatePhalanxBoneCenterX))
                                                        +((hand1Finger3IntermediatePhalanxBoneCenterY- hand1Finger4IntermediatePhalanxBoneCenterY)*(hand1Finger3IntermediatePhalanxBoneCenterY- hand1Finger4IntermediatePhalanxBoneCenterY))
                                                        +((hand1Finger3IntermediatePhalanxBoneCenterZ- hand1Finger4IntermediatePhalanxBoneCenterZ)*(hand1Finger3IntermediatePhalanxBoneCenterZ- hand1Finger4IntermediatePhalanxBoneCenterZ)))

                hand1IntermediateFinger4Finger5+=math.sqrt(((hand1Finger4IntermediatePhalanxBoneCenterX- hand1Finger5IntermediatePhalanxBoneCenterX)*(hand1Finger4IntermediatePhalanxBoneCenterX- hand1Finger5IntermediatePhalanxBoneCenterX))
                                                        +((hand1Finger4IntermediatePhalanxBoneCenterY- hand1Finger5IntermediatePhalanxBoneCenterY)*(hand1Finger4IntermediatePhalanxBoneCenterY- hand1Finger5IntermediatePhalanxBoneCenterY))
                                                        +((hand1Finger4IntermediatePhalanxBoneCenterZ- hand1Finger5IntermediatePhalanxBoneCenterZ)*(hand1Finger4IntermediatePhalanxBoneCenterZ- hand1Finger5IntermediatePhalanxBoneCenterZ)))

                #next
                hand1DistalFinger1Finger2 +=math.sqrt(((hand1Finger1DistalPhalanxBoneCenterX- hand1Finger2DistalPhalanxBoneCenterX)*(hand1Finger1DistalPhalanxBoneCenterX- hand1Finger2DistalPhalanxBoneCenterX))
                                                        +((hand1Finger1DistalPhalanxBoneCenterY- hand1Finger2DistalPhalanxBoneCenterY)*(hand1Finger1DistalPhalanxBoneCenterY- hand1Finger2DistalPhalanxBoneCenterY))
                                                        +((hand1Finger1DistalPhalanxBoneCenterZ- hand1Finger2DistalPhalanxBoneCenterZ)*(hand1Finger1DistalPhalanxBoneCenterZ- hand1Finger2DistalPhalanxBoneCenterZ)))
                
                hand1DistalFinger2Finger3+=math.sqrt(((hand1Finger2DistalPhalanxBoneCenterX- hand1Finger3DistalPhalanxBoneCenterX)*(hand1Finger2DistalPhalanxBoneCenterX- hand1Finger3DistalPhalanxBoneCenterX))
                                                        +((hand1Finger2DistalPhalanxBoneCenterY- hand1Finger3DistalPhalanxBoneCenterY)*(hand1Finger2DistalPhalanxBoneCenterY- hand1Finger3DistalPhalanxBoneCenterY))
                                                        +((hand1Finger2DistalPhalanxBoneCenterZ- hand1Finger3DistalPhalanxBoneCenterZ)*(hand1Finger2DistalPhalanxBoneCenterZ- hand1Finger3DistalPhalanxBoneCenterZ)))
                
                hand1DistalFinger3Finger4+=math.sqrt(((hand1Finger3DistalPhalanxBoneCenterX- hand1Finger4DistalPhalanxBoneCenterX)*(hand1Finger3DistalPhalanxBoneCenterX- hand1Finger4DistalPhalanxBoneCenterX))
                                                        +((hand1Finger3DistalPhalanxBoneCenterY- hand1Finger4DistalPhalanxBoneCenterY)*(hand1Finger3DistalPhalanxBoneCenterY- hand1Finger4DistalPhalanxBoneCenterY))
                                                        +((hand1Finger3DistalPhalanxBoneCenterZ- hand1Finger4DistalPhalanxBoneCenterZ)*(hand1Finger3DistalPhalanxBoneCenterZ- hand1Finger4DistalPhalanxBoneCenterZ)))

                hand1DistalFinger4Finger5+=math.sqrt(((hand1Finger4DistalPhalanxBoneCenterX- hand1Finger5DistalPhalanxBoneCenterX)*(hand1Finger4DistalPhalanxBoneCenterX- hand1Finger5DistalPhalanxBoneCenterX))
                                                        +((hand1Finger4DistalPhalanxBoneCenterY- hand1Finger5DistalPhalanxBoneCenterY)*(hand1Finger4DistalPhalanxBoneCenterY- hand1Finger5DistalPhalanxBoneCenterY))
                                                        +((hand1Finger4DistalPhalanxBoneCenterZ- hand1Finger5DistalPhalanxBoneCenterZ)*(hand1Finger4DistalPhalanxBoneCenterZ- hand1Finger5DistalPhalanxBoneCenterZ)))


        ans= str( hand1finger1CentreTip/self.NUM_FRAME_GRABS) + ','
        ans+= str( hand1finger2CentreTip/self.NUM_FRAME_GRABS) + ','
        ans+= str( hand1finger3CentreTip/self.NUM_FRAME_GRABS) + ','
        ans+= str( hand1finger4CentreTip/self.NUM_FRAME_GRABS) + ','
        ans+= str( hand1finger5CentreTip/self.NUM_FRAME_GRABS) + ','

        ans+= str(hand1ProximalFinger1Finger2/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1ProximalFinger2Finger3/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1ProximalFinger3Finger4/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1ProximalFinger4Finger5/self.NUM_FRAME_GRABS) + ','

        ans+= str(hand1IntermediateFinger1Finger2/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1IntermediateFinger2Finger3/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1IntermediateFinger3Finger4/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1IntermediateFinger4Finger5/self.NUM_FRAME_GRABS) + ','

        ans+= str(hand1DistalFinger1Finger2/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1DistalFinger2Finger3/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1DistalFinger3Finger4/self.NUM_FRAME_GRABS) + ','
        ans+= str(hand1DistalFinger4Finger5/self.NUM_FRAME_GRABS) + ','

        ans += str(sumHands/self.NUM_FRAME_GRABS) + ','
        ans += str(sumFingers/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1GrabStrength/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1PinchStrength/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Confidence/self.NUM_FRAME_GRABS) + ','
        ans += str(pitch1/self.NUM_FRAME_GRABS) + ','
        ans += str(yaw1/self.NUM_FRAME_GRABS) + ','
        ans += str(roll1/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger1MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger1ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        

        ans += str(hand1Finger1IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        

        ans += str(hand1Finger1DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        #NEXT 2
        ans += str(hand1Finger2MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger2ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        

        ans += str(hand1Finger2IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        

        ans += str(hand1Finger2DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        #NEXT 3
        ans += str(hand1Finger3MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger3ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        

        ans += str(hand1Finger3IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        

        ans += str(hand1Finger3DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        #NEXT 4
        ans += str(hand1Finger4MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger4ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        

        ans += str(hand1Finger4IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        

        ans += str(hand1Finger4DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        #NEXT 5
        ans += str(hand1Finger5MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger5ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        

        ans += str(hand1Finger5IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        

        ans += str(hand1Finger5DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','

        


        
        """
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','

        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','
        finalAns+= str(/self.NUM_FRAME_GRABS) + ','


        ans += str(/self.NUM_FRAME_GRABS) + ','

        ans += str(/self.NUM_FRAME_GRABS) + ','

        ans += str(/self.NUM_FRAME_GRABS) + ','

        ans += str(/self.NUM_FRAME_GRABS) + ','

        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','

        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','

        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','
        ans += str(/self.NUM_FRAME_GRABS) + ','"""
        

        return ans

        

def main():
    # Create a sample listener and controller.
    listener = GenerateTrainingSet()
    controller = Leap.Controller()

    # Have a sample listener recieve events from the controller
    controller.add_listener(listener)
    listener.doTheThing(controller)

if __name__ == "__main__":
    main()
