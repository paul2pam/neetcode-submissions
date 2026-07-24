class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        children = {i:[] for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}
        for prereq in prerequisites:
            children[prereq[1]].append(prereq[0])
            in_degree[prereq[0]] += 1
        
        q = deque()
        for course, degree in in_degree.items():
            if degree == 0:
                q.append(course)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for child in children[course]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)


        if len(res) == numCourses:
            return res
        else:
            return []