from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        
        indexed_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])
        res = [0] * len(queries)

        left = 0
        right = 0
        server_count = defaultdict(int)
        active_servers = set()

        for q, idx in indexed_queries:
            start = q - x

            # 오른쪽 포인터 확장
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                server_count[server] += 1
                active_servers.add(server)
                right += 1
            
            # 왼쪽 포인터 축소
            while left < len(logs) and logs[left][1] < start:
                server = logs[left][0]
                server_count[server] -= 1
                if server_count[server] == 0:
                    active_servers.remove(server)
                left += 1
            
            # 응답 없는 서버 수
            res[idx] = n - len(active_servers)
        
        return res
