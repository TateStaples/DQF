import numpy as np

iterations = 1000000
information = {}  # Tuple[int, bool, ...]: (regret, (probs,))

class Node:
	def __init__(self, num_actions):
		self.regret_sum = np.zeros(num_actions)
		self.strategy_sum = np.zeros(num_actions)
		self.num_actions = num_actions

	def get_strategy(self):
		s = np.maximum(self.regret_sum, 0)
		normalizing_sum = s.sum()
		if normalizing_sum == 0: return np.ones(len(s)) / len(s)
		return s / normalizing_sum

	def get_average_strategy(self):
		avg_strategy = np.zeros(self.num_actions)
		normalizing_sum = 0

		for a in range(self.num_actions):
			normalizing_sum += self.strategy_sum[a]
		for a in range(self.num_actions):
			if normalizing_sum > 0:
				avg_strategy[a] = self.strategy_sum[a] / normalizing_sum
			else:
				avg_strategy[a] = 1.0 / self.num_actions

		return avg_strategy

def cfr(history, dollars, main_player) -> float:
	plays = len(history)
	if plays >= 5: # spread, side, spread, side, spread
		spread1, buy1, spread2, buy2, spread3 = history
		score1 = dollars - (spread1 + 5) if buy1 else (spread1 - 5) - dollars
		score2 = dollars - (spread2 + 5) if buy2 else (spread2 - 5) - dollars
		score3 = abs(spread3 - dollars) - 5  # end always take most profitable
		return score1 + score2 + score3
	elif plays % 2 == 0:  # maker play todo: reduce strategy space
		# prev = history[-1]
		# round = plays // 2 + 1
		# print(history, round, change)
		# change = 100 / (2**round) * (1 if prev else -1)
		# return cfr((*history, history[-2]+change), dollars, not main_player)

		node_util = 0
		util = np.zeros(10)
		if history in information: node = information[history]
		else: node = information[history] = Node(10)
		strategy = node.get_strategy()
		options = range(5, 100, 10)
		if main_player:
			for index in range(10):
				new_history = (*history, options[index])
				value = cfr(new_history, dollars, not main_player)
				util[index] = value
				node_util += strategy[index] * value
			node.regret_sum += -util + node_util
			# node.util += node_util
			# node.calls += 1
			return node_util
		else:
			node.strategy_sum += strategy
			# print(len(options), len(strategy))
			choice = np.random.choice(options, p=strategy)
			new_history = (*history, choice)
			return cfr(new_history, dollars, not main_player)
	else: # taker play
		node_util = 0
		util = np.zeros(2)
		if (history, dollars) in information: node = information[(history, dollars)]
		else: information[(history, dollars)] = node = Node(2)
		# print(history, dollars, p1, p2)
		strategy = node.get_strategy()
		options = (False, True)
		if main_player:
			for index in range(2):  # 2 options
				new_history = (*history, options[index])
				value = cfr(new_history, dollars, not main_player)
				util[index] = value
				node_util += value * strategy[index]
			node.regret_sum += util - node_util
			# node.util += node_util
			# node.calls += 1
			return node_util
		else:
			node.strategy_sum += strategy
			choice = np.random.choice(options, p=strategy)
			new_history = (*history, choice)
			return cfr(new_history, dollars, not main_player)


if __name__ == "__main__":
	total = 0
	for i in range(iterations):
		dollars = np.random.randint(0, 10) * 10
		val = cfr((50,), dollars, i%2==0)
		# print(val)
		total += val
	print(total / iterations)
	for his in information:
		print(his, information[his].get_average_strategy())#, information[his].util/information[his].calls)
	print(len(information))
	for d in range(0, 100, 10):
		print(d, information[((50,), d)].get_average_strategy())