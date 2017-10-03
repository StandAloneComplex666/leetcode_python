class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda (h, k): (-h, k))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue

def reconstructQueue(people):

    people = sorted(people, key=lambda x: x[1])
    people = sorted(people, key=lambda x: -x[0])
    res = []
    for p in people:
        res.insert(p[1], p)
    return res
a = [[5,0],[7,0], [4,4], [7,1],[6,1], [5,2]]
res =reconstructQueue(a)
print(a)
print(res)