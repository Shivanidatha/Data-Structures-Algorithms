class TimeMap:

    def __init__(self):
        self.hm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append((timestamp,value))
        else:
            self.hm[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if self.hm.get(key) is None:
            return ""
        list1=self.hm[key]
        l=0
        r=len(list1)-1
        while l<=r:
            mid=(l+r)//2
            if timestamp==list1[mid][0]:
                return list1[mid][1]
            elif timestamp<list1[mid][0]:
                r=mid-1
            else:
                l=mid+1
        return list1[r][1] if r!=-1 else ""
