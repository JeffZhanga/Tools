import os
import json  
path_js ="/root/json_test"
IMG_W = 1280
IMG_H = 720
# 打开文件并读取内容  

def parsefile(path_js):
    with open(path_js, 'r', encoding='utf-8') as file:  
        # 使用json.load()方法解析JSON数据  
        data = json.load(file)  
    
    # 打印解析后的Python对象  
    print(data)  
    print(data['frameid'])  # 提取name字段的值  
    print(data['frametime'])   # 提取age字段的值
    frame_width = 0
    frame_dist = 0
    dist2center = 100000000
    for rect in data['rects']:
        print(rect['x'])
        print(rect['y'])
        print(rect['width'])
        print(rect['height'])
        print(rect['dist'])
        print(rect['realwidth'])
        c_x = rect['x'] + rect['width']/2
        c_y= rect['y']  + rect['height']/2
        dis_c = (c_x - IMG_W/2)*(c_x - IMG_W/2) + (c_y - IMG_H/2)*(c_y - IMG_H/2)
        if(dis_c<dist2center):
            dist2center =dis_c
            frame_width = rect['realwidth']
            frame_dist = rect['dist']
    return frame_dist,frame_width
    # sumdist+=frame_dist
    # sumw+=frame_width
    # if(dist2center!=100000000):
    #     num_frame+=1
def read_json_files_in_directory(directory_path):
    # 确保路径存在
    sumdist = 0
    sumw = 0
    num_frame = 0
    if not os.path.exists(directory_path):
        print(f"指定的路径 '{directory_path}' 不存在")
        return

    # 遍历目录中的所有文件
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # 检查文件是否是JSON文件
        if filename.endswith('.json'):
            print(f"正在读取文件: {filename}")
            frame_dist,frame_width=parsefile(filepath)
            if(frame_dist!=0 and frame_width!=0):
                
                sumdist+=frame_dist
                sumw+=frame_width
                num_frame+=1
    print('dist arv: ',sumdist/num_frame)
    print('width arv: ',sumw/num_frame)
    print('frame num: %d',num_frame)

read_json_files_in_directory(path_js)
