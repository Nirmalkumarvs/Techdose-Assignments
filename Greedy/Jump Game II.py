class Solution:
    def jump(self, nums: List[int]) -> int:
        last_index = len(nums) - 1 
        
        max_reachable = [start_pos + nums[start_pos] for start_pos in range(last_index)] 
        jump_range = (0, 0)
        n_jumps = 0
        while jump_range[1] < last_index:
            n_jumps += 1 
            
            jump_range = (jump_range[1]+1, max(max_reachable[jump_range[0]:jump_range[1]+1]))
        return n_jumps
