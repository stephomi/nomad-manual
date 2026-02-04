# ![](/icons/toolbox.webp) 도구 {#tools}

![](/images/tools_menu.webp)

::: tip
각 개별 도구 설명은 아래 [도구](#tools-1) 섹션을 참고하세요.
:::

## 개요 {#overview}

도구는 오른쪽의 `Toolbox` 에서 선택하고, 왼쪽의 `Tool Controls` 로 조작합니다. 추가 설정은 오른쪽 상단 메뉴의 첫 번째 아이콘인 `Settings` 메뉴에서 찾을 수 있습니다.

브러시 도구에는 크기와 강도 조절이 있습니다. 선택 도구에는 여러 선택 스타일을 위한 컨트롤이 있습니다. 도구 컨트롤 하단에는 자주 사용하는 작업(부드럽게, 마스크, 숨기기, 기즈모, 색상, 알파)에 대한 바로가기가 있습니다.

Nomad의 도구는 툴박스에서 색상으로 구분됩니다:

* <span class=brush>**브러시 도구**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**이동 도구**</span> (Move, Drag)
* <span class=mask>**마스크 도구**</span> (Mask, SelMask)
* <span class=paint>**페인트 도구**</span> (Paint, Smudge)
* <span class=flatten>**평탄화 도구**</span> (Flatten, Planar)
* <span class=pinch>**꼬집기 도구**</span> (Crease, Pinch)
* <span class=selection>**선택 기반 도구**</span> 먼저 2D 마스크를 그린 뒤 연산이 수행됩니다 (Trim, Split, Project)
* <span class=creation>**생성 도구**</span> (Tube, Lathe, Insert)
* <span class=transform>**변형 도구**</span> (Transform, Gizmo)
* <span class=misc>**기타 도구**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**뷰 도구**</span>



이들 도구 대부분은 [Stroke](stroke.md) 메뉴를 통해 브러시 동작, 압력, 텍스처 등을 커스터마이즈할 수 있습니다. 


### 브러시 컨트롤 {#brush-controls}

왼쪽 툴바에는 반경과 강도 슬라이더가 있으며, 그 아래에 도구 카테고리별 전용 컨트롤이 있습니다(아래에서 설명).

![](/images/tool_left_panel.webp)

::: tip
많은 도구의 강도 슬라이더는 100%를 넘길 수 있으니, 꼭 실험해 보세요!
:::

### 서브 모드 {#sub-mode}
강도 슬라이더 바로 아래 버튼은 `Sub` 버튼입니다. 이 버튼의 라벨과 기능은 도구마다 바뀌며, 누르면 보통 반대 동작에 해당하는 보조 모드를 호출합니다. 예를 들어 [Paint](#paint)에서는 지우개 모드가 되고, [Crease](#crease)에서는 홈 대신 튀어나온 엣지를 만듭니다.

기본적으로 이 버튼은 ‘홀드형’으로 동작합니다. 즉, 누르고 있는 동안만 보조 모드가 활성화되고, 손을 떼면 꺼집니다. 탭하면 Sub 모드가 계속 활성화됩니다.

### 단축키 {#shortcuts}
왼쪽 툴바 하단에는 [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha) 에 대한 바로가기 버튼이 있습니다. 

기본적으로 이들 역시 모두 ‘홀드형’으로 동작합니다. 즉, 누르고 있는 동안만 해당 모드가 활성화되고, 손을 떼면 꺼집니다. 탭하면 해당 바로가기 모드가 계속 활성화됩니다.

### 선택 컨트롤 {#selection-controls}

[Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup), [Hide](#hide) 도구는 모두 메시 영역 선택을 위해 비슷한 컨트롤을 사용합니다.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - 자유 곡선으로 그리는 형태
* `Polygon` - 곡선과 직선을 조합해 정의하는 폐곡선. 자세한 내용은 아래 [Shape editing](#shape-editing) 참고.
* `Curve` - (Project 전용) - 투영에 사용할 자유 곡선
* `Path` - (Project 전용) - 점으로 정의하는 곡선. 자세한 내용은 아래 [Shape editing](#shape-editing) 참고.
* `Line` - 선을 드래그해 평면 세그먼트를 정의합니다. 기본적으로 즉시 메시에 작동하며, 이를 원치 않으면 자동 검증(auto validate)을 끄세요(라인 아이콘을 길게 누르거나 스와이프).
* `Rect` - 대각선으로 드래그하면 사각형의 두 꼭짓점을 정의합니다. 길게 누르거나 스와이프하면 자동 검증, 정사각형 강제, 첫 클릭을 사각형 중심으로 사용할지에 대한 옵션이 나타납니다.
* `Ellipse` - 대각선으로 드래그하면 타원의 크기를 정의합니다. 길게 누르거나 스와이프하면 자동 검증, 원형 강제, 첫 클릭을 타원 중심으로 사용할지에 대한 옵션이 나타납니다.
* `Flip` - 셰이프 마스크를 반전하거나 Project 도구의 방향을 반전합니다.

대부분의 도구에는 자동 검증(auto validate) 옵션이 있어, 셰이프를 다 그리는 즉시 연산이 수행됩니다. 자동 검증이 꺼져 있으면 셰이프 옆에 초록색 버튼이 나타나며, 이 버튼을 눌러 연산을 실행합니다. 이 모드에서는 셰이프를 편집하거나 뷰를 조정한 뒤, 준비가 되면 초록 버튼을 눌러 사용할 수 있습니다.

### 형태 편집 {#shape-editing}
폴리곤 편집과 커브 편집은 비슷하게 동작합니다:

* 먼저 선을 드래그해 두 점을 정의한 뒤, 선의 가운데를 드래그해 폴리곤이나 커브를 만듭니다.
* 점을 탭해 부드러운 점과 날카로운 점을 토글합니다. 
* 곡선이나 선 구간을 클릭 후 드래그해 새 점을 만듭니다.
* 점을 삭제하려면, 해당 점을 이웃 점 쪽으로 드래그해 빨갛게 변할 때까지 이동합니다.
* 폴리곤 또는 패스 아이콘 모서리의 휴지통 아이콘을 누르면 셰이프가 삭제됩니다.

### 설정 메뉴 {#settings-menu}

많은 도구에는 추가 설정이 있으며, 오른쪽 상단 메뉴의 첫 번째 아이콘인 Settings 메뉴에서 찾을 수 있습니다:

![](/images/tools_settings_menu.webp)

## 도구 {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) 클레이 {#clay}
Clay 도구는 조형을 쌓아 올릴 때 유용합니다. `Sub` 는 조형에서 재질을 깎아냅니다.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) 브러시 {#brush}
표준 브러시입니다. `Sub` 는 재질을 제거합니다.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) 이동 {#move}
브러시 아래 영역이 브러시에 달라붙어 탄성 변형을 할 수 있습니다. 이동 중에는 선택 영역이 유지되므로, 브러시를 멀리 이동했다가 다시 시작 지점으로 가져오면 변형이 사라진 것을 볼 수 있습니다.

Sub 모드는 `Normal` 이며, 브러시 아래 영역을 표면 노멀 방향으로 이동시킵니다.

이 브러시는 큰 형태 변형과 섬세한 소규모 변형 모두에 적합합니다.

#### 이동 설정 {#move-settings}

* `Radius (Background)` - 모델의 실루엣을 작업할 때처럼, 모델의 가장자리에서 얼마나 떨어져 있어도 조각이 가능한지 설정합니다. 
* `Same-side vertex only` - 변형 방향과 반대 방향을 향하는 버텍스는 무시합니다.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) 드래그 {#drag}
브러시 아래 영역이 브러시에 달라붙어 탄성 변형을 합니다. Move 브러시와 달리, 드래그 중에는 선택 영역이 계속 갱신되므로, 특히 Dynamic Topology가 활성화된 상태에서 긴 뱀 같은 형태를 만들 수 있습니다.

Sub 모드는 `Normal` 이며, 브러시 아래 영역을 표면 노멀 방향으로 이동시킵니다.

이 브러시는 보다 느슨하고 제스처적인 형태 변형에 적합합니다.

#### 드래그 설정 {#drag-settings}

* `Radius (Background)` - 모델의 실루엣을 작업할 때처럼, 모델의 가장자리에서 얼마나 떨어져 있어도 조각이 가능한지 설정합니다. 
* `Same-side vertex only` - 변형 방향과 반대 방향을 향하는 버텍스는 무시합니다.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) 스무스 {#smooth}
포인트 위치의 평균을 내어 영역을 부드럽게 합니다. 이 도구는 폴리곤 밀도에 크게 의존합니다.
폴리곤이 많을수록 스무딩 효과는 덜 강하게 느껴질 수 있습니다.

Sub 모드는 `Relax` 로, 지오메트리 디테일을 유지하려 하면서 와이어프레임만 부드럽게 합니다.

#### 스무스 설정 {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### 페이스 그룹 {#smooth-facegroup}

* `Relax` - 페이스그룹 경계를 부드럽게 합니다. 100% 이상의 강도를 사용하면 경계를 빠르게 부드럽게 할 수 있습니다. `Auto` 는 페이스그룹 프리뷰가 활성화된 경우에만 스무딩, `Off` 는 비활성, `On` 은 항상 활성입니다. 

##### 버텍스 {#vertex}
* `Sticky vertex on border` - 평면처럼 열린 엣지를 가진 메시에서 모서리를 평탄하게 만들 수 있습니다. 이 옵션을 활성화하면 열린 엣지가 고정됩니다.
* `Relax` - 왼쪽 툴바의 Relax 보조 모드와 동일합니다.
* `Stable smoothing` - 토폴로지에 덜 의존적인 스무딩을 시도합니다. 토폴로지 밀도가 고르지 않을 때, 그리고 높은 스무딩 강도에서 가장 잘 작동합니다.

##### 페인팅 {#painting}
* `Screen Smoothing` - 매우 높은 폴리곤 수에서도 토폴로지에 독립적인 스무딩을 얻고 싶을 때 사용합니다.
* `Screen samples` - 스무딩 품질입니다. 값이 높을수록 더 부드럽지만 느려집니다.

::: tip
폴리곤 밀도가 높을수록 강도를 100% 이상으로 올려야 할 수 있습니다. 매우 높은 값(300%, 500%)은 조형 도구처럼 사용할 수도 있어, 브러시 아래 영역을 빠르게 평평하고 매끈하게 만들 수 있습니다. 마치 점토를 망치로 두드리는 느낌입니다!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) 마스크 {#mask}
이 도구는 버텍스를 마스킹합니다. 마스크된 버텍스는 조각이나 페인팅으로부터 보호됩니다. 

Sub 모드는 `Unmask` 로, 그려진 마스크를 지웁니다.

2D 페인팅 프로그램의 선택처럼, 마스크는 브러시로 칠하거나 셰이프 선택으로 만들 수 있고, 블러/샤픈할 수 있습니다. 

2D 페인팅 프로그램과 달리, 페이스그룹을 통해서도 만들 수 있으며, 마스크를 이용해 돌출/추출 방식으로 새 지오메트리를 생성할 수도 있습니다. 

![](/videos/tool_mask1.mp4)

 뷰포트 상단에 추가 컨트롤이 있는 툴바가 나타납니다. 

![](/images/tool_mask_toolbar.webp)

툴바의 제목을 탭하면 펼치기/접기가 되고, 오른쪽 상단의 화살표를 탭하면 UI의 위/아래로 위치를 옮길 수 있습니다.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Clear              | 마스크를 모두 지웁니다                                                                    |
| ![](/icons/invert.webp)        Invert             | 마스크를 반전합니다                                                                       |
| ![](/icons/sharpen.webp)       Sharpen            | 마스크 가장자리를 선명하게 합니다                                                         |
| ![](/icons/blur.webp)          Blur               | 마스크 가장자리를 블러 처리합니다                                                         |
|                                 Blur ->            | 좌우 드래그로 마스크 블러를 인터랙티브하게 조절합니다                                     |
| ![](/icons/culling.webp)       Front              | 전면을 향한 버텍스만 마스킹하도록 토글합니다                                              |
|                                 Convert            | 마스크를 페이스그룹으로 변환합니다                                                        |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | 활성화 시 페이스그룹이 표시되며, 페이스그룹을 탭하면 해당 그룹이 마스킹됩니다             |
|                                 On tap (mask)      | 활성화 시 마스크/비마스크 ‘섬’을 탭하면 해당 섬 전체를 플러드 필합니다.                  |
| ![](/icons/vertex.webp)        Connected          | 활성화 시 연결된 토폴로지에만 마스크 스트로크가 영향을 줍니다.                           |

##### 마스크 퀵 제스처 {#mask-quick-gesture}
왼쪽 퀵 마스킹 버튼을 누른 상태에서 ZBrush 스타일 제스처를 사용할 수 있습니다:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | 배경을 탭                          |
| Clear   | 배경을 드래그                      |
| Blur    | 마스크된 영역을 탭                 |
| Sharpen | 마스크되지 않은 영역을 탭          |


#### 마스크 설정 {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Mask 설정 메뉴는 주로 마스크에서 지오메트리를 생성하는 데 사용됩니다. 이 때문에 기본 동작은 새 지오메트리가 어떻게 보일지 미리보기입니다. 프리뷰 없음, 추출 프리뷰, 분할 프리뷰, 그리고 이 지오메트리를 X-ray 모드로 표시할지 여부를 선택할 수 있습니다.

##### 두께 {#thickness}
* `Height` - 추출된 형태의 높이입니다. 플러스/마이너스 아이콘으로 바깥쪽 돌출, 안쪽 돌출, 중앙 기준 돌출을 순환할 수 있습니다. 
* `Height/Height+Mask` - 높이를 일정하게 둘지, 마스크의 블러 정도가 높이에 영향을 주도록 할지 토글합니다. 후자는 부드럽고 가변적인 높이의 형태를 만들 수 있습니다. 

##### 부드러움 {#smoothness}
활성화 시 추출된 형태의 경계를 부드럽게 합니다. 폴리곤 수가 많을수록 더 잘 작동합니다. 
* `Iterations` - 적용되는 스무딩 양입니다. 값이 높을수록 매우 부드러운 곡선 엣지를 만들지만, 마스크 형태에서 점점 멀어질 수 있습니다.
* `All/Sharp border/Borders only` - 스무딩 방향을 설정합니다. 전체(All)는 측면과 윗면 모두를 부드럽게 하고, Sharp border는 윗면과 측면을 부드럽게 하되 엣지는 날카롭게 유지하며, Borders only는 경계만 부드럽게 하고 윗면은 그대로 둡니다.

##### 엣지 루프 (측면) {#edge-loop-side}
* `Auto Edge-loop (side)` - 추출된 형태의 측면에 자동으로 엣지 루프 수를 계산해, 마스크된 영역의 폴리곤과 맞는 정사각형 폴리곤을 만듭니다. 비활성화 시 슬라이더로 엣지 루프 수를 직접 설정할 수 있습니다.

----

##### 추출 {#extract}
* `Extract` - 추출 지오메트리를 생성합니다.
* `Closing action` - 추출 시 동작 방식을 설정합니다. 'None' 은 마스크된 폴리곤을 새 형태로 복제만 합니다. 'Fill' 은 복제 후 뒷면을 메우려 시도합니다. 'Shell' 은 'thickness' 에 설정된 만큼 돌출하며, 기본값입니다.

::: tip

프리뷰가 'Extract' 모드이고 'X-ray' 가 활성화된 상태에서 Extract 버튼을 누르면 처음에는 헷갈릴 수 있습니다. 메뉴가 활성화되어 있기 때문에, 새 형태에 대해 또 다른 추출 프리뷰를 시도하고, 원래 표면을 X-ray 처리합니다. 하지만 새 표면에는 마스크가 없으므로 추출을 미리 볼 수 없고, Nomad는 'Nothing to Extract!' 경고를 띄웁니다. 

이는 정상 동작입니다. 새 형태와 원본을 보기 위해 Mask 설정 메뉴를 닫고, 필요하다면 원본 표면을 다시 선택해 마스크를 지우거나 새 마스크를 그리세요.
:::

##### 분리 {#split-mask}
* `Split` - 마스크된 영역과 마스크되지 않은 영역 모두를 새 형태로 추출합니다. 
* `Closing action (masked)` - 마스크된 영역 추출의 동작 방식을 설정합니다. 'None', 'Fill', 'Shell' 의 의미는 Extract와 동일합니다.
* `Closing action (unmasked)` - 마스크되지 않은 영역 추출의 동작 방식을 설정합니다. 'None', 'Fill', 'Shell' 의 의미는 동일합니다.
* `Sync border` - 마스크된/비마스크된 추출 형태 사이의 경계가 서로 가깝게 유지되도록 합니다. 비활성화 시, Shell 연산이 각 면의 노멀 방향으로 돌출하기 때문에 두 형태 사이에 틈이 생길 수 있습니다.

##### 조각 {#carve}
* `Carve` - 기본 모드에서, 'thickness' 만큼 표면을 Trim 한 것처럼 동작합니다. 오렌지 껍질 한 조각을 도려낸 것과 비슷합니다. 



### ![](/icons/tool_maskSelector.webp) 선택 마스크 {#selection-mask}
이 도구는 대부분 [Mask 도구](#mask)와 비슷하지만, 스트로크로 마스크를 칠하는 대신 [Selection Controls](#selection-controls)를 사용해 마스크를 만듭니다.

Sub 모드는 `Unmask` 로, 선택 컨트롤을 사용해 마스크를 지웁니다.

Selection Mask는 `Mask` 도구와 동일한 도구 설정을 공유합니다.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) 페인트 {#paint}
색상과 머티리얼 속성을 적용합니다. 머티리얼에 대한 자세한 내용은 [Painting](painting.md) 섹션을 참고하세요.

Sub 모드는 `Erase` 로, 페인트를 제거합니다.

#### 페인트 설정 {#paint-settings}
* `Layer fitering` - Photoshop이나 Procreate의 레이어 알파 잠금과 비슷하게 동작합니다. 레이어에 페인팅 중일 때 이 옵션을 활성화하면, 이미 페인트가 있는 영역만 수정할 수 있고, 칠해지지 않은 영역은 보호됩니다.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) 스머지 {#smudge}
색상과 머티리얼 속성을 문지릅니다. Smudge 설정 메뉴에는 `Quality` 슬라이더가 있으며, 값이 낮을수록 스트로크가 더 빠릅니다.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) 플래튼 {#flatten}
포인트를 평균 평면에 투영해 영역을 평탄하게 만듭니다.

Sub 모드는 `Fill` 이며, 가장 높은 포인트를 기준으로 평면을 정의하고 포인트를 위로 끌어올리는 경향이 있습니다.

#### 플래튼 설정 {#flatten-settings}

* `Lock plane direction` - 첫 클릭에서 계산된 평면 방향을 계속 사용합니다. 기본값은 비활성입니다.
* `Lock plane origin`- 첫 클릭 위치를 평면의 중심으로 사용합니다. 기본값은 비활성입니다.

이 둘 중 하나 또는 둘 다 비활성일 때, 긴 스트로크로 서로 다른 깊이와 곡률을 가로지르며 평탄화하면 점차 더 깊게 파이거나 평면 각도를 바꿀 수 있습니다. 이는 브러시 메뉴의 영역 샘플링 옵션과 함께 사용하면 매우 정밀한 제어가 가능합니다.

::: tip
곡률이 큰 영역(예: 볼을 평탄하게 만들고 싶은데 도구가 계속 코 옆면까지 영향을 줄 때)에서는, Flatten 브러시가 영향을 주지 말아야 할 영역을 마스크로 보호해 보세요.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) 플래너 {#planar}
포인트를 평균 평면에 투영해 평탄하게 만들지만, Flatten 브러시보다 누적 효과가 적습니다. 더 깨끗한 하드 엣지 표면을 만들 수 있습니다. 짧은 스트로크는 표면을 더 밀고 당기고, 이미 평탄한 영역에서 시작해 바깥으로 천천히 그리면 평면을 더 잘 유지합니다.

Sub 모드는 `Fill` 이며, 가장 높은 포인트를 기준으로 평면을 정의하고 포인트를 위로 끌어올리는 경향이 있습니다.

Planar는 실제로 `Flatten` 과 같은 도구지만, `Lock plane direction` 이 활성화되어 있어 보다 안정적이고 하드한 표면을 만들고, Flatten은 더 조형적이며 반쯤 평평한 영역을 만드는 데 사용할 수 있습니다.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) 크리스 {#crease}
Crease 도구는 작은 컷이나 홈을 조각할 때 유용합니다.

Sub 모드는 `Invert` 로, 홈 대신 튀어나온 크리즈를 만듭니다.

#### 크리스 설정 {#crease-settings}

* `Pinch factor` - 버텍스를 브러시 쪽으로 옆으로 얼마나 끌어당길지 설정합니다. Pinch가 1이고 Offset이 0이면, 표면 깊이 변화 없이 토폴로지만 변하며, 엣지가 스트로크 쪽으로 모입니다.
* `Offset factor` - 버텍스를 깊이 방향으로 얼마나 밀고 당길지 설정합니다. Pinch가 0이고 Offset이 1이면 깊은 홈이나 튀어나온 자국이 생기지만, 크리즈의 양옆과 바닥을 정의할 만큼 충분한 지오메트리가 끌려오지 않아 거칠어 보일 수 있습니다.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) 핀치 {#pinch}
엣지를 날카롭게 만드는 데 사용할 수 있습니다.

Sub 모드는 `Invert` 로, 버텍스를 서로 멀어지게 퍼뜨립니다.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) 트림 {#trim}
Trim 도구는 메시의 일부를 잘라내고, 남은 구멍을 어떻게 처리할지에 대한 옵션을 제공합니다. 잘라낼 영역은 [Selection controls](#selection-controls)를 사용해 정의합니다.

::: tip
이 도구는 카메라에서 투영해 작동하므로, 카메라가 원근(perspective) 모드일 때 경고가 표시됩니다.

정투영(orthographic) 모드에서는 메시를 가르는 컷이 뷰와 평행하게 이루어져, 대부분 사용자가 기대하는 결과를 얻습니다. 원근 카메라에서는 객체의 앞쪽과 뒤쪽에서 컷 모양이 다르게 보입니다.
:::

#### 트림 설정 {#trim-settings}

* `Stroke painting` - 페인트 메뉴에서 페인트가 활성화되어 있으면, 메워진 영역이 현재 선택된 색으로 채워집니다.
* `Boolean` - Trim으로 생긴 구멍을 쿼드 폴리 영역으로 메웁니다. 메워진 영역은 평평합니다.
* `Legacy` - Trim 구멍을 삼각형 영역으로 메웁니다. 메워진 영역은 평평합니다.
* `Fill` - 구멍을 삼각형 영역으로 메웁니다. 메워진 영역은 비눗방울 막처럼 곡면입니다.
* `None` - 구멍을 메우지 않습니다.
* `Boolean Detail Shape` - Trim된 ‘형태 쪽’에 사용되는 쿼드와 삼각형의 대략적인 크기입니다.
* `Boolean Detail Hole` - 메워진 구멍 쪽에 사용되는 삼각형 또는 폴리곤의 대략적인 크기입니다. 
* `Legacy Detail` - Trim에 사용되는 삼각형의 대략적인 크기입니다.
* `Legacy Hole smoothing` - 메워진 영역의 삼각형을 얼마나 완화(relax)할지 설정합니다.
* `Legacy Threshold espilon` - 레거시 홀 필 알고리즘을 개선하기 위해 조정할 수 있는 값입니다.
* `Fill Detail` - Trim에 사용되는 삼각형의 대략적인 크기입니다.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) 스플릿 {#split}
[Trim](#trim) 도구와 비슷하지만, Trim이 선택 영역을 버리는 반면 Split은 선택 영역을 새 오브젝트로 유지합니다.

#### 스플릿 설정 {#split-settings}

* `Stroke painting` - 페인트 메뉴에서 페인트가 활성화되어 있으면, 메워진 영역이 현재 선택된 색으로 채워집니다.
* `Boolean` - Split으로 생긴 구멍을 쿼드 폴리 영역으로 메웁니다. 메워진 영역은 평평합니다.
* `Legacy` - Split 구멍을 삼각형 영역으로 메웁니다. 메워진 영역은 평평합니다.
* `Fill` - 구멍을 삼각형 영역으로 메웁니다. 메워진 영역은 비눗방울 막처럼 곡면입니다.
* `None` - 구멍을 메우지 않습니다.
* `Boolean Detail Shape` - Split된 ‘형태 쪽’에 사용되는 쿼드와 삼각형의 대략적인 크기입니다.
* `Boolean Detail Hole` - 메워진 구멍 쪽에 사용되는 삼각형 또는 폴리곤의 대략적인 크기입니다. 
* `Legacy Detail` - Split에 사용되는 삼각형의 대략적인 크기입니다.
* `Legacy Hole smoothing` - 메워진 영역의 삼각형을 얼마나 완화(relax)할지 설정합니다.
* `Legacy Threshold espilon` - 레거시 홀 필 알고리즘을 개선하기 위해 조정할 수 있는 값입니다.
* `Fill Detail` - Split에 사용되는 삼각형의 대략적인 크기입니다.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) 프로젝트 {#project}
Project 도구는 겉보기에는 [Trim](#trim) 도구와 비슷하지만, 지오메트리를 삭제하거나 생성하지 않고, 단지 버텍스를 선택 영역에 맞게 이동시킵니다.

![](/videos/tool_project.mp4)

::: tip
레이어 위에서 Project를 사용하면, 레이어 슬라이더로 원래 형태와 투영된 형태 사이를 블렌딩할 수 있습니다.
:::

### ![](/icons/tool_layer.webp) 레이어 {#layer}
표면을 올리되, 높이에 제한을 둡니다.

펜을 떼지 않고 같은 영역을 계속 칠해도, Layer는 일정 높이까지만 올리고 그 이상은 더 올라가지 않습니다. 다른 도구들은 계속 높이가 누적되는 것과 대조적입니다.

단, 기본적으로 이 제한은 ‘스트로크당’으로만 적용됩니다! 새 스트로크를 시작하면, 새 표면 높이에서 다시 쌓입니다.

여러 스트로크에 걸쳐 일정한 최대 높이를 유지하려면, Nomad의 [Layers](layers.md) 시스템과 함께 Layer 도구를 사용하세요.

레이어를 만든 뒤 이 도구를 사용하면, 최대 높이가 레이어에 의해 고정되므로, 여러 번 브러시를 그어도 높이는 항상 동일하게 유지됩니다.

`Sub` 는 최소 깊이를 사용해 홈을 만듭니다.

#### 레이어 설정 {#layer-settings}

* `Use layer data` - 활성화 시, 선택된 레이어가 있을 경우 레이어 데이터를 사용해 최대 높이를 설정합니다.
* `Inflate`- 활성화 시 Layer가 작동하는 방향을 조정해 더 부드러운 결과를 얻습니다.
* `Relax (Normal)` - 노멀에 적용되는 스무딩 양입니다.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) 인플레이트 {#inflate}
버텍스를 각자의 노멀 방향으로 이동시킵니다. `Sub` 는 버텍스를 반대 노멀 방향으로 이동시킵니다.

#### 인플레이트 설정 {#inflate-setings}
* `Relax (Normal)` - 노멀에 적용되는 스무딩 양입니다.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) 너지 {#nudge}
스트로크 방향으로 포인트를 이동하거나 ‘문지릅니다’.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) 스탬프 {#stamp}

선택된 알파 모양대로 조형의 한 영역을 클릭-드래그해 돌출시킵니다.

이는 Stroke 타입이 `Lock + radius` 로 설정된 [Brush 도구](#brush)에 불과합니다. 

`Sub` 는 스탬프를 밖으로 빼내는 대신 안으로 밀어 넣습니다.

::: tip
Stamp는 보통 고해상도 지오메트리에서 가장 잘 작동합니다. 온라인에서 'wrinkles alpha', 'pores alpha', 'scales alpha' 등을 검색하면, 이 알파 텍스처와 Stamp를 이용해 캐릭터 스컬프에 유기적인 디테일을 더하는 데 큰 도움이 됩니다.

두 가지 스트로크 모드는 서로 다른 용도에 유용합니다. 

* `Lock + radius` 는 *높이*가 고정되며, 드래그로 스탬프의 폭과 회전을 조절합니다. 깊이/높이는 같지만 회전과 스케일만 달라야 하는 피부 텍스처에 좋습니다. 반복 패턴을 숨기기에도 유리합니다.
* `Lock + intensity` 는 *폭*이 고정되며, 드래그로 회전과 높이를 조절합니다. 크기는 같고 회전과 높이만 달라야 하는 리벳 등에 좋습니다. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) 레이어 삭제 {#delete-layer}
이 도구는 레이어를 국소적으로 리셋할 수 있습니다. 활성 레이어가 없으면 아무 일도 일어나지 않습니다.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) 튜브 {#tube}
곡선을 그려 튜브를 생성합니다. 
![](/images/tool_tube_new.webp)

튜브가 생성되면, 표준 [Shape editing](#shape-editing) 및 커브 편집 도구와 유사한 컨트롤을 사용해 3D 공간에서 경로를 편집할 수 있습니다. 

![](/videos/tool_tube.mp4)

#### 튜브 왼쪽 툴바 {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

왼쪽 툴바에는 다음 옵션이 있습니다:

* `Sync` - 현재 튜브가 인스턴스이고, 인스턴스 간에 튜브의 자식 노드가 서로 다를 경우 이를 다시 동기화합니다.
* `Snap` - 활성화 시, Curve와 Path 모드에서 그리는 동안 다른 오브젝트에 스냅됩니다. 비활성화 시, 첫 점만 스냅되고 나머지 튜브는 그 깊이에 맞춰 그려집니다. 작은 플라이아웃 메뉴가 있습니다:
    * `Offset` - 스냅 깊이를 설정합니다. 0% 는 튜브 단면의 중앙이 표면에 스냅되며, 양수는 표면에서 띄우고, 음수는 표면 안으로 넣습니다.
* `Curve` - 자유 곡선으로 튜브를 스케치합니다. 작은 플라이아웃 메뉴가 있습니다:
    * `Auto-validate` - 스트로크가 끝나는 즉시 튜브를 생성합니다. 비활성화 시, 곡선 경로 옆에 초록색 검증 원이 표시되며, 이를 눌러 확정하거나 이 메뉴에 나타나는 `Reset` 링크로 경로를 삭제할 수 있습니다.
    * `Closed` - 튜브를 루프로 만듭니다.
    * `Screen` - Auto-validate가 비활성일 때만 사용 가능. 활성화 시 경로가 화면에 ‘고정’되어, 뷰와 오브젝트를 움직여도 경로는 제자리에 남습니다. 비활성화 시 경로는 3D 씬의 일부가 되어 카메라와 오브젝트와 함께 움직입니다.
    * `Accuracy` - 그려진 경로를 튜브로 변환할 때 사용할 커브 포인트 수입니다. 0% 는 최소 포인트를 사용해 작은 곡률 변화를 놓칠 수 있고, 100% 는 매우 정확하지만 많은 포인트를 사용합니다.
* `Path` - 클릭으로 커브 포인트를 정의해 튜브를 만듭니다. 초록색 원을 탭해 경로를 확정합니다. 작은 플라이아웃 메뉴가 있습니다:
    * `B-spline` - 커브 포인트가 곡선 위에 직접 놓이지 않는 대신 더 부드러운 결과를 낼 수 있는 대체 커브 방식입니다.
    * `Closed` - 튜브를 루프로 만듭니다.
    * `Screen` - 활성화 시 경로가 화면에 ‘고정’되어, 뷰와 오브젝트를 움직여도 경로는 제자리에 남습니다. 비활성화 시 경로는 3D 씬의 일부가 되어 카메라와 오브젝트와 함께 움직입니다.

##### 튜브 상단 툴바 {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
튜브가 선택되면, 뷰포트 상단에 추가 컨트롤이 있는 툴바가 나타납니다. 툴바 제목을 클릭해 접기/펼치기를 하고, 오른쪽 상단 화살표를 클릭해 툴바를 뷰포트 위/아래로 이동할 수 있습니다.

* `Validate` - 튜브를 일반 폴리곤으로 베이크해 조각할 수 있게 합니다.
* `Edit` - 커브 포인트를 표시해 조작할 수 있게 합니다.
* `Mirror` - 이 커브의 부모로 미러 리피터를 추가합니다.
* `Snap` - 커브 포인트를 인근 표면에 스냅합니다.
* `Closed` - 커브의 시작과 끝을 이어 루프를 만듭니다.
* `B-spline` - Catmull-rom과 B-spline 보간을 토글합니다.
* `Cap` - 튜브 양 끝에 캡을 모두 씌우거나, 시작/끝만 씌우거나, 캡 없음으로 순환합니다.
* `Hole` - 튜브에 두께를 추가해 파이프 형태로 만듭니다. 양 끝 모두 구멍, 끝만 구멍, 구멍 없음으로 순환합니다. 
* `Radius` - 반경을 균일, 시작/끝, 포인트별 반경으로 순환합니다. 이는 커브 위의 주황색 핸들로 편집합니다.
* `Twist` - 트위스트 없음, 균일 트위스트, 시작/끝 트위스트, 포인트별 트위스트로 순환합니다. 이는 커브 위의 분홍색 핸들로 편집합니다.
* `Profile` - 프로파일 없음(원형 단면), 균일 프로파일, 시작/끝 프로파일, 포인트별 프로파일로 순환합니다.
* `Profile edit` - 프로파일 에디터를 표시합니다. 이는 [Shape editing](#shape-editing) 도구와 비슷하게 동작하며, 프로파일 프리셋 저장/불러오기를 지원하고, 3D 공간에서 프로파일을 편집할 수 있는 토글이 있습니다.
* `Spiral` - 튜브에 나선형 트위스트를 추가하는 메뉴를 토글합니다. 이 메뉴에는 `Twist Angle`, `Offset`, `Scale`, `Angle offset` 옵션이 있습니다.
* `X Divisions` - 튜브 둘레 방향 분할 수입니다. 예를 들어 4 분할이면 사각형 튜브가 됩니다. 
* `Constant density` - 활성화 시 폴리곤을 정사각형으로 유지합니다. 비활성화 시 튜브 길이 방향의 `Y divisions` 를 설정할 수 있습니다.
* `...` - Tube 설정 메뉴입니다.

#### 커브 포인트 삭제 토글 {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

툴바 아래에는 커브 포인트 삭제 토글이 있습니다. 커브 포인트를 다른 포인트 근처로 드래그하면 빨갛게 변하며, 이 상태에서 손을 떼면 포인트가 삭제됩니다. 작은 편집을 할 때 포인트를 삭제하고 싶지 않다면, 이 버튼으로 포인트 삭제 동작을 비활성화할 수 있습니다.



#### 튜브 설정 {#tube-settings}
* `Primitive` - UV 활성/비활성, 튜브 검증(Validate)을 위한 버튼입니다.
* `Post subdivision` - 검증 전에 멀티레졸루션 레벨을 설정하는 바로가기입니다.
* `Linear subdivision` - 검증 전에 선형 서브디비전 레벨을 설정하는 바로가기입니다. 
* `Division X` - 툴바의 X Divisions와 동일합니다.
* `Division Y` - 툴바의 Y Divisions와 동일합니다.
* `Curve (Repeater)` - 튜브를 [Curve Repeater](scene.md#curve)로 변환합니다.

::: tip
Division을 4로, Post subdivision을 3으로 설정하면 끝이 둥근 매끄러운 튜브가 만들어져, 벌레, 뱀, 신체 일부 등에 좋습니다.
:::


### ![](/icons/tool_lathe.webp) 레이스 {#lathe}
곡선을 그려 회전 표면을 생성합니다.

이 도구는 꽃병, 와인잔 같은 형태에 적합합니다.

![](/videos/tool_lathe.mp4)

#### 레이스 왼쪽 툴바 {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

왼쪽 툴바에는 다음 옵션이 있습니다:

* `Sync` - 현재 Lathe가 인스턴스이고, 인스턴스 간에 Lathe의 자식 노드가 서로 다를 경우 이를 다시 동기화합니다.
* `Fixed` - 활성화 시 Lathe의 중심이 고정되어 화면에 표시됩니다. 이 중심선에는 조정 가능한 편집 포인트가 있습니다. 비활성화 시, Lathe의 중심은 그려진 곡선의 시작과 끝에 맞춰 동적으로 업데이트됩니다.
* `Curve` - 한 번의 스트로크로 Lathe 프로파일을 그립니다. 작은 플라이아웃 메뉴가 있습니다:
    * `Auto-validate` - 활성화 시, 펜을 화면에서 떼는 순간 Lathe가 생성됩니다. 비활성화 시, 곡선 옆의 초록색 원을 눌러 Lathe를 생성할 수 있습니다. `Reset` 버튼으로 곡선을 삭제할 수 있습니다.
    * `Closed` - 곡선의 시작과 끝을 이어 루프를 만듭니다.
    * `Screen` - Auto-validate가 비활성일 때만 사용 가능. 활성화 시 경로가 화면에 ‘고정’되어, 뷰와 오브젝트를 움직여도 경로는 제자리에 남습니다. 비활성화 시 경로는 3D 씬의 일부가 되어 카메라와 오브젝트와 함께 움직입니다.
    * `Accuracy` - 그려진 경로를 튜브로 변환할 때 사용할 커브 포인트 수입니다. 0% 는 최소 포인트를 사용해 작은 곡률 변화를 놓칠 수 있고, 100% 는 매우 정확하지만 많은 포인트를 사용합니다.
* `Path` - 클릭으로 커브 포인트를 정의해 Lathe를 만듭니다. 초록색 원을 탭해 경로를 확정합니다. 작은 플라이아웃 메뉴가 있습니다:
    * `B-spline` - 커브 포인트가 곡선 위에 직접 놓이지 않는 대신 더 부드러운 결과를 낼 수 있는 대체 커브 방식입니다.
    * `Closed` - 튜브를 루프로 만듭니다.
    * `Screen` - 활성화 시 경로가 화면에 ‘고정’되어, 뷰와 오브젝트를 움직여도 경로는 제자리에 남습니다. 비활성화 시 경로는 3D 씬의 일부가 되어 카메라와 오브젝트와 함께 움직입니다.

#### 레이스 상단 툴바 {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Lathe가 선택되면, 뷰포트 상단에 추가 컨트롤이 있는 툴바가 나타납니다. 툴바 제목을 클릭해 접기/펼치기를 하고, 오른쪽 상단 화살표를 클릭해 툴바를 뷰포트 위/아래로 이동할 수 있습니다.

* `Validate` - Lathe를 일반 폴리곤으로 베이크해 조각할 수 있게 합니다.
* `Edit` - 커브 포인트를 표시해 조작할 수 있게 합니다.
* `Mirror` - 이 Lathe의 부모로 미러 리피터를 추가합니다.
* `Snap` - 커브 포인트를 인근 표면에 스냅합니다.
* `Stable` - 활성화 시, 커브 프로파일이 Lathe 중심선의 자식이 됩니다. 비활성화 시, 중심선을 편집해도 커브는 움직이지 않아 더 복잡한 형태를 만들 수 있습니다.
* `Focus` - 뷰를 회전시켜 커브 프로파일을 카메라에 완전히 평평하게 보이도록 합니다.
* `Closed` - 곡선의 시작과 끝을 이어 루프를 만듭니다.
* `Cap` - Closed가 비활성일 때, 튜브 양 끝에 캡을 모두 씌우거나, 시작/끝만 씌우거나, 캡 없음으로 순환합니다.
* `Hole` - Lathe에 두께를 추가해 파이프 형태로 만듭니다. 양 끝 모두 구멍, 끝만 구멍, 구멍 없음으로 순환합니다. 
* `B-spline` - Catmull-rom과 B-spline 보간을 토글합니다.
* `X Divisions` - Lathe 둘레 방향 분할 수입니다. 예를 들어 4 분할이면 사각형 프로파일 Lathe가 됩니다. 
* `Constant density` - 활성화 시 폴리곤을 정사각형으로 유지합니다. 비활성화 시 튜브 길이 방향의 `Y divisions` 를 설정할 수 있습니다.
* `...` - Lathe 설정 메뉴입니다.

#### 레이스 설정 {#lathe-settings}
* `Primitive` - UV 활성/비활성, 튜브 검증(Validate)을 위한 버튼입니다.
* `Post subdivision` - 검증 전에 멀티레졸루션 레벨을 설정하는 바로가기입니다.
* `Linear subdivision` - 검증 전에 선형 서브디비전 레벨을 설정하는 바로가기입니다. 
* `Division X` - 툴바의 X Divisions와 동일합니다.
* `Division Y` - 툴바의 Y Divisions와 동일합니다.
* `Curve (Repeater)` - 커브 프로파일을 [Curve Repeater](scene.md#curve)로 변환합니다.

### ![](/icons/tool_insert.webp) 인서트 {#insert}
다른 표면 위에 오브젝트를 배치합니다. 사용감은 Stamp 도구와 비슷하지만, 완전한 3D 형태를 사용합니다.

왼쪽 툴바에서 프리미티브를 선택한 뒤, 어떤 표면이든 클릭-드래그하면 클릭한 위치에 프리미티브가 배치되고, 드래그 길이로 크기가 정해집니다. 드래그를 마치면 Insert는 [Transform](#transform) 모드로 전환됩니다.

Instance 모드에서는 드래그로 새 인스턴스를 생성하고 표면 위를 미끄러뜨립니다. 크기는 첫 형태에서 복제되므로, 동일한 크기의 오브젝트 인스턴스를 여러 개 표면 위에 배치할 수 있습니다.

프리미티브만 삽입할 필요는 없습니다! 아웃라이너에서 *어떤* 형태든 선택한 뒤, Insert가 Instance 또는 Clone 모드일 때 다른 표면 위로 드래그하면 선택된 오브젝트의 복사본을 배치할 수 있습니다.

오브젝트에 커스텀 피벗이 있다면, 그 피벗이 앵커 포인트로 사용됩니다. 아래 영상을 참고하세요.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) 트랜스폼 {#transform}
보통 다른 오브젝트 표면 위에서, 1~2 손가락으로 모델을 직접 이동/회전/스케일합니다.

도구는 왼쪽 툴바의 5개 버튼으로 제어합니다:

* `Snap` - 모델을 다른 표면에 스냅합니다.
* `Group` - 선택된 오브젝트가 오브젝트와 인스턴스의 조합일 때, 도구의 동작 방식을 결정합니다.
* `Move` - 한 손가락 드래그로 오브젝트를 이동합니다. Snap이 활성화된 경우, 손가락 아래 표면을 따라 오브젝트가 미끄러집니다.
* `Rotate` - 한 손가락 드래그로 오브젝트를 회전합니다. Snap이 활성화된 경우, 손가락 아래 표면의 노멀을 기준으로 회전합니다.
* `Scale` - 한 손가락 드래그로 오브젝트를 스케일합니다.

Transform은 두 손가락을 사용해 이들 모드 중 두 가지를 빠르게 사용할 수 있습니다:

* 오브젝트를 드래그해 배치합니다. 첫 번째 손가락을 화면에서 떼지 말고, 움직임만 멈춥니다.
* 첫 손가락을 유지한 채 두 번째 손가락을 화면에 댑니다. 두 번째 손가락을 드래그하면 오브젝트가 스케일됩니다.
* 두 번째 손가락을 떼고, 첫 손가락을 다시 드래그하면 오브젝트는 다시 Move 모드가 됩니다.

두 번째 손가락 탭 제스처로 두 번째 모드를 바꿀 수도 있습니다:

* 오브젝트를 드래그해 배치하고, 손가락을 떼지 않은 채 움직임만 멈춥니다.
* 첫 손가락을 유지한 채 두 번째 손가락으로 탭합니다.
* 도구가 회전 모드로 전환됩니다. 첫 손가락을 드래그해 회전을 설정합니다.
* 다시 두 번째 손가락으로 탭하면 도구가 Move 모드로 돌아옵니다.

이는 지형 위에 바위를 복제 배치하는 등, 다른 오브젝트 위에 오브젝트를 복제하는 빠른 워크플로를 제공합니다. Clone 버튼이 왼쪽 툴바에 있는 것도 이 때문입니다:

* Transform 도구로 바위를 한 개 배치합니다.
* 손을 떼고, Clone 버튼을 누릅니다.
* 이 바위를 이동하고, 필요하다면 회전/스케일합니다.
* 손을 떼고, Clone 버튼을 누릅니다.
* 이 바위를 이동하고, 반복합니다.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) 기즈모 {#gizmo}
이 도구는 오브젝트를 이동, 회전, 스케일하고, 오브젝트의 피벗을 변경할 수 있게 해줍니다.

뷰포트 핸들은 다음 기능을 갖습니다:

* `Move` - 선+화살표를 드래그해 X/Y/Z 방향으로 이동합니다. 기즈모 중앙의 살구색 점을 드래그해 화면 공간에서 자유롭게 이동합니다. 빨강/초록/파랑 사각형을 클릭해 X/Y/Z 평면에서 이동합니다.
* `Rotate` - 빨강/초록/파랑 원을 드래그해 X/Y/Z 축으로 회전합니다. 원 안의 구를 드래그해 자유 회전합니다.
* `Scale`- 바깥쪽 빨강/초록/파랑 점을 드래그해 X/Y/Z 방향으로 스케일합니다. 바깥쪽 빨강/초록/파랑 콘을 드래그해 X/Y/Z 평면에서 스케일합니다. 바깥쪽 살구색 원을 드래그해 균일 스케일합니다.

![](/images/tool_gizmo.webp)

#### 노드와 버텍스 {#nodes-and-vertices}

Nomad의 모든 오브젝트는 노드와 버텍스로 구성됩니다:

* `Node` - 오브젝트의 ‘핸들’로, 위치/회전/스케일(변환 행렬)을 저장합니다.
* `Vertices` - 오브젝트 표면을 정의하는 포인트로, 위치와 페인트 정보를 저장합니다.

8개의 버텍스로 이루어진 단순 박스가 있다면, 변환 행렬을 수정해 박스를 이동할 수도 있고, 버텍스 위치를 수정해 이동할 수도 있습니다. 조각할 때는 보통 버텍스를 수정하고, 기즈모로 오브젝트를 움직일 때는 보통 노드를 수정합니다. Nomad는 두 가지 모두를 지원합니다. 

#### 왼쪽 메뉴 툴바 {#left-menu-toolbar}

왼쪽 툴바는 기즈모가 노드 또는 버텍스 중 어느 쪽에 작동할지와 기타 기능을 제어합니다:

* `Clone` - 현재 오브젝트의 독립 복사본을 만들고, 기즈모로 드래그해 이동할 수 있습니다.
* `Instance` - 현재 오브젝트의 인스턴스 복사본을 만듭니다. 오브젝트들이 연결되어, 한 오브젝트에서 조각한 변경 사항이 모든 인스턴스에 반영됩니다.
* `Group/Object/Vertex/Auto` - 기즈모가 오브젝트의 노드 또는 버텍스에 작동할지 설정합니다. 기본 'Auto' 모드는 최선의 추측을 시도합니다. 여러 오브젝트가 계층 구조로 부모-자식 관계일 때, 'Object' 는 현재 오브젝트만 이동시키고 자식 오브젝트는 그대로 둡니다. 기즈모는 마스크와 대칭도 고려할 수 있습니다.
* `Pin` - 기본적으로 기즈모는 선택된 오브젝트의 피벗으로 이동합니다. Pin이 활성화되면, 기즈모는 현재 위치에 고정됩니다.
* `Align` - 피벗을 현재 오브젝트에 정렬할지, 월드에 정렬할지 토글합니다.
* `Snap rotation` - 회전 값을 일정 간격으로 스냅합니다. 스냅 값은 스냅이 활성일 때 표시되며 편집할 수 있습니다.
* `Snap translation` - 이동 값을 일정 간격으로 스냅합니다. 스냅 값은 스냅이 활성일 때 표시되며 편집할 수 있습니다.
* `Pivot` - 활성화 시, 오브젝트를 움직이지 않고 기즈모만 이동/회전할 수 있습니다. 아래에서 설명하는 추가 메뉴가 있습니다.

#### 피벗 {#pivot}
Pivot 모드가 활성화되면, 빠른 피벗 변경을 위한 메뉴가 표시됩니다:

**Reset** 
* `Center` - 피벗을 오브젝트 중심으로 이동합니다.
* `Bottom` - 피벗을 오브젝트 바닥으로 이동합니다.
* `Align` - 회전을 리셋해 월드에 정렬합니다.
* `Mask` - 피벗을 비마스크 영역의 중심으로 이동합니다.

**On Tap**
* `None` - 오브젝트를 탭해도 아무 동작도 하지 않습니다.
* `Normal` - 표면을 탭한 위치로 피벗을 이동하고, 그 표면에 정렬되도록 회전합니다.
* `First` - 표면을 탭한 위치로 피벗을 이동하지만, 회전은 변경하지 않습니다.
* `Medial` - 탭한 표면 아래 오브젝트의 중간 지점으로 피벗을 이동합니다.

#### 기즈모 설정 {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### 매트릭스 {#matrix}
* ![](/icons/target.webp) `Move origin` - 오브젝트의 피벗이 씬의 중심(원점)에 오도록 오브젝트를 이동합니다.
* ![](/icons/bake.webp)  `Bake` - 현재 위치에서 오브젝트를 고정하고, 이동/회전 값을 0, 스케일을 1로 설정합니다.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - 기즈모 핸들이 월드에서 위치한 곳에 맞춰 행렬 값을 설정합니다.
* ![](/icons/reset.webp) `Reset` - 이동 값을 0, 회전 값을 0, 스케일을 1로 설정하는 바로가기이며, 오브젝트를 이동/회전시킵니다.

::: tip Bake vs Bake Pivot
박스를 하나 만들고, Gizmo 도구를 선택한 뒤 설정 메뉴를 열어 고정(pin)하세요. 기본적으로 이동/회전은 0, 스케일은 1입니다.

Pivot 모드를 활성화하고 핸들을 한쪽으로 옮긴 뒤, Pivot 모드를 끕니다. 피벗은 바뀌었지만, 이동 값은 여전히 0입니다. 

피벗이 *실제로* 어디 있는지 보고 싶다면 `Bake Pivot` 을 클릭하세요. 이제 이동 값이 업데이트됩니다. 이 작업 동안 박스는 움직이지 않고, Pivot 모드에서도 마찬가지입니다.

박스를 이동/회전시킨 뒤 `Move Origin` 을 탭하면, 피벗이 월드 중심에 오도록 오브젝트가 이동하지만, 회전은 그대로 유지됩니다.

`Reset` 을 클릭하면 회전도 0으로 설정됩니다.

박스를 다시 이동/회전시키고 이번에는 `Bake` 를 클릭하세요. 피벗과 박스는 그대로 있지만, 이동/회전 값은 0으로 설정됩니다.

이 과정을 몇 번 연습해 보세요! 피벗 값은 숨겨져 있고 Nomad가 이를 관리하지만, 피벗을 실제 공간상의 위치에 맞추고 싶을 때는 Bake Pivot이 그 역할을 한다는 점을 이해하는 것이 중요합니다.

:::

* `Translation` - X, Y, Z 이동 값
* `Rotation` - X, Y, Z 회전 값
* `Scale` - 균일 스케일이 활성일 때는 하나의 값, 비활성일 때는 X, Y, Z 스케일 값
* `Uniform scale` - 균일 스케일과 축별 스케일을 토글합니다.

-----

* `Compact` - 기즈모 레이아웃을 토글해 추가 핸들을 회전 구 바깥/안쪽에 배치합니다.
* `Widget size` - 기즈모 크기
* `Thickness` - 기즈모 선 두께
* `Opacity` - 기즈모 불투명도
* `Hide on interaction` - 드래그 중 기즈모를 일시적으로 숨길지 토글합니다.

-----

* `Tangent roll threshold` - X/Y/Z 회전 원을 드래그할 때 회전 UI 동작을 제어합니다. 값이 0이면 다이얼처럼 기즈모를 원형으로 드래그해 회전합니다. 값이 90이면 요요 줄을 당기듯, 처음 클릭한 지점을 향해 직선으로 드래그해 회전합니다. 0~90 사이 값에서는 두 동작이 혼합됩니다. 값보다 작은 각도에서는 직선 드래그, 그 이상에서는 원형 드래그가 적용됩니다.
* `Numerical input` - 활성화 시, 기즈모를 한 번 탭하면 해당 축에 정확한 값을 입력할 수 있는 창이 나타납니다.

::: warning
[Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate), [Scale](#scale) 는 각자 고유한 대칭 체크박스를 사용합니다!

기본적으로 이 대칭은 꺼져 있습니다.
:::

왼쪽에서는 기즈모 피벗을 이동할 수 있으며, 아래 영상에서 실제 동작을 볼 수 있습니다.
이는 특히 회전에 유용하며, 이동에는 영향을 주지 않습니다.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) 페이스 그룹 {#facegroup}

Facegroup은 오브젝트를 서로 다른 색상의 면으로 구성해 정리할 수 있게 해줍니다. Nomad에서 Facegroup은 여러 방식으로 사용할 수 있습니다:

* 마스크를 위한 빠른 선택 방법
* 오브젝트의 일부를 숨기거나 표시
* 오브젝트를 여러 파트로 나누지 않고도 구조화
* UV 영역 정의
* Quad Remesher 가이드
* Smooth 같은 도구에 추가 제어 제공

#### 페이스 그룹 왼쪽 툴바 {#facegroup-left-toolbar}

* `Patch ` - 사용 가능한 Facegroup을 패치로 표시합니다. 사용하지 않는 패치는 삭제할 수 있습니다. 패치를 탭해 이름을 바꾸거나 색을 변경합니다. 플러스 아이콘으로 새 패치를 생성합니다.
* `Dot` - 오브젝트 위를 칠해 Facegroup을 정의합니다. '+ Face Group' 이 활성화되어 있으면, 매 스트로크마다 자동으로 새 Facegroup이 생성되어 영역을 빠르게 정의할 수 있습니다. 탭하면 선택된 영역을 플러드 필합니다. 슬라이더는 점의 반경을 설정합니다.
* `Relax` - Facegroup 경계를 부드럽게 합니다. Quad Remeshing을 위한 깔끔한 엣지 정의나 하드 서피스 모델링용 패널 정의에 매우 유용합니다. 슬라이더는 Relax 연산의 반경과 강도를 제어합니다.
* `Shape selector` - 브러시 대신 `Lock+Radius`, `Lasso`, `Polygon`, `Rect`, `Ellipse` 를 사용해 셰이프로 Facegroup을 만듭니다. 자세한 내용은 [Shape Selector](#shape-selector)를 참고하세요.
* `Auto-pick` - 활성화 시, 스트로크가 시작되는 지점의 패치를 자동으로 선택해 스트로크 전체에 적용합니다. Facegroup 영역을 정리할 때 매우 유용합니다. Facegroup이 너무 멀리 확장되었다면 Auto-pick을 켜고, 패치가 올바른 영역에서 스트로크를 시작해 경계까지 드래그해 올바른 패치로 재할당할 수 있습니다.

### ![](/icons/tool_hide.webp) 숨기기 {#hide}
오브젝트의 일부를 숨기거나 고립시킵니다. 

주요 모드는 왼쪽 메뉴에서 제어합니다:

* `Dot` - 오브젝트 위를 브러시로 칠해 일부를 숨깁니다.
* `Shape selector` - 브러시 대신 `Lasso`, `Polygon`, `Line`, `Rect`, `Ellipse` 를 사용해 셰이프로 숨깁니다. 자세한 내용은 [Shape Selector](#shape-selector)를 참고하세요.
* `Show` - 동작을 반전해, 선택된 모드가 오브젝트 일부를 숨기는 대신 표시하도록 합니다.

뷰포트 상단에 추가 컨트롤이 있는 툴바가 나타납니다:

* `Clear` - 오브젝트를 복원해, 숨겨진 모든 부분을 다시 표시합니다.
* `Invert` - 숨겨진 부분과 표시된 부분을 서로 바꿉니다.
* `Facegroup` - Facegroup을 사용해 빠르게 영역을 숨깁니다. Facegroup을 탭하면 해당 그룹 전체가 숨겨집니다.
* `Mask` - 마스크가 활성 상태라면, 이 버튼을 탭해 마스크된 영역을 숨깁니다.
* `Delete` - 숨겨진 부분을 삭제합니다.
* `Split` - 숨겨진 부분을 새 형태로 분리합니다.

### ![](/icons/tool_measure.webp) 측정 {#measure}
두 점 사이의 거리를 측정하려면 드래그합니다.

### ![](/icons/tool_remesh.webp) 쿼드 리메셔 {#quad-remesher}

![](/images/tool_quadremesher.webp)

이 도구는 선택된 오브젝트를 밀도, 엣지 흐름, 대칭을 제어할 수 있는 깔끔한 쿼드 토폴로지로 변환합니다. 

::: tip
Quad Remesher는 iOS 및 데스크톱용으로 [Exoside](https://exoside.com/) 에서 개발했습니다. 

iOS에서는 Nomad 내 인앱 구매로 제공되며, 1회 결제 금액은 16달러(USD)입니다.

데스크톱에서는 [Exoside](https://exoside.com/quadremesher/quadremesher-buy/) 에서 라이선스를 구매하세요. Nomad 데스크톱 전용 또는 지원되는 모든 데스크톱 앱용 크로스 라이선스를 구매할 수 있습니다.

이미 다른 데스크톱 앱용 Quad Remesher를 보유하고 있다면, [더 낮은 비용으로 모든 플랫폼용 업그레이드를 구매](https://exoside.com/quadremesher/quadremesher-upgrade/) 할 수 있습니다.

Quad Remesher는 Android에서는 사용할 수 없습니다. Android에서는 Topology -> Misc 메뉴 아래에 있는 무료 오픈소스 'Quad Remesh - Instant' 를 사용할 수 있지만, 기능 세트가 매우 제한적이라는 점을 이해해야 합니다.
:::

When this tool is activated for the first time, it will ask if you want to enable it as an in-app purchase. Once active, the left and top toolbars will be enabled.

* `Dot` - 이 브러시는 목표 밀도를 설정합니다. 강도가 100%일 때는 빨간색으로 칠해지며, 해당 영역에서 목표 쿼드 밀도의 두 배를 사용합니다. 강도가 0%일 때는 청록색으로 칠해지며, 해당 영역에서 목표 쿼드 밀도의 절반을 사용합니다. 강도가 50%일 때는 회색으로 칠해지며, 기본 목표 쿼드 밀도를 사용합니다.
* `Smooth` - 빨간색/회색/청록색 밀도 전환을 부드럽게 만듭니다.
* `Curve` - 스컬프트 표면 위에 곡선을 스케치합니다. 쿼드 리메셔는 이를 엣지 플로우의 가이드로 사용합니다. 곡선을 탭하면 삭제됩니다.
* `Path` - 스컬프트 표면 위에 경로를 그립니다. 쿼드 리메셔는 이를 엣지 플로우의 가이드로 사용합니다. 경로를 탭하면 삭제됩니다. 
* `Rect` - 스컬프트 표면 위에 사각형을 그립니다. 쿼드 리메셔는 이를 엣지 플로우의 가이드로 사용합니다. 경로를 탭하면 삭제됩니다.
* `Ellipse` - 스컬프트 표면 위에 타원을 그립니다. 쿼드 리메셔는 이를 엣지 플로우의 가이드로 사용합니다. 경로를 탭하면 삭제됩니다.

#### 쿼드 리메셔 상단 툴바 {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

뷰포트 상단에 추가 컨트롤이 있는 툴바가 나타납니다:


* `<Count>` - 클릭하면 쿼드 리메셔 프로세스를 시작합니다. 이 숫자는 목표 쿼드 리메시 개수를 나타냅니다.
* `Quads` - 좌우로 슬라이드하여 목표 쿼드 개수를 설정하거나, 탭하여 정확한 숫자를 입력합니다. 이는 고정값이라기보다는 가이드에 가깝다는 점에 유의하세요. 쿼드 리메셔의 다양한 설정으로 인해 결과가 이 목표와 정확히 일치하지 않을 수 있습니다.
* `Half` - 현재 폴리곤 개수의 절반을 목표 개수로 설정하는 바로가기입니다.
* `Same` - 현재 폴리곤 개수를 목표 개수로 설정하는 바로가기입니다.
* `Guides` - 전체 가이드 개수를 표시하거나, 탭하여 모든 가이드를 삭제합니다.
* `Density X` - 탭하여 모든 밀도 페인팅을 제거합니다.
* `Density (painting)` - 밀도 페인팅을 사용할지 무시할지 토글합니다.
* `Face Group` - 페이스 그룹을 사용하여 쿼드 리메셔를 유도할지 여부를 토글합니다.
* `Relax` - 쿼드 리메싱 중 페이스 그룹 경계를 자동으로 릴랙스할지 토글합니다. 이미 페이스 그룹 경계를 릴랙스/스무딩했다면 이 옵션을 비활성화하세요.
* `Relax Slider` - 페이스 그룹 경계를 릴랙스하기 위한 바로가기 슬라이더입니다.
* `Hard Edges` - 하드 엣지를 유지하려고 시도할지 토글합니다.
* `Reproject Vertex` - 새 레이아웃을 입력 메시에 다시 투영할지 토글합니다.
* `Symmetry` - 대칭 결과를 활성화할지 토글합니다. 대칭은 항상 월드 X축을 기준으로 계산되므로, 대칭 결과를 기대한다면 모델이 원점에 위치하도록 하세요.
* `...` - 쿼드 리메셔 설정 메뉴입니다. 

#### 쿼드 리메셔 설정 메뉴 {#quad-remesher-settings-menu}

이 설정 대부분은 상단 툴바에서도 사용할 수 있습니다.

* `<Count>, Half, Same` - 상단 툴바의 Remesh, Half, Same 버튼과 동일합니다.
* `Target Quads` - 상단 툴바의 `Quads` 버튼과 동일합니다.
* `Adaptive quad count` - 곡률이 높은 영역에는 더 작은 쿼드를, 곡률이 낮은 영역에는 더 큰 쿼드를 사용하도록 토글합니다.
* `Adaptive size` - 적응 정도를 설정합니다. 100%에서는 최대한의 적응 크기를 허용하며, 0%에서는 쿼드가 균일해집니다.
* `Auto-Detect Hard Edges` - 날카로운 표면을 더 잘 따르도록 쿼드 리메시 레이아웃을 조정할지 토글합니다.
* `Density (painting)` - 상단 툴바의 `Density (painting)` 버튼과 동일합니다.
* `Reproject Vertex` - 새 레이아웃을 입력 메시에 다시 투영할지 토글합니다.
* `Face Group` - 상단 툴바의 `Face Group` 버튼과 동일합니다.
* `Relax Slider` - 페이스 그룹 경계를 릴랙스하기 위한 바로가기 슬라이더입니다.

::: tip

아티팩트를 최소화하면서 좋은 쿼드 리메시를 얻기 위한 레시피:

* 원하는 이상적인 쿼드 플로우를 정의하기 위해 메시에 페이스 그룹을 지정합니다.
* 페이스 그룹 릴랙스를 사용해 페이스 그룹 경계를 부드럽게 만듭니다.
* 디시메이트를 수행합니다. 이렇게 하면 페이스 그룹 가장자리에 얇거나 왜곡된 폴리곤이 없도록 보장할 수 있습니다. 디시메이트 설정에서 페이스 그룹 옵션이 활성화되어 있는지 확인하세요. 이렇게 하면 삼각형 엣지가 페이스 그룹 엣지를 정확히 따르게 됩니다. 

쿼드 리메시 옵션에서 릴랙스는 이미 메쉬를 릴랙스했으므로 비활성화하고 실행하면 좋은 결과를 얻을 수 있습니다.

:::

### ![](/icons/tool_select.webp) 선택 {#select}
도형 모드를 사용해 씬의 오브젝트를 선택합니다. `Unselect`는 선택에서 오브젝트를 제거합니다.

### ![](/icons/tool_view.webp) 뷰 {#view}
이 "툴"은 특별히 아무 작업도 하지 않으며, 단지 씬을 수정하지 않고 모델을 보기 위한 용도입니다.


## 툴박스 컨텍스트 메뉴 {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

툴박스에서 도구를 오른쪽 클릭하거나 길게 누르면 컨텍스트 메뉴가 나타납니다. 이 메뉴에는 다음 옵션이 있습니다:

* `Save` - 도구에 가한 변경 사항을 저장합니다.
* `Clone` - 도구를 복제하여 새 도구 바로가기를 만듭니다.
* `Last save` - 이전에 저장된 도구 버전으로 되돌립니다.
* `Icon` - 도구의 아이콘을 변경합니다.
* `Reset` - 도구를 기본값으로 초기화합니다.