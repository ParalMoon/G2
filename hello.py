import dash
from dash import html
import dash_cytoscape as cyto

# 애플리케이션 생성
app = dash.Dash(__name__)

# 그래프 데이터
nodes = [
    {"data": {"id": "1", "label": "Node 1"}, "position": {"x": 100, "y": 100}},
    {"data": {"id": "2", "label": "Node 2"}, "position": {"x": 200, "y": 200}},
    {"data": {"id": "3", "label": "Node 3"}, "position": {"x": 300, "y": 100}},
]

edges = [
    {"data": {"source": "1", "target": "2"}},
    {"data": {"source": "2", "target": "3"}},
    {"data": {"source": "1", "target": "3"}},
]

# Cytoscape 그래프 구성
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=nodes + edges,
        layout={'name': 'preset'},  # 노드의 초기 위치를 유지
        style={'width': '100%', 'height': '400px'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'background-color': '#0074D9',
                    'color': 'white',
                    'text-halign': 'center',
                    'text-valign': 'center',
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': '#B10DC9',
                    'target-arrow-color': '#B10DC9',
                    'target-arrow-shape': 'triangle',
                }
            }
        ],
        userZoomingEnabled=True,  # 사용자가 줌 가능
        pannable=True,            # 그래프를 드래그로 이동 가능
        autoResize=True,          # 창 크기에 맞게 조정
        draggable=True            # 노드를 드래그 가능
    )
])

# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)
