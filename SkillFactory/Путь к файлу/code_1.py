"""Создайте любой файл на операционной системе под название input.txt и 
построчно перепишите его в файл output.txt."""

with open('C:\MY_FOLDER\IDE\SkillFactory\Путь к файлу\input.txt','r',encoding='utf8') as f:
    with open('C:\MY_FOLDER\IDE\SkillFactory\Путь к файлу\output.txt','w',encoding='utf8') as nf:
        for i in f:
            nf.write(f'{i}\n')