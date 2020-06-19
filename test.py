import os

def get_texture(path):
    texture_list = os.listdir(path=os.getcwd()+"/"+path+"/")
    name= os.listdir(path=path+"/")
    i=0
    while i != len(texture_list):
        name[i] = os.getcwd()+"/"+path+"/"+texture_list[i]
        print(texture_list[i])
        i += 1
get_texture("textures")