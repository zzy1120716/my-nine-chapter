class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        results = []
        
        if numbers is None or len(numbers) < 3:
            return results
        
        numbers.sort()
        n = len(numbers)
        
        for i in range(n - 2):
            # skip duplicate triples with the same first number
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            target = -numbers[i]
            
            self.twoSum(numbers, i, target, results)
            
        return results
        
    def twoSum(self, numbers, start, target, results):
        left, right = start + 1, len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                results.append((numbers[start], numbers[left], numbers[right]))
                left += 1
                right -= 1
                # skip duplicate pairs with the same left
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                # skip duplicate pairs with the same right
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1