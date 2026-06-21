# ROS2 ESP-32 자율 주행 프로젝트

ROS2, Nav2, SLAM Toolbox, ESP32를 활용하여 제작한 실내 자율주행 로봇 프로젝트입니다.

## Features

- URDF 기반 로봇 모델링
- LiDAR 데이터 수신 및 ROS2 토픽 연동
- SLAM Toolbox를 이용한 맵 생성
- Nav2를 이용한 경로 계획 및 자율 주행
- Waypoint 기반 순찰 기능 구현
- Explore Lite를 이용한 자동 맵 탐사
- RViz2를 통한 센서 및 경로 시각화
  
## System Architecture

ESP32 기반 로봇이 LiDAR 데이터를 ROS2로 전송하며,
SLAM을 통해 지도를 생성.
생성된 맵을 기반으로 Nav2가 경로를 계획하고
목표 지점까지 자율 주행을 수행.
사전에 기록해 놓은 waypoint patrol도 가능.

## Tech Stack

- ROS2 Iron
- Nav2
- SLAM Toolbox
- Explore Lite
- RViz2
- URDF
- Python
- ESP32
- LiDAR

## Patrol

https://github.com/user-attachments/assets/ef422328-2e9d-43cf-b42f-a8a5032f7f9c

## explore

https://github.com/user-attachments/assets/068469ab-a465-4720-a76f-d37a73bd5c28

## SLAM

https://github.com/user-attachments/assets/54cdfa0d-e340-4d6d-af21-706e7d7a7a62

## nav2

https://github.com/user-attachments/assets/2a7586c1-0934-4072-8e20-ffbf7c85d573

