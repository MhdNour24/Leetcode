class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        enb=0
        for i in range(len(accounts)):
            sum_liste=sum(accounts[i])
            if sum_liste>enb:
                enb=sum_liste
        return enb