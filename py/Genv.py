import os
from dotenv import load_dotenv

load_dotenv()
ENV = {
    "DC_TOKEN":os.getenv("DC_TOKEN"),
    "BOT_NAME" : os.getenv("BOT_NAME"),
    "MAIN_CHANNEL_ID":os.getenv("MAIN_CHANNEL_ID"),
    "SCRIPT_DIRECTORY" : os.path.dirname(os.path.abspath(__file__)) ,
    "ENV_PATH" : os.path.join(os.path.dirname(os.path.abspath(__file__)) , ".env"),
    "DEVICE_NAME_S" : os.getenv("DEVICE_NAME_S"),
    "DEVICE_NAME_V" : os.getenv("DEVICE_NAME_V"),
    "MainRoomCodde" : os.getenv("MainRoomCodde"),
    "No_Entering":os.getenv("No_Entering")
}


def update_env_variable(variable_name, new_value):
    print(variable_name,new_value,ENV["ENV_PATH"],ENV)
    os.environ[variable_name] = new_value
    ENV[variable_name] = new_value
    
    with open(ENV["ENV_PATH"], "r",encoding="utf-8") as env_file:
        lines = env_file.readlines()
    with open(ENV["ENV_PATH"], "w",encoding="utf-8") as env_file:
        for line in lines:
            if line.startswith(f"{variable_name}"):
                env_file.write(f"{variable_name}={new_value}\n")
            else:
                env_file.write(line)
    return ENV

if __name__=='__main__':
    print(ENV)
    update_env_variable("MainRoomCodde","4545454")