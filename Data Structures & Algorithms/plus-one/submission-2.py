class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 0
        digits[i] += 1

        while i >= 0:
            actual_sum = digits[i] + carry
            if actual_sum >= 10:
                digits[i] = (actual_sum) % 10
                carry = (actual_sum) // 10
            else:
                digits[i] = actual_sum
                carry = 0
            i -= 1
            
        
        # if carry != 0:
        #     new_arr = [0] * (len(digits) + 1)
        #     i = len(digits) - 1

        #     while i > 0:
        #         new_arr[i + 1] = digits[i]
        #         i -= 1
            
        #     new_arr[0] = carry
        #     digits = new_arr

        if carry != 0:
            digits.append(digits[len(digits) - 1])
            i = len(digits) - 1

            while i > 0:
                digits[i] = digits[i - 1]
                i -= 1
            digits[0] = carry

        
        return digits
            

        
            
        