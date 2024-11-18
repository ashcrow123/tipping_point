from Creation import *
from image2base64 import image_to_base64
import os
import random
import json

def random_pairing(list):
    # 确保列表元素个数是偶数
    if len(list) % 2 != 0:
        raise ValueError("The number of elements in the list must be an even number.")

    # 随机打乱列表
    random.shuffle(list)

    # 将元素两两配对
    pairs = [(list[i], list[i + 1]) for i in range(0, len(list), 2)]

    return pairs

class game:
    def __init__(self,N,C,M,T,game_descrip,name):
        self.N=N
        self.C=C
        self.M=M
        self.T=T
        self.player_list=[]
        self.game_descrip=game_descrip
        # self.game_name=input('Naming your new game:')
        self.game_name=name
        self.folderpath = os.path.join('./game', self.game_name)
        self.count_1=0
        self.count_2=0
        # if image_path:
        #     self.image = image_to_base64(image_path)
        # self.image=''
        self.record_1={}
        self.record_2={}
        while os.path.isdir(self.folderpath):
            print('The name is already in use.\n')
            self.game_name=input('Please enter the new name:')
            self.folderpath=os.path.join('./game',self.game_name)

    def convention_judge(self):
        if self.player_list[0].memory:
            flag = self.player_list[0].memory[0]
        else:
            return False

        for i in self.player_list:
            if not i.memory:
                return False
            for j in i.memory:
                if j!=flag:
                    return False
        return True

    # def start_game(self):
    #     os.mkdir(self.folderpath)
    #     for i in range(self.N):
    #         self.player_list.append(player(M=self.M,system_msg=self.game_descrip.replace('!<game_round>!',str(self.M))))
    #
    #     with open('prompt/round_begin_v1.txt', 'rt', encoding='utf-8') as f:
    #         begin_prompt=f.read()
    #     # with open('prompt/round_end.txt', 'rt', encoding='utf-8') as f:
    #     #     end_prompt=f.read()
    #     while 1:
    #         if self.convention_judge():
    #             break
    #         self.count_1 += 1
    #         if self.count_1>=80:
    #             print('Social convention fail to form.')
    #             return
    #         pair = list(range(self.N))
    #         pairs = random_pairing(pair)
    #         self.record_1[f'round_{self.count_1}'] = []
    #         for i, j in pairs:
    #             memory_i=f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[i].get_memory_length())} rounds are {self.player_list[i].get_memory_list()}' if self.player_list[i].get_memory_length() else 'This is the first round of the game.'
    #             memory_j=f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[j].get_memory_length())} rounds are {self.player_list[j].get_memory_list()}' if self.player_list[j].get_memory_length() else 'This is the first round of the game.'
    #
    #             begin_prompt_i = begin_prompt.replace('!<memory_state>!',memory_i)
    #             begin_prompt_j = begin_prompt.replace('!<memory_state>!',memory_j)
    #
    #             response_i = self.player_list[i].response(prompt=begin_prompt_i, image=self.image)
    #             response_j = self.player_list[j].response(prompt=begin_prompt_j, image=self.image)
    #
    #
    #             print('----------------------------------------------------------------')
    #             print(f'Convention formation:round {self.count_1}:\n')
    #             print(response_i)
    #             print(response_j)
    #             self.player_list[i].memory_update(response_j)
    #             self.player_list[j].memory_update(response_i)
    #             self.record_1[f'round_{self.count_1}'].append(response_i)
    #             self.record_1[f'round_{self.count_1}'].append(response_j)
    #
    #
    #
    #     Committed_name = Creation(system_msg=self.game_descrip.replace('!<game_round>!', str(self.M)))
    #     committed_name = Committed_name.create(prompt=begin_prompt.replace('!<memory_state>!', 'This is the first round of the game.'),image=self.image)
    #
    #     while committed_name==self.player_list[0].memory[0]:
    #
    #         committed_name = Committed_name.create(prompt=begin_prompt.replace('!<memory_state>!', 'This is the first round of the game.'),image=self.image)
    #
    #
    #     for i in range(self.C):
    #         self.player_list[i].player_switch(committed_name)
    #
    #     for round in range(self.T):
    #         self.count_2 +=1
    #         pair = list(range(self.N))
    #         pairs = random_pairing(pair)
    #         self.record_2[f'round_{self.count_2}'] = []
    #         for i, j in pairs:
    #             memory_i = f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[i].get_memory_length())} rounds are {self.player_list[i].get_memory_list()}' if \
    #             self.player_list[i].get_memory_length() else 'This is the first round of the game.'
    #             memory_j = f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[j].get_memory_length())} rounds are {self.player_list[j].get_memory_list()}' if \
    #             self.player_list[j].get_memory_length() else 'This is the first round of the game.'
    #
    #             begin_prompt_i = begin_prompt.replace('!<memory_state>!', memory_i)
    #             begin_prompt_j = begin_prompt.replace('!<memory_state>!', memory_j)
    #             response_i = self.player_list[i].response(prompt=begin_prompt_i, image=self.image)
    #             response_j = self.player_list[j].response(prompt=begin_prompt_j, image=self.image)
    #             print('---------------------------------------------------------------------')
    #             print(f'Convention change:round {self.count_2}:\n')
    #             print(response_i)
    #             print(response_j)
    #             self.player_list[i].memory_update(response_j)
    #             self.player_list[j].memory_update(response_i)
    #             self.record_2[f'round_{self.count_2}'].append(response_i)
    #             self.record_2[f'round_{self.count_2}'].append(response_j)
    #
    #     path_1=os.path.join(self.folderpath,'Formation_of_conventions,json')
    #     with open(path_1,'w',encoding='utf-8') as f:
    #         json.dump(self.record_1,f,indent=4)
    #     path_2 = os.path.join(self.folderpath, 'Change_of_conventions,json')
    #     with open(path_2, 'w', encoding='utf-8') as f:
    #         json.dump(self.record_2, f, indent=4)

    def get_round_1_count(self):
        return self.count_1

    def start_game(self,image_description,image_path):
        os.mkdir(self.folderpath)
        path_1 = os.path.join(self.folderpath, 'Formation_of_conventions')
        path_2 = os.path.join(self.folderpath, 'Change_of_conventions')
        os.mkdir(path_1)
        os.mkdir(path_2)
        for i in range(self.N):
            self.player_list.append(
                player(M=self.M, system_msg=self.game_descrip.replace('!<game_round>!', str(self.M))))

        with open('prompt/round_begin_v1.txt', 'rt', encoding='utf-8') as f:
            begin_prompt = f.read()
        with open(image_description,'r',encoding='utf-8') as f:
            initial_data = json.load(f)
        convention_name=initial_data['name1']
        committed_name=initial_data['name2']
        image=image_to_base64(image_path)


        for i in self.player_list:
                for j in range(self.M):
                    i.memory.append(convention_name)

        for i in range(self.C):
                self.player_list[i].player_switch(committed_name)

        for round in range(self.T):
            self.count_2 +=1
            pair = list(range(self.N))
            pairs = random_pairing(pair)
            self.record_2[f'round_{self.count_2}'] = []
            for i, j in pairs:
                memory_i = f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[i].get_memory_length())} rounds are {self.player_list[i].get_memory_list()}' if \
                self.player_list[i].get_memory_length() else 'This is the first round of the game.'
                memory_j = f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[j].get_memory_length())} rounds are {self.player_list[j].get_memory_list()}' if \
                self.player_list[j].get_memory_length() else 'This is the first round of the game.'

                begin_prompt_i = begin_prompt.replace('!<memory_state>!', memory_i)
                begin_prompt_j = begin_prompt.replace('!<memory_state>!', memory_j)
                response_i = self.player_list[i].response(prompt=begin_prompt_i,image=image)
                response_j = self.player_list[j].response(prompt=begin_prompt_j,image=image)
                print('---------------------------------------------------------------------')
                print(f'Convention change:round {self.count_2}:\n')
                print(response_i)
                print(response_j)
                self.player_list[i].memory_update(response_j)
                self.player_list[j].memory_update(response_i)
                self.record_2[f'round_{self.count_2}'].append(response_i)
                self.record_2[f'round_{self.count_2}'].append(response_j)
            with open(os.path.join(path_2,f'round_{self.count_2}.json'),'w',encoding='utf-8') as f:
                json.dump(self.record_2[f'round_{self.count_2}'],fp=f,indent=4)

    def start_noimg_game(self,image_description):
        os.mkdir(self.folderpath)
        path_1 = os.path.join(self.folderpath, 'Formation_of_conventions')
        path_2 = os.path.join(self.folderpath, 'Change_of_conventions')
        os.mkdir(path_1)
        os.mkdir(path_2)
        for i in range(self.N):
            self.player_list.append(
                player(M=self.M, system_msg=self.game_descrip.replace('!<game_round>!', str(self.M))))

        with open('prompt/round_begin_v3.txt', 'rt', encoding='utf-8') as f:
            begin_prompt = f.read()
        with open(image_description,'r',encoding='utf-8') as f:
            initial_data = json.load(f)
        convention_name=initial_data['name1']
        committed_name=initial_data['name2']
        image_description=initial_data['Description for the image']
        begin_prompt=begin_prompt.replace("!<image_description>!",image_description)

        for i in self.player_list:
                for j in range(self.M):
                    i.memory.append(convention_name)

        for i in range(self.C):
                self.player_list[i].player_switch(committed_name)

        for round in range(self.T):
            self.count_2 +=1
            pair = list(range(self.N))
            pairs = random_pairing(pair)
            self.record_2[f'round_{self.count_2}'] = []
            for i, j in pairs:
                memory_i = f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[i].get_memory_length())} rounds are {self.player_list[i].get_memory_list()}' if \
                self.player_list[i].get_memory_length() else 'This is the first round of the game.'
                memory_j = f'A new round of games has begun! The names given by your opponents in the last {str(self.player_list[j].get_memory_length())} rounds are {self.player_list[j].get_memory_list()}' if \
                self.player_list[j].get_memory_length() else 'This is the first round of the game.'

                begin_prompt_i = begin_prompt.replace('!<memory_state>!', memory_i)
                begin_prompt_j = begin_prompt.replace('!<memory_state>!', memory_j)
                response_i = self.player_list[i].response(prompt=begin_prompt_i)
                response_j = self.player_list[j].response(prompt=begin_prompt_j)
                print('---------------------------------------------------------------------')
                print(f'Convention change:round {self.count_2}:\n')
                print(response_i)
                print(response_j)
                self.player_list[i].memory_update(response_j)
                self.player_list[j].memory_update(response_i)
                self.record_2[f'round_{self.count_2}'].append(response_i)
                self.record_2[f'round_{self.count_2}'].append(response_j)
            with open(os.path.join(path_2,f'round_{self.count_2}.json'),'w',encoding='utf-8') as f:
                json.dump(self.record_2[f'round_{self.count_2}'],fp=f,indent=4)
        # path_1=os.path.join(self.folderpath,'Formation_of_conventions.json')
        # with open(path_1,'w',encoding='utf-8') as f:
        #     json.dump(self.record_1,f,indent=4)
        # path_2 = os.path.join(self.folderpath, 'Change_of_conventions.json')
        # with open(path_2, 'w', encoding='utf-8') as f:
        #     json.dump(self.record_2, f, indent=4)


# files = os.listdir('./images')
#
# # 过滤出图片文件（假设只处理jpg, png格式的图片）
# image_files = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg'))]


# if image_files:
#     random_image = random.choice(image_files)
#     print(f"A randomly selected picture is: {random_image}")
#     path = os.path.join('./images', random_image)
#     with open('prompt/game_introduction_v4.txt', 'rt', encoding='utf-8') as f:
#         gf = f.read()
#     g = game(N=20, C=5, T=45, M=5, game_descrip=gf,image_description="./prompt/Mary.json")
#     start_time=time.time()
#     print('开始时间：',start_time)
#     g.start_noimg_game()
#     end_time=time.time()
#     exe_time=end_time-start_time
#     print("总共运行时间：",exe_time,'秒')
# else:
#     print("No image file found in the folder.")

with open('prompt/game_introduction_v1.txt', 'rt', encoding='utf-8') as f:
    gf = f.read()
g1 = game(N=20, C=6, T=45, M=13, game_descrip=gf,name='N20C6T60M13 1')
#g2=game(N=20, C=6, T=40, M=10, game_descrip=gf,name='N20C6T40M10 2')
#g3=game(N=20, C=6, T=40, M=10, game_descrip=gf,name='N20C6T40M10 3')
start_time=time.time()
print('开始时间：',start_time)
# g1.start_game(image_description="./prompt/Mary.json",image_path="./images/Mary.jpg")
# g2.start_game(image_description="./prompt/Mary.json",image_path="./images/Mary.jpg")
# g3.start_game(image_description="./prompt/Mary.json",image_path="./images/Mary.jpg")
g1.start_noimg_game(image_description="./prompt/Mary.json")
#g2.start_noimg_game(image_description="./prompt/Mary.json")
#g3.start_noimg_game(image_description="./prompt/Mary.json")
end_time=time.time()
exe_time=end_time-start_time
print("总共运行时间：",exe_time,'秒')



