'''
  If you're on Linux-based operating system you'll need mplayer to 
  play around the script.

  This command will install mplayer and you're good to go.

    sudo apt-get install mplayer

  If you want to use other player, assuming you know what you're doing, 
  just change LINUX_BASE_OS string to contain whatever new player you wanna
  invoke during script interpretation.

'''

LINUX_BASE_OS = 'mplayer'

'''
  Getting this to work in Windows requires vlc media player.

  If this isn't the path you've installed your VLC player to then go into 
  program files and search for a folder VideoLAN. Just copy/paste the whole 
  path in the WINDOWS_BASE_OS string. 

  After doing this you're good to go. 

'''


WINDOWS_BASE_OS = 'C:/Program Files (x86)/VideoLAN/VLC/'
WINDOWS_BASE_OS += 'vlc.exe'
