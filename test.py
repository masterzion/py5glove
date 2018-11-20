import py5glove
import  time
StepPins =  [1,2,3,4]
obj = py5glove.Glove(-1)
while True:
    obj.GetSample(-1)
    print("GetFingers")
    print( obj.GetFingers() )
    print("GetButtons")
    print( obj.GetButtons() )
    print("GetPos")
    print( obj.GetPos() )
    print("GetRotation")
    print( obj.GetRotation() )
    time.sleep(1)
