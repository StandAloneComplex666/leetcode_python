class Solution(object):
    def real_imag(self, com):
        real = int(com.split('+')[0])
        imag = int(com.split('+')[1][:-1])
        return real, imag
    
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """   
        real_a ,imag_a = self.real_imag(a)
        real_b ,imag_b = self.real_imag(b)
        real_res = real_a*real_b - imag_a*imag_b
        imag_res = real_a*imag_b + real_b*imag_a
        res = ''.join([str(real_res),'+',str(imag_res)+'i'])
        print(res)
        return res