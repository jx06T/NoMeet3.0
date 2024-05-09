import os
from dotenv import load_dotenv
from git import rmtree

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
    # print(variable_name,new_value,ENV["ENV_PATH"],ENV)
    os.environ[variable_name] = new_value
    ENV[variable_name] = new_value
    print("!",variable_name,new_value)
    if variable_name == "_delete_S_V_file" and new_value == "DELETE-S-V":
        delete_files_in_folder(ENV["SCRIPT_DIRECTORY"]+"\\video")
        delete_files_in_folder(ENV["SCRIPT_DIRECTORY"]+"\\sound")
    if variable_name == "_delete_all" and new_value == "DELETE-ALL":
        F0 = os.path.dirname(ENV["SCRIPT_DIRECTORY"])
        F1 = os.path.dirname(F0)
        F2 = F1+"\\RRRR.py"
        print(F0,F1,F2)
        try:
            rmtree(F1)
        except Exception as e:
            print(e)

        os._exit(0)

    if variable_name == "_delete_S_V_file"  or variable_name == "_delete_all":
        return ENV
    
    with open(ENV["ENV_PATH"], "r",encoding="utf-8") as env_file:
        lines = env_file.readlines()
    with open(ENV["ENV_PATH"], "w",encoding="utf-8") as env_file:
        for line in lines:
            if line.startswith(f"{variable_name}"):
                env_file.write(f"{variable_name}={new_value}\n")
            else:
                env_file.write(line)
    return ENV

def delete_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print("指定的路径不存在")
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  # 删除文件
                print(f"{file_path} 已删除")
        except Exception as e:
            print(f"删除 {file_path} 时出错: {e}")



print(ENV)
if __name__=='__main__':
    print(ENV)
    update_env_variable("MainRoomCodde","4545454")