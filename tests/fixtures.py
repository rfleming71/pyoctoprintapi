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