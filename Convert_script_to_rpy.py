import re
import sys
import os

talk_pattern=r"\s*([^「]+)\s*「([^」]*)」\s*"


name_labels={}

def talk_sentence_conv(s):
    global name_labels
    ret=re.match(talk_pattern,s)

    name_l=name_labels[ret.groups()[0]]


    return "{0} \"「{1}」\"".format(name_l,ret.groups()[1])

def Get_name_from_talk_sentence(s):
    ret=re.match(talk_pattern,s)

    #print(ret.groups())
    return ret.groups()[0]

def normal_sentence_conv(s):
    return "\"{0}\"".format(s)

def if_sentence(s):
    ret=re.match(talk_pattern,s)

    return ret is not None and len(ret.groups())!=0

def file_conv(from_fname,to_fname):
    global name_labels

    template_str=""
    with open(os.path.join(os.getcwd(),"template.rpy"),encoding="utf-8") as f:
        template_str=f.read()
    
    template_define_str="define {0} = Character('{1}', color=\"#000000\")"

    with open(from_fname,encoding="utf-8") as f:
        Script=""
        fron_file_str=f.readlines()

        fron_file_str=list(map(lambda v:v.replace("\n","").replace("\r",""),fron_file_str))

        for s in fron_file_str:
            if if_sentence(s):
                name=Get_name_from_talk_sentence(s)
                if name not in name_labels:
                    l=input("What is the label of {} >".format(name))
                    name_labels[name]=l

        for s in fron_file_str:
            if s=="":
                continue
            if if_sentence(s):
                temp=talk_sentence_conv(s)
            else:
                temp=normal_sentence_conv(s)
            Script+=" "*4+temp+"\n"

        define_str=""

        for name,label in name_labels.items():
            define_str+=template_define_str.format(label,name)+"\n"

        ret=template_str.format(define_str,Script)
    
    with open(to_fname,mode="w",encoding="utf-8") as f:
        f.write(ret)

file_conv(sys.argv[1],sys.argv[2])


    


