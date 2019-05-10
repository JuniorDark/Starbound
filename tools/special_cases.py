#!/usr/bin/python
# -*- coding: utf-8 -*-
from re import compile as regex

def matches(patts, filename):
  for p in patts:
    if not p.match(filename) is None:
      return True
  return False

class SpecialSection():

  def __init__(self, name, pathPatterns, filePatterns, all_conditions = False):
    self.name = name
    self.allcond = all_conditions
    self.fpat = []
    self.ppat = []
    for pat in filePatterns:
      self.fpat.append(regex(pat))
    for pat in pathPatterns:
      self.ppat.append(regex(pat))

  def match(self, filename, path):
    fmatch = matches(self.fpat, filename)
    if fmatch and not self.allcond:
      return True
    pmatch = matches(self.ppat, path)
    if pmatch and (fmatch or not self.allcond):
      return True
    return False

specialSections = [
  SpecialSection("Adjetivo", [], ["^.*quests/generated/pools/guardthemes\.config$"]),
  SpecialSection("Acusativo", [], ["^.*quests/generated/pools/weapon\.config$"]),
  SpecialSection("Chance", [], ["^.*pools/hatadjectives.config$"]),
  SpecialSection("Expressão regular (não para tradução, mas para apoiar nomes em alfabeto cirílico)", ["^.*/regex$"], ["^.*\.config$"], True),
  SpecialSection("Aderiu ao adjetivo do chão",
    ["^.*generatedText/fluff/2/.*$"],
    ["^.*quests/generated/templates/spread_rumors.questtemplate$"], True),
  SpecialSection("Preposição", ["^.*generatedText/fluff/3/.*$"],
    ["^.*quests/generated/templates/escort\.questtemplate$"], True),
  SpecialSection("Preposição", [".*generatedText/fluff/5/.*$"],
    ["^.*quests/generated/templates/kidnapping\.questtemplate$"], True),
  SpecialSection("Plural", ["^.*generatedText/fluff/3/.*$"],
    ["^.*kill_monster_group\.questtemplate$"], True),
  SpecialSection("Genitivo", ["^.+/name$"],
    ["^.*pools/monsterthreats\.config$"], True),
]
