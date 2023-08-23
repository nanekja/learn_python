class MaxSizeList(object):
    def __init__(self, length):
        self.len=length
        self.que=[]

    def push(self, text):
        self.que.append(text)
        if len(self.que)>self.len:
            self.que.pop(0)

    def get_list(self):
        return self.que
        




    