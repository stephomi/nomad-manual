# ![](/icons/interface.webp) 인터페이스 메뉴 

이 메뉴에서는 Nomad의 인터페이스를 사용자 정의하기 위한 다양한 옵션을 제어합니다. 

![](/images/interface_overview2.webp)

Nomad는 상당히 깊은 수준까지 커스터마이즈할 수 있으며, 이 메뉴는 Interface, Gesture, Bindings, Debug 네 개의 섹션으로 나뉩니다.

![](/images/interface_menu.webp)


::: tip
이 페이지는 인터페이스 “메뉴”에 대한 것이며, 인터페이스 자체에 대한 것이 아닙니다! 전체 인터페이스는 [Getting Started](gettingstarted.md)에서 설명합니다.
:::

## Interface 

Interface 섹션에서는 단축키를 추가하고, 떠 있는 툴바를 만들고, Nomad 사용자 인터페이스의 색상, 크기, 외형을 제어할 수 있습니다.

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

하단 툴바에는 기본적으로 다음 단축키가 활성화되어 있습니다:
* `Undo` - 이전 작업을 되돌립니다.
* `Redo` - 직전에 되돌린 작업을 다시 복원합니다.
* `Solo` - 선택된 오브젝트만 보이도록 나머지 모든 오브젝트를 일시적으로 숨깁니다. 다시 누르면 모든 오브젝트가 복원됩니다.
* `X-ray` - 선택된 오브젝트만 불투명하게 두고, 나머지 모든 오브젝트를 반투명하게 만듭니다. 다시 누르면 기본 머티리얼로 돌아갑니다.
* `Voxel remesh` - 마지막으로 사용한 보xel 해상도를 사용해 현재 오브젝트를 리메시합니다. 길게 누르거나 위로 스와이프하면 해상도 슬라이더와 샤프 엣지 토글이 나타납니다.
* `Grid` - 뷰 그리드를 토글합니다. 길게 누르거나 위로 스와이프하면 그리드의 색상과 불투명도를 변경할 수 있습니다.
* `Wireframe` - 와이어프레임 오버레이를 토글합니다. 길게 누르거나 위로 스와이프하면 와이어프레임의 색상과 불투명도를 변경할 수 있습니다.
* `Inspector` - Nomad 배경 위에 uv, 베이크된 텍스처, 기타 속성 등 메시의 속성을 표시합니다.
* `Face Group` - 페이스 그룹 오버레이를 토글합니다. 자세한 내용은 [Tools->FaceGroup](tools.md#facegroup) 참고. 

이 메뉴에서 자주 사용하는 다른 단축키도 사용할 수 있으며, 더 많은 기능은 Bindings 버튼 안에서 찾을 수 있습니다.

#### ![](/icons/more.webp) Bindings

Nomad의 거의 모든 기능은 Bindings 버튼을 통해 단축키 툴바에 추가할 수 있습니다. 버튼을 클릭하면 바인딩 메뉴가 표시됩니다:

![](/images/interface_bindings_search.webp)

상단의 아이콘으로 카테고리별 검색을 하거나, 검색 필드에서 이름으로 기능을 찾을 수 있습니다. 기능을 클릭하면 툴바에 추가됩니다. 다시 클릭하면 제거됩니다.

#### ![](/icons/list.webp) Order

단축키 목록을 표시합니다. 길게 누른 후 드래그하여 단축키의 순서를 변경할 수 있습니다.

#### ![](/icons/reset.webp) Reset

Reset은 하단 툴바를 기본 설정으로 되돌립니다.

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

+를 클릭하면 떠 있는 툴바가 추가됩니다. Bindings 버튼을 눌러 단축키를 추가하기 전까지는 보이지 않습니다. 단축키를 추가한 후에 표시 여부를 설정할 수 있습니다. 

툴바는 여러 개 만들 수 있으며, 각 툴바는 이 메뉴에서 다음 옵션을 가집니다:

* ![](/icons/checked.webp) `Visible` - 툴바의 표시 여부를 토글합니다.
* ![](/icons/more.webp)`Bindings` - 툴바에 추가/제거할 기능을 선택하는 바인딩 창을 표시합니다.
* ![](/icons/list.webp)`Order` - 툴바의 순서를 재정렬하는 메뉴를 표시합니다.
* ![](/icons/reset.webp) `Reset` - 툴바를 기본 상태로 초기화합니다.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - 툴바 오른쪽 아래 모서리에 리사이즈 핸들을 토글합니다.
* ![](/icons/sort_down.webp) `Collapsable` - 오른쪽 위에 접기 핸들을 토글합니다.
* ![](/icons/trash.webp) `Delete` - 툴바를 삭제합니다.

### Toolbox

Nomad 인터페이스 오른쪽에 있는 툴 메뉴에 대한 옵션입니다.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

툴바 하단 모서리에 리사이즈 핸들을 토글합니다.

#### Hidden
일반적으로 상단 바의 Toolbox 아이콘은 긴 단일 열과 다중 열 툴 목록 사이를 토글합니다. 이 옵션을 사용하면 다중 열 목록과 완전 숨김 사이를 토글합니다.

#### Colored
카테고리별로 아이콘에 색상을 부여합니다. 예: 모든 마스크 도구는 갈색, 분할 도구는 빨간색, 평탄화 도구는 녹색 등.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
툴박스의 기본 도구 순서를 초기화합니다. 사용자 정의 아이콘은 목록 끝에 그대로 남습니다.


### Presets

![](/images/interface_presets.webp)

인터페이스용 색상 프리셋 모음입니다.

#### High-contrast button
활성화된 버튼이 더 잘 보이도록 하는 대체 스타일입니다. Auto로 설정하면, 활성/비활성 UI 색상 대비가 낮을 때 Nomad가 이 모드를 사용합니다.

#### Color widget/Color base
인터페이스에서 사용되는 기본 색상입니다.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
활성화하면 Nomad에서 메뉴와 패널의 외형을 제어하는 추가 옵션이 나타납니다. 색상, 투명도, 블러 양을 조절할 수 있습니다.

::: tip
작은 기기에서는 색상 패널을 거의 흰색, 투명, 낮은 블러 강도로 설정하면 메뉴가 씬을 가리지 않게 할 수 있습니다.
:::

----

### Mirror top bar
상단 바의 메뉴 순서를 반전합니다.

### Mirror side bars
사이드 바를 서로 바꿔서 툴박스를 왼쪽, 툴 옵션을 오른쪽에 배치합니다.

### Mirror bottom bar
하단 바를 오른쪽 아래 모서리로 옮기고 버튼 순서를 반전합니다.

### Material color preview
머티리얼 색상을 선택할 때, 현재 선택된 오브젝트에 이 머티리얼의 미리보기가 표시됩니다.

----
### Help popup on hover

호버를 지원하는 기기에서, Nomad의 ![](/icons/help.webp) 아이콘으로 표시되는 컨텍스트 도움말을 호버 시 표시할지, 클릭 시에만 표시할지 설정합니다.

----

### Overall scale
모든 UI 요소에 적용되는 크기 배율입니다.
### Panel width
메뉴와 패널의 너비입니다.
### Font scale
폰트 크기 배율입니다.
### Vertical spacing
메뉴와 패널 내 요소 간의 세로 간격입니다.
### Vertical spacing (left)
왼쪽 툴바 내 요소 간의 세로 간격입니다.

----

### Edge offset
화면 가장자리의 버튼과 상호작용하는 데 문제가 있을 때만 이 값을 변경해야 합니다. 슬라이더가 비활성화되어 있으면, Nomad는 기기에서 제공하는 안전 영역(safe area) 값을 사용합니다.

::: tip
Nomad를 새 기기로 옮길 때(예: iPhone 12에서 iPhone 15로 교체), Edge 옵션을 반드시 기본값으로 리셋하세요!
:::

### Reset style
모든 UI 요소를 기본값으로 초기화합니다.


## Gesture
Gesture 메뉴는 스타일러스와 손가락 입력이 Nomad를 어떻게 제어하는지 설정합니다.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad는 입력 장치에 따라 동작을 제한할 수 있습니다. 예를 들어 손가락 드래그는 카메라 이동만, 스타일러스 드래그는 조각만 수행하도록 설정할 수 있습니다. 마우스나 트랙패드가 있다면, 그것도 특정 동작을 제어하도록 할당할 수 있습니다.

Nomad는 현재 다음 모드를 손가락, 스타일러스, 마우스 제스처의 임의 조합으로 설정할 수 있습니다:

* Camera
* Sculpt
* Gizmo
* Material picking (롱 프레스)
* Select object


`Finger always smooths` - 손가락 드래그로만 Smooth가 작동하도록 설정할 수 있습니다.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Mask 버튼을 누르고 있지 않아도 다음 단일 탭 단축키를 활성화합니다. 다음 제스처가 가능해집니다:
* 배경을 탭하여 마스크 반전
* 마스크된 영역을 탭하여 마스크 블러
* 마스크되지 않은 영역을 탭하여 마스크 샤픈

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - 길게 누르면 Mask와 SelMask 사이를 전환하고 새 스트로크를 시작합니다. 스트로크가 끝나면 이전 도구가 다시 선택됩니다. 
* `Tool` - 움직이지 않고 길게 누른 후 떼면 Mask와 SelMask 사이를 전환합니다. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts`를 활성화하면 Hide 도구에서 다음 단축키를 사용할 수 있습니다:
* 페이스 그룹을 탭하여 해당 그룹 숨기기
* 빈 공간을 탭하여 숨겨진 폴리곤 반전

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

기기가 3손가락 제스처를 지원하는 경우, 이 제스처에 대한 단축키를 설정할 수 있습니다. 

옵션 매트릭스를 사용하면 수직 드래그와 수평 드래그를 서로 다른 단축키로 정의할 수 있습니다. 동일한 제스처가 두 옵션에 선택되면, 하나는 비활성화됩니다.

* `Rotate lighting` - 환경, 조명, Matcap을 회전합니다.
* `Tool Radius` - 도구 반경을 조절합니다.
* `Tool Intensity` - 도구 강도를 조절합니다. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - 활성화하면 다음 제스처가 동작합니다:
* Undo - 두 손가락 탭
* Redo - 세 손가락 탭

`Long press` - 활성화하면, 두/세 손가락을 누르고 있으면 빠르게 Undo/Redo가 반복됩니다.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window`는 드래그, 핀치, 롤, 카메라 동작을 제어하는 떠 있는 툴바를 표시합니다.

### Camera
`Camera` 메뉴로 이동하는 바로가기입니다(카메라 옵션은 원래 여기 있었으나, 카메라 메뉴로 이동되었습니다).

### Pencil double tap -> Bindings 

`Bindings` 메뉴로 이동하는 바로가기입니다(Apple Pencil 탭 및 더블 탭 옵션은 원래 여기 있었으나, Bindings 메뉴로 이동되었습니다).


## Bindings
키보드 및 버튼 단축키는 Bindings 메뉴에서 정의할 수 있습니다:

![](/images/interface_bindings.webp)
기기에 키보드가 있다면 Nomad의 거의 모든 기능을 키보드 단축키에 바인딩할 수 있으며, 스타일러스의 추가 버튼이나 게임패드 컨트롤러에도 바인딩할 수 있습니다.

바인딩을 만들려면, 기능 옆의 사각형을 클릭하고 키/버튼을 누르세요. 

상단의 카테고리 아이콘으로 기능을 찾거나, 검색창에서 이름으로 검색할 수 있습니다. 

각 바인딩은 이름 옆의 체크박스로 개별적으로 비활성화할 수 있습니다.

### ![](/icons/more.webp) Context menu
각 바인딩 뒤의 ![](/icons/more.webp) 아이콘은 컨텍스트 메뉴를 표시합니다:

![](/images/interface_bindings_context.webp)

* `Clone` - 바인딩 복제
* `Reset` - 바인딩 초기화
* `Delete` - 바인딩 삭제
* `Toggle shortcut on key tap` - 탭과 롱 프레스를 다르게 처리할지 설정합니다. 활성화하면, 탭은 도구를 활성화합니다. 롱 프레스는 키를 누르고 있는 동안에만 도구를 활성화하고, 키를 떼면 이전 도구로 돌아갑니다. 다른 3D 앱에서 흔히 ‘sticky keys’라고 부르는 동작입니다.

### Advanced
Bindings 메뉴 하단에는 고급 옵션용 톱니바퀴 메뉴가 있습니다:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Mask, Smooth, Gizmo, Hide, Sub 등의 표준 단축키를 탭하면 해당 모드로 토글되지만, 키를 누르고 있으면 그 모드로 전환되었다가 키를 떼면 이전 모드로 돌아갑니다. 다른 3D 앱에서 흔히 ‘sticky keys’라고 부르는 동작입니다.
* `Toggle tool shortcuts` - 도구 단축키를 사용할 때, 같은 단축키를 두 번 누르면 이전 도구로 토글됩니다. 이렇게 하면 같은 핫키로 두 도구를 번갈아 사용할 수 있습니다.
* `Invert Y (Zooming)` - 줌 방향을 반전합니다.
* `Reset bindings` - 모든 바인딩을 기본값으로 초기화합니다.


## iOS ⌘ Keyboard shortcuts display

키보드가 연결된 iOS 기기에서는 ⌘(cmd) 키를 길게 눌러 단축키 목록을 표시할 수 있습니다.

Android 키보드 지원은 아직 다소 실험적입니다.

![](/images/shortcuts.webp)


## Debug
일부 실험적 기능과 디버그 옵션이 이 메뉴에 있습니다. 이 옵션들 대부분은 기본값으로 두는 것이 좋으며, Nomad 지원팀과 상의한 후에만 변경하는 것을 권장합니다.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - Nomad가 UV를 [0-1] 타일 안으로 정규화합니다.

### Quad Remesh
* `Instant Mesh` - Instant remesh 알고리즘을 활성화합니다.
* `Quadriflow` - 대체 쿼드 리메시 방법입니다.

### Render
* `Heightmap` - 뷰포트를 씬의 깊이를 렌더링하는 모드로 변경합니다. 브러시에 사용할 알파 맵을 만드는 데 사용할 수 있습니다.
* `Refraction write depth (back)` - 굴절 메시의 뒷면을 깊이 버퍼에 기록합니다.
* `Flip Y (normal map)` - 노멀 맵을 베이크할 때 Y 채널을 반전합니다. 일부 게임 및 렌더 엔진에서 필요합니다.
* `Angle weighted smooth normals` - 특정 경우에 크리즈를 방지할 수 있는 스무스 셰이딩 방식 조정입니다.

### Target FPS
비활성화하면 Nomad는 디스플레이의 주사율에 프레임 레이트를 동기화합니다.

활성화하면 Nomad가 렌더링할 초당 프레임 수를 직접 설정할 수 있습니다.

### Interface
* `Top: layout` 
  * Collapse: 작은 기기에서 상단 바를 더 많은 서브 메뉴로 접습니다. 
  * Scroll: 큰 화면에서의 Nomad 레이아웃에 익숙하고 일반 레이아웃을 선호한다면, 이 옵션을 활성화해 표준 넓은 상단 바를 사용하고 스크롤할 수 있습니다.
  * Multiline: 전체 상단 메뉴를 여러 줄에 걸쳐 표시합니다.
* `Bottom: draggable popup` - 하단 툴바에는 팝업 대화 상자를 띄우는 버튼이 여러 개 있습니다. 이 옵션을 활성화하면 해당 대화 상자를 화면의 다른 위치로 이동할 수 있습니다.  
* `Toolbox: show all` - Nomad는 현재 선택에 관련 없는 도구를 숨깁니다(예: 검증되지 않은 프리미티브에서는 모든 Sculpt 브러시가 숨겨짐). 이 옵션을 활성화하면 숨기는 대신 비활성 도구를 흐리게 표시합니다.
* `Toolbox: colored` - 도구 유형에 따라 툴박스 아이콘에 색상을 부여합니다.
* `Panel: Drop shadows` - 메뉴와 패널 주변에 그림자를 그립니다. 일부 구형 기기에서는 성능에 영향을 줄 수 있습니다.
* `Panel: Blending` - 디버그 옵션
* `Pointer: hovering dot` - 스타일러스 호버를 지원하는 기기에서, 스타일러스가 메뉴와 패널 위에 호버할 때 점을 표시합니다.

### Gif turntable
Nomad는 애니메이션 gif 턴테이블을 내보낼 수 있습니다. gif 포맷의 한계로 인해 품질은 낮습니다. 일반적으로 화면 녹화가 더 좋은 방법입니다.

* `Duration` - 턴테이블의 길이(초 단위)
* `Rotation center` - 카메라 피벗 위치, 즉 카메라가 회전할 씬의 중심
* `Transparent background` - gif에 투명 배경 옵션을 사용합니다. gif는 1비트 투명도만 지원하므로, 가장자리가 심하게 계단 현상을 보일 수 있습니다.
* `Max frame sampling` - Nomad의 많은 고품질 렌더링 효과는 여러 프레임을 합성해 얻습니다. 이 슬라이더는 합성할 프레임 수를 설정합니다.
* `Export (GIF)` - gif 내보내기를 시작합니다.

### Post Process
* `Filtering` - 디버그 옵션
* `Format` - 디버그 옵션
* `Buffer reuse` - 디버그 옵션

### Performance
* `Multicore general` - 디버그 옵션
* `Multicore sculpting` - 디버그 옵션
* `Partial Drawing` - 실험적 기능입니다! 고폴리 메시의 비교적 작은 부분만 조각할 때 사용하세요. 조각이 더 부드러워질 수 있지만, 와이어프레임은 활성화하지 말아야 합니다! 또한 브러시 스트로크 중에 시각적 아티팩트가 생길 수 있습니다.

### Feature
* `Flip quad split (on tap)` -  디버그 옵션
* `Join: merge radius` - 메시를 합칠 때, 충분히 가까운 버텍스는 자동으로 용접됩니다. 이 슬라이더로 반경을 조절할 수 있습니다.

### Debug
* `Logs` - 로그 뷰를 팝업합니다.
* `App review popup` - 디버그 옵션
* `FPS` - 뷰포트 통계에 초당 프레임 수 카운터를 추가합니다.
