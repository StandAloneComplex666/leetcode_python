# my wrong answer, whose error is 'List index out of range'
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #tempChar = ''
        tempSum = 1
        res = 0
        if len(chars) == 1:
            return 2
        for i in range(1,len(chars)):
            #print(chars[i])
            #print(chars[i] == chars[i-1])
            if chars[i] == chars[i-1]:
                tempSum += 1
            else:
                res += len(str(tempSum)) + 1
                tempChar = chars[i]
                tempSum += 1
            #print(res)
        res += len(str(tempSum)) + 1
        #print('Final Res: ',res)
        return res

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #tempChar = ''
        tempSum = 1
        res = 0
        # tempList = ["a","b","c"]
        # print (len(tempList))
        if len(chars) == 1:
            return 2
        for i in range(1,len(chars)):
            print(i)
            print(chars[i])
            #print(chars[i] == chars[i-1])
            if chars[i] == chars[i-1]:
                tempSum += 1
            else:
                res += len(str(tempSum)) + 1
                #tempChar = chars[i]
                tempSum = 1
            #print(res)
        res += len(str(tempSum)) + 1
        #print('Final Res: ',res)
        return res


# a correct answer:
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return len(chars)
        count = 1  
        k = 0 
        for i in range(len(chars) - 1):
            if chars[i] == chars[i+1]:
                count += 1
            else:
                new_length = 1 if count == 1 else (1+len(str(count)))
                new_str = chars[i] if count == 1 else (chars[i]+str(count))
                count = 1
                chars[k:k+new_length] = new_str
                k = k+new_length
        new_length = 1 if count == 1 else (1+len(str(count)))
        new_str = chars[i+1] if count == 1 else (chars[i+1]+str(count))
        chars[k:k+new_length] = new_str
        k = k+new_length
        del chars[k:len(chars)]
        return len(chars)