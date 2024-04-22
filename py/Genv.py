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
    # print(variable_name,new_value,ENV["ENV_PATH"],ENV)
    os.environ[variable_name] = new_value
    ENV[variable_name] = new_value
    print("!",variable_name,new_value)
    if variable_name == "_delete_S_V_file" and new_value == "DELETE-S-V":
        delete_files_in_folder(".\\py\\video")
        delete_files_in_folder(".\\py\\sound")
    if variable_name == "_delete_all" and new_value == "DELETE-ALL":
        print(os.path.abspath(os.path.join(os.path.abspath(ENV["SCRIPT_DIRECTORY"]), os.pardir, os.pardir)))
        delete_files_in_folder(os.path.abspath(os.path.join(os.path.abspath(ENV["SCRIPT_DIRECTORY"]), os.pardir)))

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
        print(f"資料夾 {folder_path} 不存在")
        return
    
    try:
        # 遞迴刪除資料夾中的所有檔案和資料夾
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                # os.remove(file_path)
                print(f"已刪除檔案: {file_path}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                # os.rmdir(dir_path)
                print(f"已刪除資料夾: {dir_path}")
        print(f"已刪除資料夾 {folder_path} 中的所有檔案和資料夾")
        # os.rmdir(folder_path)
        print(f"已刪除資料夾 {folder_path} ")
    except Exception as e:
        print(f"無法刪除資料夾 {folder_path}, 錯誤訊息: {e}")


if __name__=='__main__':
    print(ENV)
    update_env_variable("MainRoomCodde","4545454")