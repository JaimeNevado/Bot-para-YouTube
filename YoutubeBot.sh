#!/bin/sh

echo "
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗    ██╗   ██╗██████╗ ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗      ██║   ██║██████╔╝██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██║   ██║██╔═══╝ ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ╚██████╔╝██║     ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
   By Jaime Nevado
"                                                                                                                                

PYTHON="/usr/bin/python3"
FILE="/Users/jaimenevado/Desktop/Bot-para-YouTube/main.py"

ffmpeg -i video.mp4 -vf 'split[original][copy];[copy]scale=-1:ih*(16/9)*(16/9),crop=w=ih*9/16,gblur=sigma=20[blurred];[blurred][original]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2' output.mp4

filename="parte"

ffmpeg -i output.mp4 -c copy -map 0 -segment_time 00:00:30 -start_number 1 -f segment -reset_timestamps 1 ${filename}%02d.mp4

rm video.mp4
rm output.mp4

mv *.mp4 /Users/jaimenevado/Desktop/Bot-para-YouTube/videos

$PYTHON "$FILE"

cd videos
MAX=17
VIDEOS=$(ls | wc -l)

if [[ $VIDEOS -gt $MAX ]]
   then
      echo "borrando 17 primeros videos"
      rm *0*.mp4
      rm *10.mp4
      rm *11.mp4
      rm *12.mp4
      rm *13.mp4
      rm *14.mp4
      rm *15.mp4
      rm *16.mp4      
   else
      echo "borrando TODOS"
      rm *.mp4
fi