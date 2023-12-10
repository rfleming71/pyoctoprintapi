"""Sample api calls for testing"""

TEST_JOB = """
{
   "job":{
      "estimatedPrintTime":null,
      "filament":{
         "length":null,
         "volume":null
      },
      "file":{
         "date":null,
         "name":null,
         "origin":null,
         "path":null,
         "size":null
      },
      "lastPrintTime":null,
      "user":null
   },
   "progress":{
      "completion":45.65,
      "filepos":null,
      "printTime":15432,
      "printTimeLeft":12354,
      "printTimeOrigin":null
   },
   "state":"Printing"
}"""

TEST_PRINTER = """
{
   "sd":{
      "ready":false
   },
   "state":{
      "flags":{
         "cancelling":false,
         "closedOrError":false,
         "error":false,
         "finishing":false,
         "operational":true,
         "paused":false,
         "pausing":false,
         "printing":false,
         "ready":true,
         "resuming":false,
         "sdReady":false
      },
      "text":"Operational"
   },
   "temperature":{
      "bed":{
         "actual":14.53,
         "offset":-5,
         "target":60
      },
      "tool0":{
         "actual":14.17,
         "offset":10,
         "target":200
      }
   }
}
"""

TEST_SERVER = """
{"safemode":"bad_file","version":"1.5.3"}
"""

TEST_SETTINGS_TRACKING = """
{
   "enabled":false,
   "events":{
      "commerror":true,
      "plugin":true,
      "pong":true,
      "printer":true,
      "printer_safety_check":true,
      "printjob":true,
      "slicing":true,
      "startup":true,
      "throttled":true,
      "update":true
   },
   "ping":null,
   "pong":86400,
   "server":null,
   "unique_id":"6c4fae84-4be3-4c4d-8fbd-de9d0c3e1fcb"
}
"""

TEST_SETTINGS_DISCOVERY = """
{
   "httpPassword":"password",
   "httpUsername":"username",
   "publicHost":"host",
   "publicPort":80,
   "upnpUuid":"436fc3ec-fc2e-4851-b289-eb17974aa706"
}
"""

TEST_SETTINGS_CAMERA = """
{
   "bitrate": "10000k",
   "cacheBuster": false,
   "ffmpegPath": "/usr/bin/ffmpeg",
   "ffmpegThreads": 1,
   "ffmpegVideoCodec": "libx264",
   "flipH": false,
   "flipV": false,
   "rotate90": false,
   "snapshotSslValidation": true,
   "snapshotTimeout": 5,
   "snapshotUrl": "http://127.0.0.1:8080/?action=snapshot",
   "streamRatio": "16:9",
   "streamTimeout": 5,
   "streamUrl": "/webcam/?action=stream",
   "timelapseEnabled": true,
   "watermark": true,
   "webcamEnabled": true
}
"""

TEST_SETTINGS_CAMERA_1 = """
{
   "bitrate": "10000k",
   "cacheBuster": false,
   "ffmpegPath": "/usr/bin/ffmpeg",
   "ffmpegThreads": 1,
   "ffmpegVideoCodec": "libx264",
   "flipH": false,
   "flipV": false,
   "rotate90": false,
   "snapshotSslValidation": true,
   "snapshotTimeout": 5,
   "snapshotUrl": "http://127.0.0.1:8080/?action=snapshot",
   "streamRatio": "16:9",
   "streamTimeout": 5,
   "streamUrl": "http://127.0.0.1:8000/webcam/?action=stream",
   "timelapseEnabled": true,
   "watermark": true,
   "webcamEnabled": true
}
"""

# go2rtc style
TEST_SETTINGS_CAMERA_2 = """
{
   "bitrate": "10000k",
   "cacheBuster": false,
   "ffmpegPath": "/usr/bin/ffmpeg",
   "ffmpegThreads": 1,
   "ffmpegVideoCodec": "libx264",
   "flipH": false,
   "flipV": false,
   "rotate90": false,
   "snapshotSslValidation": true,
   "snapshotTimeout": 5,
   "snapshotUrl": "http://127.0.0.1:1984/api/frame.jpeg?src=streamname",
   "streamRatio": "16:9",
   "streamTimeout": 5,
   "streamUrl": "webrtc://127.0.0.1:1984/api/webrtc?src=streamname",
   "timelapseEnabled": true,
   "watermark": true,
   "webcamEnabled": true
}
"""
