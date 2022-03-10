class solution:
    def minimumSemesters(N,relations):
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for relation in relations:
            prereq = relation[0]
            courses = relation[1]
            graph[preqreq].append(course)
            in_degree[course] += 1
        queue = deque([i for i in range(1,N+1) if i not in in_degree])
        ans = 0
        courses_took = 0
        while queue:
            ans += 1
            for i in range(len(queue)):
                vertex = queue.popleft()
                courses_took += 1
                for nei in graph[vertex]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        queue.append(nei)
        return ans if courses_took == n else -1
    
