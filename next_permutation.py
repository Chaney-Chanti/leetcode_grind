class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # What the next lexicography greater pemutation means is that the order of permutations is in ascending order.
        # [1, 2, 3]
        # [1, 3, 2]
        # [2, 1, 3]
        # [2, 3, 1]
        # [3, 1, 2]
        # [3, 2, 1]

        # it seems that the brute force solution would be to calculate every permutation then find the minimum thats greater than the number passed in
        # That would be O(n!)... oof 

        # hint: Notice that just before a "jump" (e.g. [1,3,2] → [2,1,3]), the suffix from the pivot rightward is in descending order. That's the core observation. The pivot is the number that needs to change in order to get the next perm

        # Compare 3 and 2 → 3 > 2, not a dip, keep going
        # Compare 1 and 3 → 1 < 3, found a dip! ← pivot is index 0 (value 1)
        # The suffix [3, 2] is in descending order — and that's exactly why 1 is the pivot. You couldn't make a larger permutation by only rearranging [3, 2] since it's already in its largest possible order. So you have to touch the 1 to get the next permutation.

        # https://www.youtube.com/watch?v=quAS1iydq7U
        # Video does a good job explaining how permutations are built. In the first slot you are given a descision space of 1, 2, 3. In the second digit, you have a descision space of 2 numbers (- whatever number you descided to put in the first slot).

        # a strictly descending pattern has completley exhuasted itself.

        # First find pivot point
        # Swap the pibot and the next number in line (The min number greater than the pivot)
        # reverse the order of the suffix
        pivot = -1
        # find the pivot
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        print("nums before: ", nums)
        # find the swap target (min number to the right of pivot that's also greater than the pivot)]
        if pivot != -1:
            for j in range(len(nums) -1, pivot, -1):
                if nums[j] > nums[pivot]:
                    # swap
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break

        print("chaney debug nums after (swapped): ", nums)
        # make the suffix in ascending order, use two pointers because we know the data is already descending
        # Using a sorting algo would be slower, and you should only use a sorting algo if we know nothing about
        # the data.
        left, right = pivot + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
        
