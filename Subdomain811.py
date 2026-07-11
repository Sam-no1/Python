class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = []
        store = {}
        for val in cpdomains:
            domain = val.split(" ")
            count = domain[0]
            d = domain[1].split(".")
            print(count)
            for i in range(len(d)):
                do = ".".join(d[i:len(d)])
                if do in store:
                    store[do] += int(count)
                else:
                    store[do] = int(count)
        for key, val in store.items():
            res.append(str(val) + " "+ key)
        return res