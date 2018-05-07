from hmm_segger import HmmSegger
import os

def data_path(filename):
    return os.path.join(os.path.dirname(__file__), "%s" % filename)


hmm_segger1 = HmmSegger()
hmm_segger1.load(filename=data_path("..\\corpus\\hmm.json"))


def hmm_cut(sentence):
    return hmm_segger1.cut(sentence)



print(hmm_cut('希腊的经济结构较特殊。'))