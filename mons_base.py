import random
import math

class Pokemon:
	
	def __init__(self, mon, level):
		self.stats = {}
		self.stats["hp"] = None
		self.stats["attack"] = None
		self.stats["spattack"] = None
		self.stats["defense"] = None
		self.stats["spdefense"] = None
		self.stats["speed"] = None
		self.evs = {}
		self.evs["hp"] = 0
		self.evs["attack"] = 0
		self.evs["spattack"] = 0
		self.evs["defense"] = 0
		self.evs["spdefense"] = 0
		self.evs["speed"] = 0
		self.ivs = {}
		self.ivs["hp"] = None
		self.ivs["attack"] = None
		self.ivs["spattack"] = None
		self.ivs["defense"] = None
		self.ivs["spdefense"] = None
		self.ivs["speed"] = None
		self.lvl = None
		self.expToNextLvl = None
		self.currentExp = 0
		self.commulativeExp = 0
		self.ogTrainer = None
		self.mon_type = None
		self.lvl = level
		self.mon_type = mon

		self.GenerateIVs()
		self.UpdateStats()

	def GenerateIVs(self):
		self.ivs["hp"] = random.randint(0, 31)
		self.ivs["attack"] = random.randint(0, 31)
		self.ivs["defense"] = random.randint(0, 31)
		self.ivs["spattack"] = random.randint(0, 31)
		self.ivs["spdefense"] = random.randint(0, 31)
		self.ivs["speed"] = random.randint(0, 31)

	def GiveEV(self, stat, amount):
		self.evs[stat] += amount
		self.UpdateStats()

	def UpdateStats(self):
		self.stats["hp"] = CalculateStatHP(self.ivs["hp"], self.lvl, self.evs["hp"], self.mon_type.baseStats["hp"])
		self.stats["attack"] = CalculateStat(self.ivs["attack"], self.lvl, self.evs["attack"], self.mon_type.baseStats["attack"])
		self.stats["spattack"] = CalculateStat(self.ivs["spattack"], self.lvl, self.evs["spattack"], self.mon_type.baseStats["spattack"])
		self.stats["defense"] = CalculateStat(self.ivs["defense"], self.lvl, self.evs["defense"], self.mon_type.baseStats["defense"])
		self.stats["spdefense"] = CalculateStat(self.ivs["spdefense"], self.lvl, self.evs["spdefense"], self.mon_type.baseStats["spdefense"])
		self.stats["speed"] = CalculateStat(self.ivs["speed"], self.lvl, self.evs["speed"], self.mon_type.baseStats["speed"])
		self.expToNextLvl = CalculateTotalExpAtLvl(self.mon_type.expGroup, self.lvl + 1) - CalculateTotalExpAtLvl(self.mon_type.expGroup, self.lvl)
	
	def RareCandyLevelUp(self):
		self.GiveExp(self.expToNextLvl - self.currentExp)
	
	def LevelUp(self):
		self.currentExp += -self.expToNextLvl
		self.lvl += 1
		if self.lvl == 100:
			self.currentExp = 0
		self.UpdateStats()

	def GiveExp(self, amount):
		if self.lvl != 100:
			self.currentExp += amount
			self.commulativeExp += amount
		while self.currentExp >= self.expToNextLvl:
			self.LevelUp()

	def dumpStats(self):
		print("--Stats--")
		print("hp    " + str(self.stats["hp"]))
		print("att   " + str(self.stats["attack"]))
		print("spatt " + str(self.stats["spattack"]))
		print("def   " + str(self.stats["defense"]))
		print("spdef " + str(self.stats["spdefense"]))
		print("speed " + str(self.stats["speed"]))

	def dumpIVs(self):
		print("--IVs--")
		print("hp    " + str(self.ivs["hp"]))
		print("att   " + str(self.ivs["attack"]))
		print("spatt " + str(self.ivs["spattack"]))
		print("def   " + str(self.ivs["defense"]))
		print("spdef " + str(self.ivs["spdefense"]))
		print("speed " + str(self.ivs["speed"]))

	def dumpEVs(self):
		print("--EVs--")
		print("hp    " + str(self.evs["hp"]))
		print("att   " + str(self.evs["attack"]))
		print("spatt " + str(self.evs["spattack"]))
		print("def   " + str(self.evs["defense"]))
		print("spdef " + str(self.evs["spdefense"]))
		print("speed " + str(self.evs["speed"]))

def CalculateStat(iv, level, ev, base):
	return math.floor((((2 * base + iv + math.floor(ev / 4)) * level) / 100) + 5)

def CalculateStatHP(iv, level, ev, base):
	return math.floor((((2 * base + iv + math.floor(ev / 4)) * level) / 100) + level + 10)

def CalculateTotalExpAtLvl(group, level):
	if group == "Fast":
		#Needs testing
		return math.floor((4 * pow(level, 3)) / 5)
	elif group == "Medium Fast":
		return math.floor(math.pow(level, 3))
	elif group == "Medium Slow":
		#Needs testing
		return math.floor(((6 / 5) * math.pow(level, 3)) - (15 * math.pow(level, 2)) + (100 * level) - 140)
	elif group == "Slow":
		#Needs testing
		return math.floor((5 * math.pow(level, 3)) / 4)
	elif group == "Erratic":
		#Needs testing
		if level <= 50:
			return (math.pow(level, 3)*(100 - level)) / 50
		elif level <= 68:
			return (math.pow(level, 3) * (100 - n)) / 100
		elif level <= 98:
			return (math.pow(level, 3) * math.floor((1911 - (10 * level) / 3))) / 500
		else:
			return (math.pow(level, 3) * (160 - level)) / 100
	elif group == "Fluctuating":
		#Needs testing
		if level <= 15:
			return math.pow(level, 3) * ((math.floor((level + 1) / 3) + 24) / 50)
		elif level <= 36:
			return math.pow(level, 3) * ((level + 14) / 50)
		else:
			return math.pow(level, 3) * ((math.floor(level / 2) + 32) / 50)

#Implement Natures
#Implement basic evolution
