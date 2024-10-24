#Persistent
#MaxThreadsPerHotkey 4

; Press and hold the first side mouse button (XButton1) to start spamming
; Release XButton1 to stop spamming
XButton2::
    While GetKeyState("XButton2", "P") ; Check if XButton1 is still being pressed
    {
        Click, right ; Perform the right click action
        Sleep, 50 ; Short pause to prevent CPU overload, adjust as needed
    }
return