import os
import random



def make_commit(days: int):
    if days <1:
        return os.system('git push')
    else:
        dates = f'{days-random.randint(150,200)} days ago'
        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')
        os.system('git add data.txt')
        os.system('git commit --date="'+dates+'" -m"first commit"')
        return days * make_commit(days-1)

make_commit(40)
