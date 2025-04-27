def solution(info, edges):
    adj = [[] for _ in range(len(info))]  # 인접 리스트 만들기
    for parent, child in edges:
        adj[parent].append(child)

    # dfs 함수에서 max_sheep을 인자로 전달하고 값을 갱신
    def dfs(current, sheep, wolf, next_nodes, max_sheep):
        print(current)
        if info[current] == 0:  # 현재 노드가 양이면
            sheep += 1
        else:  # 늑대면
            wolf += 1
        
        if wolf >= sheep:
            return max_sheep  # 늑대가 같거나 많으면 종료
        
        max_sheep = max(max_sheep, sheep)  # 최대 양 마리 수 갱신

        # 다음 탐색할 후보 노드들
        next_nodes += adj[current]

        for next_node in next_nodes:
            new_next_nodes = next_nodes.copy()
            new_next_nodes.remove(next_node)
            max_sheep = dfs(next_node, sheep, wolf, new_next_nodes, max_sheep)

        return max_sheep

    # dfs를 시작하고 max_sheep 값을 반환받음
    max_sheep = dfs(0, 0, 0, [], 0)

    return max_sheep
solution(info, edges)