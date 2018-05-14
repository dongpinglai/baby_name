#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class BabyName(object):
    def __init__(self, candidate_first_name=None, candidate_middle_name=None, candidate_last_name=None, is_middleAsLast=True):
        self.candidate_first_name = candidate_first_name or set() 
        self.candidate_middle_name = candidate_middle_name or set()
        self.candidate_last_name = candidate_last_name or set()
        self.is_middleAsLast = is_middleAsLast
        if is_middleAsLast:
            self.candidate_last_name = self.candidate_middle_name 
        self._name_buffer = set()
        self.name_file_path = "bady_name_file.txt"
        self._fp = open(self.name_file_path, "wt")

    def get_full_name(self):
        candidate_names = self.choose_candidate_names()
        candidate_names = set(candidate_names)
        fp = self._fp
        full_names = []
        for candidate_name in candidate_names:
            first = candidate_name[0]
            if first in self.candidate_first_name:
                if all(candidate_name):
                    full_name = "".join(candidate_name)
                if full_name:
                    full_names.append(full_name.encode("utf-8"))
        print len(full_names)
        full_names = filter(self.filter_name, full_names)
        print len(full_names)
        with fp:
            fp.write("\n".join(full_names))

    def filter_name(self, full_name):
        filter_chars = ["安", "彩", "青", "必", "富", "珍", "彪", "衣", "衫"]
        for filter_char in filter_chars:
            if filter_char in full_name:
                return False
        used_chars = ["骞"]
        for used_char in used_chars:
            if used_char in full_name:
                return True
        return False
        
    def choose_candidate_names(self):
        from itertools import permutations
        candidate_names = []
        candidate_first_name = self.candidate_first_name
        candidate_middle_name = self.candidate_middle_name
        candidate_last_name = self.candidate_last_name
        candidate_names.extend(candidate_first_name)
        candidate_names.extend(candidate_middle_name)
        if not self.is_middleAsLast:
            candidate_names.extend(candidate_last_name)
        iter_candidate_names = permutations(candidate_names, 3)
        return iter_candidate_names


if __name__ == "__main__":
    middle_name_string = u"人今任令仰仲企伸布位住伯余佩佳依俊杰倩值伟健字守安宏宜宁宙有家富冠玛笃骏驻骋骆骐骞腾骧骅约珍绅维纬彤形彦彩彪彭衣衫绮装褚希佩纶席心必志忠忻念思恒恩恭情惟慈慧惠育青有肯胜腾不少士臣"
    candidate_first_name = [u"赖"]
    candidate_middle_name = []
    for char in middle_name_string:
        candidate_middle_name.append(char)
    baby_name = BabyName(set(candidate_first_name), set(candidate_middle_name))
    baby_name.get_full_name()
