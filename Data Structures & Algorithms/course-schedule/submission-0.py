from typing import List
from collections import deque

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> bool:
        # unlocks[p] lists the courses you can work toward after taking p.
        unlocks = [[] for _ in range(numCourses)]

        # indegree[c] counts how many prerequisites course c still needs.
        indegree = [0] * numCourses

        # A pair [course, prerequisite] means prerequisite -> course.
        for course, prerequisite in prerequisites:
            unlocks[prerequisite].append(course)
            indegree[course] += 1

        # Start with every course that needs no prerequisites.
        queue = deque(
            course
            for course in range(numCourses)
            if indegree[course] == 0
        )

        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in unlocks[course]:
                # Taking this course satisfies one prerequisite.
                indegree[next_course] -= 1

                # Only enqueue it when ALL its prerequisites are satisfied.
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If some courses couldn't be completed, a cycle blocked them.
        return completed == numCourses