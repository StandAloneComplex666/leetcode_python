class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        statDomain = {}
        res = []
        for pair in cpdomains:
            freq, compDomain = int(pair.split(' ')[0]), pair.split(' ')[1]
            domainParts = compDomain.split('.')
            for i in range(len(domainParts)):
                tempStr = '.'.join(domainParts[i::])
                if tempStr in statDomain:
                    statDomain[tempStr] += freq
                else:
                    statDomain[tempStr] = freq
        for key, value in statDomain.items():
            tempRes = str(value) + ' ' + key
            res.append(tempRes)
        return res