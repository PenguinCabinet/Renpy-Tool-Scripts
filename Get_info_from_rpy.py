import re
import sys
import os

talk_pattern=r"\s*([^「]+)\s*「([^」]*)」\s*"


name_labels={}

def talk_sentence_conv(s):
    global name_labels
    ret=re.match(talk_pattern,s)

    name_l=name_labels[ret.groups()[0]]


    return "{0} \"{1}\"".format(name_l,ret.groups()[1])

def Get_name_from_talk_sentence(s):
    ret=re.match(talk_pattern,s)

    #print(ret.groups())
    return ret.groups()[0]

def normal_sentence_conv(s):
    return "\"{0}\"".format(s)

def if_sentence(s):
    ret=re.match(talk_pattern,s)

    return ret is not None and len(ret.groups())!=0

patterns=[
    r"image\s+[^\s]+\s+[^\s]+\s*=\s*\"([^\\\"]+)\".*",
    r"\s*scene\s+([^:]+).*",
    r"\s*play\s+music\s+\"([^\\\"]+)\".*",
    r"\s*play\s+sound\s+\"([^\\\"]+)\".*",
]

def file_conv(from_fname,to_fname):
    global name_labels

    material_infos=[[] for i in range(len(patterns))]

    material_info_items=["キャラクター立ち絵","背景画像","BGM","SE"]

    with open(from_fname,encoding="utf-8") as f:
        from_file_str=f.readlines()

        from_file_str=list(map(lambda v:v.replace("\n","").replace("\r",""),from_file_str))

        for s in from_file_str:
            for i,pattern in enumerate(patterns):
                r=re.match(pattern,s)
                if r is not None and len(r.groups())!=0:
                    material_infos[i].append(r.groups()[0])

        material_infos=list(map(lambda v:sorted(list(set(v))),material_infos))

        ret=""
        for e1,e2 in zip(material_info_items,material_infos):
            ret+="{}\n{}\n\n".format(e1,"\n".join(e2))
    
    with open(to_fname,mode="w",encoding="utf-8") as f:
        f.write(ret)

file_conv(sys.argv[1],sys.argv[2])


    


