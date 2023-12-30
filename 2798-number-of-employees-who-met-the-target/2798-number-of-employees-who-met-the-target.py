class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort(reverse=True)
        filtered_employees=list(filter(lambda houre:houre>=target,hours))
        return len(filtered_employees)