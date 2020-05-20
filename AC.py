#!/usr/bin/env python
#-*-ending:utf-8
# author:zhanglu
import ahocorasick


def build_actree(wordlist):
    actree = ahocorasick.Automaton()
    for index, word in enumerate(wordlist):
        actree.add_word(word, (index, word))
    actree.make_automaton()
    return actree


if __name__ == '__main__':
    wordlist = ['中国', '中山大学', '广州市', '清华大学', '北京市']
    sent = '中山大学是一所位于广州市的综合性院校。'
    actree = build_actree(wordlist=wordlist)
    for i in actree.iter(sent):
        print(i)