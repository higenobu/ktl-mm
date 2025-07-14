from  pyknp import Juman, BList, KNP
import time
 
def jumman_parse(text):
    text = text.replace(" ", "")
    text = text.replace("   ", "")
    text = text.replace("＃", "")
    text = text.replace("#", "")
    words = []
    sentences = [text]
    for sentence in sentences:
        try:
            juman = Juman("jumanpp", multithreading=True)
            parse_result = juman.analysis(sentence + "。")
        except:
            print("jumanpp error!!!!!!!!")
            print(sentence)
            continue
        for v in parse_result:
            print(v.genkei)
    return words
 
 
start = time.time()
jumman_parse("形態素解析は面白いです")
end = time.time()
print(end - start)
