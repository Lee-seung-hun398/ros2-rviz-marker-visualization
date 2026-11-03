# ROS 2 RViz Marker Visualization

오토모티브SW프로그래밍 9주차 실습 프로젝트입니다.

ROS 2의 `visualization_msgs/MarkerArray`를 이용하여 RViz2에서 사용자 정의 마커를 시각화합니다.

## 구현 내용

- 녹색 경로(Line Strip) 표시
- 빨간색 장애물(Cube) 표시
- 장애물 경고 텍스트 표시
- MarkerArray 토픽 발행
- RViz2 설정 파일 저장
- Launch 파일을 이용한 Marker Publisher와 RViz2 통합 실행

## 패키지

```text
my_viz_pkg
├── config
│   └── integrated_view.rviz
├── launch
│   └── rviz_advanced.launch.py
├── my_viz_pkg
│   ├── __init__.py
│   └── custom_marker_publisher.py
├── package.xml
├── setup.cfg
├── setup.py
└── README.md
```

## 빌드

```bash
cd ~/ros2_ws
colcon build --symlink-install --packages-select my_viz_pkg
source ~/ros2_ws/install/setup.bash
```

## 실행

WSL 환경에서 RViz2를 실행하기 위해 X11 호환 모드를 사용합니다.

```bash
QT_QPA_PLATFORM=xcb ros2 launch my_viz_pkg rviz_advanced.launch.py
```

실행하면 Custom Marker Publisher와 RViz2가 동시에 실행됩니다.

## 실행 결과

RViz2에서 다음 요소를 확인할 수 있습니다.

- 녹색 주행 경로
- 빨간색 장애물
- `WARNING: OBSTACLE [3.0m]` 경고 텍스트

Fixed Frame은 `base_link`를 사용합니다.

### 실행 화면

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a147c109-b06c-49f3-9f8a-b0350797f3b3" />

