import networkx as nx
import matplotlib.pyplot as plt
import re

def read_graph_from_file(filename: str) -> nx.Graph:
    """
    주어진 파일을 읽어들여 그래프를 구성하여 반환합니다.
    공백이나 쉼표 등의 불필요한 기호를 제거한 뒤 숫자들을 처리합니다.
    """
    G = nx.Graph()
    vertices = set()  # 입력 파일에서 등장하는 정점 집합
    edges = set()  # 중복 간선을 방지하기 위한 집합

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # 숫자와 공백만 남기고 다른 기호 제거
            cleaned_line = re.sub(r'[^\d\s]', '', line)
            # 공백을 기준으로 분리
            parts = cleaned_line.split()

            # 비어 있는 줄은 무시
            if not parts:
                continue

            # 첫 번째 숫자를 현재 정점으로 설정
            current_vertex = int(parts[0])
            vertices.add(current_vertex)

            # 그 뒤의 숫자들을 연결된 정점으로 처리
            for neighbor_str in parts[1:]:
                try:
                    neighbor = int(neighbor_str)
                    vertices.add(neighbor)

                    # 자기 자신(자기 루프)은 무시
                    if neighbor != current_vertex:
                        # 간선은 집합으로 중복 여부를 확인
                        edge = tuple(sorted((current_vertex, neighbor)))  # (작은 값, 큰 값) 형태로 저장
                        if edge not in edges:
                            edges.add(edge)
                            G.add_edge(current_vertex, neighbor)
                except ValueError:
                    # 숫자로 변환할 수 없는 경우 무시
                    continue

    # 명시적으로 모든 정점을 추가 (간선에서 생성되지 않은 경우 포함)
    G.add_nodes_from(vertices)
    return G

def main():
    # input.txt로부터 그래프를 생성
    graph = read_graph_from_file("cinput.txt")

    # 평면 그래프인지 확인
    is_planar, planar_embedding = nx.check_planarity(graph)
    if not is_planar:
        print("The graph is not planar. The output may have crossing edges.")
        pos = nx.spring_layout(graph, k=2)  # 일반적인 레이아웃
    else:
        print("The graph is planar. Using planar_layout for visualization.")
        pos = nx.planar_layout(graph)  # 평면 그래프를 위한 레이아웃

    # 그래프 크기 설정
    plt.figure(figsize=(10, 10))  # 출력 그래프 크기 조정

    # 사용자 입력에 따른 정점 레이블 설정
    labels = {node: str(node) for node in graph.nodes}

    # 그래프를 그립니다.
    nx.draw(
        graph, pos, 
        labels=labels,              # 사용자 정의 정점 레이블 반영
        with_labels=True,           # 레이블 표시 활성화
        node_color='lightblue',     # 정점 색상
        edge_color='gray',          # 간선 색상
        node_size=2000,             # 정점 크기 증가
        font_size=15                # 레이블 폰트 크기 증가
    )

    # 그래프를 PNG로 저장
    output_filename = "graph.png"
    plt.savefig(output_filename, format='png', dpi=300)
    print(f"Graph has been saved to {output_filename}")

if __name__ == "__main__":
    main()
