class CsvException(Exception):
    def __init__(self, message):
        super(CsvException, self).__init__(message)

class ArmCommand():
    def __init__(self, time, jointNumber, angle, grab):
        self.time = time;
        self.jointNumber = jointNumber
        self.angle = angle
        self.grab = grab
        
    def __repr__(self):
        return 'command: Time: {}, joint: {}, angle: {}, grab: {}'.format(self.time, self.jointNumber, self.angle, self.grab)
    
    def getTime(self):
        return self.time
    
    def getJoint(self):
        return self.jointNumber
    
    def getAngle(self):
        return self.angle
    
    def getGrab(self):
        return self.grab


class CommandCsvReader():
    def __init__(self):
        self.filename = None
        self.delimiter = None
        #commands are stored in a dictionary containing a list of commands for each timestamp
        self.commandList = {}
    
    def lineToCommand(self, line):
        if (not line):
            raise CsvException("line is empty")
        falseList = [0, "False", "false", "No", "no", "FALSE"]
        try:
            list = line.split(self.delimiter)
            if (len(list) < 4):
                grab = False
            elif (list[3] in falseList):
                grab = False
            else:
                grab = True
            return ArmCommand(float(list[0]), int(list[1]), int(list[2]), grab)
        except:
            raise CsvException("Something went wrong while parsing the line: " + line)
        
    def getCommandList(self):
        return self.commandList
    
    def getTimeCommands(self, time):
        return self.commandList[time]
    
    def load(self, filename, delimiter):
        self.filename = filename
        self.delimiter = delimiter
        try:
            file = open(self.filename, "r")
        except:
            raise CsvException("Failed to open file " + self.filename)
        try:
            if file.mode == 'r':
                row = file.readline()
                while(row):
                    command = self.lineToCommand(row.strip('\n'))
                    if (command.getTime() in self.commandList):
                        self.commandList[command.getTime()].append(command)
                    else:
                        self.commandList[command.getTime()] = [command]
                    row = file.readline()
        except:
            raise CsvException("Something went wrong while reading the file.")
            
    