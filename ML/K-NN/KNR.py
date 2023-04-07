
"""
class sklearn.neighbors.KNeighborsRegressor(n_neighbors=5, *, weights='uniform', algorithm='auto', leaf_size=30, p=2,
metric='minkowski', vmetric_params=None, n_jobs=None)

# n_neighbors : int
이웃의 수인 K를 결정한다. default는 5

# weights : {'uniform', 'distance'} or callable
예측에 사용되는 가중 방법을 결정한다. default는 uniform

'uniform' : 각각의 이웃이 모두 동일한 가중치를 갖는다. 
'distance' : 거리가 가까울수록 더 높은 가중치를 가져 더 큰 영향을 미치게 된다.
callable : 사용자가 직접 정의한 함수를 사용할 수도 있다. 거리가 저장된 배열을 입력으로 받고 가중치가 저장된 배열을 반환하는 함수가 되어야 한다. 

# algorithm : {'auto', 'ball_tree', 'kd_tree', 'brute'}
가장 가까운 이웃들을 계산하는 데 사용하는 알고리즘을 결정한다. default는 auto.

'auto' : 입력된 훈련 데이터에 기반하여 가장 적절한 알고리즘을 사용한다.
'ball_tree' : Ball-Tree 구조를 사용한다. (Ball-Tree 설명 : https://nobilitycat.tistory.com/entry/ball-tree)
'kd_tree' : KD-Tree 구조를 사용한다.
'brute' : Brute-Force 탐색을 사용한다.

# leaf_size : int
Ball-Tree나 KD-Tree의 leaf size를 결정한다. default값은 30이다.
이는 트리를 저장하기 위한 메모리뿐만 아니라, 트리의 구성과 쿼리 처리의 속도에도 영향을 미친다.

# p : int
민코프스키 미터법(Minkowski)의 차수를 결정한다.
예를 들어 p = 1이면 맨해튼 거리(Manhatten distance), p = 2이면 유클리드 거리(Euclidean distance)이다.
"""