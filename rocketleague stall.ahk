XButton2::  ; When the first side button is pressed
{
    Send, {a down}{e down}{RButton down}  ; Press A, E, and right mouse button down
    Send, {a up}{e up}{RButton up}  ; Release A, E, and right mouse button
    Return
}