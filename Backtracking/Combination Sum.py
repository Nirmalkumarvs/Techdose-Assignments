class Solution(object):
	def combinationSum(self, candidates, target):
		result = []
		
		def dfs(index, target, arr):
			if target == 0:
				result.append(arr)
				return 
			
			if target <0 :
				return
			
			for i in range(index, len(candidates)):
				dfs(i, target-candidates[i], arr + [candidates[i]])
				
				
		dfs(0, target, [])
		return result
