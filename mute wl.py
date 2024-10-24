from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# List of all sessions
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    if session.Process and session.Process.name() == "wallpaper32.exe":  # Specify your program here
        volume = session.SimpleAudioVolume
        volume.SetMute(1, None)  # Mute the application
        print(f"Muted: {session.Process.name()}")
