from sys import argv, exit
import os, subprocess, signal


# Global Declarations

station_dictionary = {
  'metal': 'http://173.231.136.91:8090/',
  'random': 'http://173.231.136.91:8050/',
  'rock': 'http://173.231.136.91:8020/',
  'indie': 'http://173.231.136.91:8070/',
  'main': 'http://173.231.136.91:8000/',
}

# What all stations you can listen to

permissible_names = ['metal', 'random', 'rock', 'indie', 'main']

# Process Name for Windows and Linux

LINUX_BASE_OS = 'mplayer'

WINDOWS_BASE_OS = 'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe'



# Main Program logic

def main():
  handle_args()

  stream_name = which_stream()
  player_name = detect_os()
  
  open_stream(player_name, station_dictionary[stream_name])



# Returns if the station name provided is legal or not

def which_stream():

  try:
    for name in permissible_names:
      if name == argv[1]:
        return argv[1]

    raise Exception('Stream name incorrect')

  except Exception as e:

    print e

  print "Try these ones: "
  print permissible_names

  exit(1)



# Detect which Operating System user is using

def detect_os():
  
  if os.name.upper() == 'LINUX':
    return LINUX_BASE_OS 
  
  else:
    return WINDOWS_BASE_OS



# Open stream using vlc or mplayer

def open_stream(player_name, stream_name):
  print 
  music_pointer = subprocess.Popen([player_name, stream_name], stdin = None, stdout = None, stderr = None, shell = False)



# Logic for handling number of arguments passed in the script

def handle_args():
  if len(argv) <= 1 or len(argv) > 2:
    print "Usage: python radio-reddit.py [station name]"
    print "Station names: "
    print "main, indie, rock, metal, random"
    exit(1)


if __name__ == '__main__':
  main()