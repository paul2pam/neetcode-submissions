class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        for prereq in prerequisites:
            if prereq[0] not in m:
                m[prereq[0]] = []
            m[prereq[0]].append(prereq[1])


        visited = set()
        cycle = set()
        def dfs(course):
            if course in visited or course not in m:
                return True
            if course in cycle:
                print(f"{course} in {cycle}")
                return False
            cycle.add(course)
            for prereq in m[course]:
                if not dfs(prereq):
                    print(f"dfs({prereq}) returned false")
                    return False
            cycle.remove(course)
            visited.add(course)
            return True
        print(m.items())
        for k, v in m.items():
            visited.clear()
            if not dfs(k):
                print(f"not dfs({k})")
                return False
        return True