### Overview 

Logging with python

Logging level

- Critical
- Error
- Warning
- Info
- Debug

The way this works with logging is if you mention Warning in logging level then all above level will also be logged

Example 
- Logging level - Warning --> Logs will capture -- Warning,Error,Critical
- Logging level - Info --> Logs will capture -- Info,Warning,Error,Critical
- Logging level - Debug --> Logs will capture -- Debug,Info,Warning,Error,Critical

Logging configuration -- logging.basicConfig(filename="log.txt",level=logging.DEBUG,filemode='a')
If set to logging.basicConfig() 
- Error will be printing on screen
- Level will be warning
- Filemode will be append
