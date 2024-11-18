import openai
import json
import time
from image2base64 import image_to_base64
api_key=""
base_url=''

class Creation:
    def __init__(self, system_msg, image=None,model="gpt-4o-mini", temprature=1, max_tokens=4096, top_p=1,
                 frequency_penalty=0, presence_penalty=0):
        # parameter
        self.msg = [{"role": "system", "content": system_msg}]
        if image:
            pass
        else:
            self.msg = [{"role": "system", "content": system_msg}]
        self.model = model
        self.temp = temprature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    # input prompt, return explicit norms
    def create(self, prompt,image=None):
       if image:
           user_prompt = {"role": "user", "content": [{"type":"text","text":prompt},{"type":"image_url","image_url": {"url": f"data:image/jpeg;base64,{image}"}}]}
           self.msg.append(user_prompt)
       else:
           user_prompt = {"role": "user", "content": prompt}
           self.msg.append(user_prompt)
       client = openai.OpenAI(api_key=api_key,base_url=base_url)
       gpt_ret=None
       for i in range(5):
           try:
               gpt_ret = client.chat.completions.create(model=self.model, messages=self.msg, temperature=self.temp,
                                                        max_tokens=self.max_tokens, top_p=self.top_p,
                                                        frequency_penalty=self.frequency_penalty,
                                                        presence_penalty=self.presence_penalty)
               break
           except:
               time.sleep(10)

       # ret_str = json.dumps(gpt_ret["choices"][0]["message"])
       # ret_dict = json.loads(ret_str)
       self.msg.pop(-1)
       if not gpt_ret:
           return "ERROR:No result return."
       else:
           response = gpt_ret.choices[0].message.content
           return response
       # print(ret_dict["content"])
       # self.msg.append({"role": "assistant", "content": ret_dict["content"]})



class player:

    def __init__(self,M,system_msg=''):
        self.memory=[]
        self.memory_length=M
        self.creation=Creation(system_msg)
        self.committed=False
        self.committed_name=''

    def player_switch(self,name):
        self.committed=True
        self.committed_name=name

    def memory_update(self,m):
        if len(self.memory)<self.memory_length:
            self.memory.append(m)
        else:
            self.memory.pop(0)
            self.memory.append(m)
        return

    def response(self,prompt,image=None):
         if not self.committed:
             return self.creation.create(prompt=prompt,image=image)
         else:
             return self.committed_name

    def get_memory_length(self):
        return len(self.memory)

    def get_memory_list(self):
        return ','.join(self.memory)


if __name__=='__main__':
     # path="./prompt/image_description.txt"
     # with open(path,'r',encoding='utf-8') as f:
     #     prompt=f.read()
     #
     # image_path="./images/Mary.jpg"
     # image=image_to_base64(image_path)
     # persona=Creation(prompt)
     # result=persona.create(prompt='Now return your result.',image=image)
     # print(result)
     # result=''.join(result.splitlines()[1:-1])
     # print(result)
     # with open("./prompt/Mary.json",'w',encoding='utf-8') as f:
     #     json.dump(json.loads(result),fp=f,indent=4)
     c=Creation('')
     prompt=input('请输入：')
     print(c.create(prompt))




