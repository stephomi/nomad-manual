# ![](/icons/image.webp) 배경

이 메뉴에서는 Nomad의 배경색과 사용할 참조 이미지를 설정할 수 있습니다.

![](/images/background_overview.webp)

## Background 
![](/images/background_selector.webp)

뷰포트 배경에는 세 가지 옵션이 있습니다.

* `Environment` - [Shading](shading)에서 선택한 환경 맵을 표시합니다. Blur와 Exposure(밝기) 컨트롤로 추가 조정할 수 있습니다. 
* `Color` - 사용자가 선택하는 단색 배경
* `Gradient` - 위에서 아래로 이어지는 색상 그라디언트입니다. Factor 슬라이더로 그라디언트의 중간 지점을 조절할 수 있습니다.  

## Reference Image

![](/images/background_reference.webp)

배경에 원하는 이미지를 추가하여 참조용으로 사용할 수 있습니다.
예를 들어 화면 구석으로 옮기고 싶다면, 위치와 크기를 변경할 수 있습니다.

### ![](/icons/tool_transform.webp) Transform 

이 버튼을 사용하면 참조 이미지를 인터랙티브하게 배치할 수 있습니다. 두 손가락으로 참조 이미지를 이동, 확대/축소, 회전하여 원하는 위치에 둘 수 있습니다. 최종 배치는 아래 슬라이더에 반영됩니다:

* `Overlay` - 0%에서는 참조 이미지가 항상 오브젝트 뒤에, 100%에서는 앞에 표시됩니다. 
* `Opacity` - 이미지의 투명도입니다.
* `Position` - 이미지의 X, Y 위치입니다.
* `Rotation` - 이미지 회전입니다.
* `Scale` - 이미지 크기입니다.


::: tip

카메라와 참조 이미지는 서로 연결되어 있습니다. 

즉, 조형물에 맞춰 참조 이미지를 정렬해 둔 상태에서 [Camera 메뉴](camera)에서 카메라를 생성하면, 참조 이미지의 위치, 회전, 크기 정보도 함께 카메라에 저장됩니다. 참조 이미지를 끄고 다른 뷰포트로 회전해도, 다시 해당 카메라를 통해 보면 참조 이미지가 이전에 사용한 설정과 함께 활성화됩니다.

심지어 카메라마다 서로 다른 이미지를 선택하는 것도 가능합니다!

 ![](/videos/reference_camera.mp4)

:::
