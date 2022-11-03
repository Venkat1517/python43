import yaml
import configparser
import os,sys,json
#Globalvariables
YamlData=""
ConfigData=""
INPUTFILEPATH=""

#Errors
SUCCESS=0
YAML_FILE_NOTFOUND=1
YAML_PARSE_ERROR=2
CONFIG_FILE_NOTFOUND=3
WRONG_OUTPUT_FORMAT=4
WRONG_INPUT_FORMAT=5

#Reading the yaml file and parsing the data
def read_yarn():
    global YamlData
    if(os.path.exists(INPUTFILEPATH)):
        with open("file.yaml", "r") as stream:
            try:
                YamlData=yaml.safe_load(stream)
                return SUCCESS
            except yaml.YAMLError as exc:
                print(exc)
                return YAML_PARSE_ERROR
    else:
        print('Provided yaml file is not present...')
        return YAML_FILE_NOTFOUND
    
#Reading the config file and parsing the data
def read_conf():
    global ConfigData
    if(os.path.exists(INPUTFILEPATH)):
        config = configparser.RawConfigParser()
        config.read('data.txt')
        ConfigData = dict(config.items('My Section'))
        return SUCCESS
    else:
        print('Provided config file is not present...')
        return CONFIG_FILE_NOTFOUND


def create_outdata():
    if(OutputFormat=='1'):
        json_object = json.dumps(YamlData, indent=4)
        with open("Out.json", "w") as outfile:
            outfile.write(json_object)
        print('Json file created ...')
        return SUCCESS
    elif(OutputFormat=='2'):
        os.environ['cgpa'] = YamlData['cgpa']
        os.environ['name'] = YamlData['cgpa']
        os.environ['phonenumber'] = YamlData['phonenumber']
        os.environ['rollno'] = YamlData['rollno']
        print('Env variales set ...')
        return SUCCESS
    else:
        print("Invalid Output argument")
        return WRONG_OUTPUT_FORMAT
    
def main():
    global OutputFormat,INPUTFILEPATH
    print("Please provide input file format..")
    print("1.YAML")
    print("2.CONFIG")
    InputFormat=input("Please choose 1 or 2..")
    if(InputFormat not in ("1","2")):
        print("wrong input format selected...")
        return WRONG_INPUT_FORMAT
    INPUTFILEPATH=input("Please provide Input PATH...")
    if(InputFormat=="1"):
        YarnReturn=read_yarn()
        if(YarnReturn!=SUCCESS):
            return YarnReturn
    elif(InputFormat=="2"):
        ConfigReturn=read_yarn()
        if(ConfigReturn!=SUCCESS):
            return ConfigReturn
    print("Please provide out file format..")
    print("1.JSON")
    print("2.ENV")
    OutputFormat=input("Please choose 1 or 2..")
    if(OutputFormat not in ("1","2")):
        print("wrong out format selected...")
        return WRONG_OUTPUT_FORMAT
    OutReturn=create_outdata()
    if(OutReturn!=SUCCESS):
        return OutReturn
    return SUCCESS
if(__name__=='__main__'):
    r=main()
    sys.exit(r)
