# ![](/icons/material.webp) 머티리얼 {#material}

이 메뉴에서는 현재 오브젝트의 머티리얼을 변경하고, 오브젝트/머티리얼의 렌더 속성을 조정하며, 머티리얼에 텍스처를 할당할 수 있습니다.

![](/images/material_overview.webp)

머티리얼은 오브젝트가 빛과 다른 오브젝트에 어떻게 반응하는지를 제어하여, 오브젝트의 외형을 정의합니다. 오브젝트의 외형은 다음 속성들에 의해 제어됩니다:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

이 속성들을 조합하면 포토리얼리스틱부터 카툰풍, 실험적인 스타일까지 매우 다양한 결과를 얻을 수 있습니다.

Color, roughness, metalness, opacity는 페인팅할 수 있습니다. 자세한 내용은 [Vertex Paint options](painting.md)을 참고하세요.

Material type, reflectance, emissive/unlit은 아래에서 설명하는 머티리얼 속성입니다.

이 메뉴 상단의 복사/붙여넣기 버튼을 사용하면 한 오브젝트의 머티리얼을 다른 오브젝트로 복사할 수 있습니다.

Nomad의 렌더러는 실시간 렌더러입니다. 강력하지만, 특정 효과에 대해서는 정확도보다 속도를 우선합니다. 

## 머티리얼 종류 {#material-types}

![](/images/material_types.webp)

Nomad의 머티리얼 타입은 Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher입니다.

### ![](/icons/material_opaque.webp) 불투명 {#opaque}
기본 모드로, 표면을 단순한 머티리얼로 취급하며, 색상, 러프니스, 메탈니스, 불투명도(Opacity) 페인팅을 지원합니다.

### ![](/icons/material_subsurface.webp) 서브서피스 {#subsurface}
피부, 왁스, 비취(jade)처럼 내부에서 빛이 퍼지고 산란되는 재질을 시뮬레이션할 수 있는 모드입니다.

최상의 결과를 얻으려면 PBR 셰이딩 모드로 전환하고, 최소 하나의 디렉셔널 라이트 또는 스포트라이트를 사용하며, 가능하면 환경광은 어둡게 설정하세요.

`Depth`는 빛이 전면에서 내부로 스며들었다가 다시 전면 표면으로 나올 때까지 얼마나 멀리 산란되는지를 제어합니다. 이는 강한 그림자를 부드럽게 하고, 표면 디테일을 블러 처리하는 효과를 줍니다.

`Translucency`는 잎 뒷면을 통과하는 빛이나, 귀가 강하게 역광을 받을 때처럼, 전면에서 후면으로 빛이 얼마나 산란되는지를 제어합니다. 

### ![](/icons/material_blending.webp) 블렌딩 {#blending}

Opaque와 비슷하지만, 머티리얼이 불투명과 투명 사이를 섞을 수 있도록 하는 opacity 슬라이더를 지원합니다. Opaque 머티리얼이 페인팅 가능한 opacity를 지원하는 것과 달리, 이 모드는 단일 슬라이더로 opacity를 제어합니다. 

::: warning
Blending 모드는 복잡하거나 서로 교차하는 형태에서 깜빡임(flickering)이나 튐(popping) 현상을 유발할 수 있습니다.
:::

### ![](/icons/material_additive.webp) 가산 {#additive}
이 머티리얼을 사용하면 메시를 반투명하게 만들 수 있습니다. Blending 머티리얼과 비슷하지만, Blending이 주변과 색을 섞는 반면, Additive는 항상 뒤에 있는 오브젝트보다 더 밝게 표현됩니다. 빛줄기, 불꽃, 폭발 같은 밝은 효과에 적합합니다.

Opacity 값을 1보다 크게 설정할 수 있으며, 이 경우 오브젝트는 더 밝게 보입니다.  
이는 [bloom](postprocess.md#bloom)과 `threshold parameter`를 사용하여, 이 오브젝트만 발광(emissive) 오브젝트처럼 빛나게 만들고 싶을 때 유용합니다.

이 모드는 [Blending](#blending)보다 아티팩트가 적은 경향이 있습니다(순서에 독립적인 투명도).

### ![](/icons/material_refraction.webp) 굴절 {#refraction}
이 모드는 유리(glass) 재질을 시뮬레이션하는 데 사용할 수 있습니다. 실시간 렌더링 제약으로 인해, 자기 굴절(self-refraction)과 다중 레이어 굴절은 다소 제한적입니다.

모델에 페인팅된 러프니스는 굴절이 얼마나 흐릿하게 보이는지에 영향을 줍니다.  
기본적으로 Nomad에서 생성된 모든 오브젝트는 약 25% 정도의 러프니스를 가지므로, 굴절은 완전히 선명하지 않고 약간 흐릿하게 보입니다.  
`paint glossy` 버튼을 사용하면 색상에는 영향을 주지 않고, 러프니스와 메탈니스를 0으로 다시 페인팅할 수 있습니다.

여기에는 두 가지 서로 다른 러프니스가 작용합니다. 하나는 표면에서 반사의 흐릿함을 제어하고, 다른 하나는 내부(굴절)의 흐릿함을 제어합니다.  
하지만 Nomad에는 페인팅용 러프니스 채널이 하나뿐이므로, 내부와 외부 러프니스는 같은 값을 공유합니다.  
막대사탕처럼 표면은 날카롭고 내부는 흐릿한 효과를 원한다면, `Surface glossiness`와 `Interior roughness` 슬라이더를 사용해 페인팅된 러프니스를 덮어쓸 수 있습니다.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) 디더링 {#dithering}
일부 픽셀을 무작위로 버리는 방식으로 오브젝트를 반투명하게 만듭니다.

### ![](/icons/material_shadow_catcher.webp) 그림자 수집기 {#shadow-catcher}

오브젝트를 보이지 않게 만들고, 그림자만 받도록 합니다. Nomad 렌더를 다른 이미지와 합성할 때 유용합니다. 

::: tip

투명도와 블렌딩 모드에 대한 추가 정보는 https://support.fab.com/s/article/Transparency-Opacity 에서 확인할 수 있습니다.

:::

## 컨트롤 {#controls}

![](/images/material_controls.webp)

### 항상 언릿 {#always-unlit}
활성화하면 오브젝트는 PBR과 Matcap을 무시하고, 셰이딩 없이 페인팅된 색상만 표시합니다.  
[Additive](#additive)를 사용하는 경우, 검은색으로 페인팅하여 직접 투명도를 표현할 수 있습니다.

### 불투명도 {#opacity}
오브젝트가 얼마나 단단하거나 불투명하게 보일지를 제어합니다. 100%는 완전 불투명, 0%는 완전 투명입니다. 더 세밀한 제어를 위해 opacity를 페인팅할 수도 있습니다.

### 반사율 {#reflectance}
비금속 머티리얼이 받는 반사의 양을 제어합니다. 대부분의 경우 기본값을 사용하는 것이 좋으며(법선 방향에서 약 4%의 빛을 반사하는 표준값에 해당), 예를 들어 캐릭터의 눈에 반사와 하이라이트를 강조하고 싶을 때 값을 높일 수 있습니다.

### 역 컬링 {#inverse-culling}
표면의 노멀 방향을 반전합니다. 일반적으로 필요하지 않지만, 모델이 안팎이 뒤집혀 보이거나, `Two sided`를 비활성화한 상태와 조합하여 카메라에 가장 가까운 벽이 항상 숨겨지는 실내 공간을 만들 때 사용할 수 있습니다.

### 스무스 셰이딩 {#smooth-shading}
[글로벌 옵션](settings.md#smooth-shading)을 참고하세요.  
`Auto` 값은 글로벌 옵션을 사용합니다.

### 양면 {#two-sided}
[글로벌 옵션](settings.md#two-sided)을 참고하세요.  
`Auto` 값은 글로벌 옵션을 사용합니다.

### 색상 백페이스 {#coloured-backface}
[글로벌 옵션](settings#two-sided)을 참고하세요.  
`Auto` 값은 글로벌 옵션을 사용합니다.

### 그림자 생성 {#casts-shadows}
현재 `Auto`는 `On`과 동일합니다.  
투명 오브젝트도 그림자를 투사하며(블렌딩된 그림자를 흉내 내기 위해 디더링 패턴 사용),  
예를 들어 큰 바닥처럼, 장면에 크지만 그림자를 투사할 필요가 없는 오브젝트가 있다면 그림자 투사를 비활성화하는 것이 좋습니다.

### 그림자 수신 {#recieve-shadows}
현재 `Auto`는 `On`과 동일합니다.

### 와이어프레임 {#wireframe}
[글로벌 옵션](settings.md#wireframe)을 참고하세요.  
`Auto` 값은 글로벌 옵션을 사용합니다.


## 텍스처 {#textures}

![](/images/material_textures.webp)

오브젝트에 UV가 있다면, 버텍스 color/roughness/metalness/opacity에 더해 텍스처를 머티리얼에 적용할 수 있습니다. 일반적으로 이는 텍스처 베이크 결과이지만, Nomad 외부에서 제작된 이미지를 사용할 수도 있습니다.

텍스처는 다음에 적용할 수 있습니다:

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

텍스처 슬롯을 클릭하면 선택 창이 나타납니다. 머티리얼 슬롯에 텍스처를 할당한 후 다시 클릭하면 텍스처 패널이 열립니다:

### 텍스처 패널 옵션 {#texture-panel-options}

![](/images/material_texture_panel.webp)

### 열기 {#open}
다른 텍스처를 선택합니다.

### 없음 {#none}
텍스처를 제거합니다.

### 불투명도 {#texture-opacity}

이미지에 알파 채널이 있는 경우, 이를 Opacity에 사용할지 무시할지를 선택할 수 있습니다.

### ![](/icons/link.webp) 체인/링크 아이콘 {#chainlink-icon}

아래 섹션들에서 링크 아이콘을 활성화하면, 해당 옵션 설정이 링크 아이콘이 활성화된 다른 텍스처들(color, normal, roughness, metalness, opacity, emissive)과 공유됩니다. 

이를 통해 정렬된 텍스처들을 사용할 때, 파라미터나 프로젝션 타입을 변경하더라도 서로 계속 정렬된 상태를 유지할 수 있습니다.


### 프로젝션 {#projection}
![](/images/material_projection.webp)

텍스처를 오브젝트에 어떻게 적용할지 설정합니다.

* `Auto` - 오브젝트에 UV가 있으면 UV, 없으면 Triplanar
* `UV` - 메시의 UV 좌표를 사용해 텍스처를 적용합니다. 메시와 텍스처가 Nomad 외부에서 왔거나, Nomad에서 내보내 다른 곳에서 사용할 예정이라면 UV가 올바른 선택입니다.
* `Triplanar` - X, Y, Z 축 방향으로 텍스처를 투영하고, 이음새를 블렌딩합니다. 

### 트라이플래너 {#triplanar}
![](/images/material_triplanar.webp)

Triplanar 프로젝션은 텍스처를 오브젝트에 적용하는 강력하면서도 간단한 방법입니다.

Triplanar는 같은 이미지를 가진 6개의 프로젝터가 오브젝트의 앞, 뒤, 왼쪽, 오른쪽, 위, 아래에서 비추는 것과 같습니다.

필요하다면 이를 UV나 버텍스 컬러로 베이크할 수 있습니다.


![](/images/material_triplanar_example.webp)

#### 방식 {#method}

* `Local` - 프로젝션이 오브젝트의 트랜스폼과 함께 이동합니다.
* `World` - 프로젝션은 고정되고, 오브젝트를 움직이면 오브젝트가 프로젝션을 가로질러 미끄러지듯 이동합니다.

#### 경도 {#hardness}

프로젝션들이 어떻게 섞이는지를 제어합니다. 100%는 블렌딩을 하지 않아 프로젝션 경계가 날카롭게 보입니다. 0%는 넓은 각도에 걸쳐 경계를 블렌딩합니다. 기본값은 90%로, 경계를 숨기기에 충분한 블렌딩을 하면서 나머지 영역은 선명하게 유지합니다.

### 유니폼 {#uniform}

체크하면 모든 프로젝션에 동일한 hardness가 사용됩니다. 체크를 해제하면 X, Y, Z 프로젝션 각각에 대한 추가 hardness 컨트롤이 표시됩니다.


### 파라미터 {#parameter}
![](/images/material_parameter.webp)

#### 필터링 {#filtering}
텍스처 필터링 방식을 설정합니다. 기본값은 `Auto`이며, 사용 가능한 방식은 `Nearest`, `Linear`, `Mipmap`입니다. Nearest는 필터링을 하지 않아, 가까이에서 볼 때 텍스처에 톱니 모양 아티팩트가 생길 수 있습니다. Linear와 Mipmap은 더 나은 필터링을 제공하여, 가까이에서 볼 때 텍스처가 톱니 모양 대신 블러 처리된 것처럼 보입니다.

#### 타일링-X {#tiling-x}
Scale 파라미터가 1보다 커서 텍스처가 오브젝트 UV보다 작아질 때, X축 방향으로 텍스처를 어떻게 타일링할지 설정합니다. `None`은 반복 없음, `Repeat`는 텍스처를 복제하여 반복, `Mirror`는 텍스처를 복제하되, 두 번째마다 좌우 반전하여 타일링 아티팩트를 줄이는 데 도움이 됩니다.

#### 타일링-Y {#tiling-y}
Tiling-X와 동일하지만 Y축 방향에 적용됩니다.

### 트랜스폼 {#transform}
![](/images/material_transform.webp)

UV 공간에서 텍스처에 적용되는 추가 2D 변환입니다. 리셋 버튼은 기본값으로 되돌리고, (color 이외의 텍스처가 선택된 경우) 체인 아이콘은 color 텍스처와 동일한 Transform을 링크/언링크합니다.

#### 이동 {#translation}
텍스처의 X, Y 오프셋입니다.

#### 회전 {#rotation}
텍스처의 회전입니다.

#### 스케일 {#scale}
텍스처의 스케일입니다. 값이 클수록 오브젝트 위에서 텍스처가 더 작게 보입니다. Tiling-X와 Tiling-Y 슬라이더를 사용해 그때의 동작을 제어합니다.

### 균일 스케일 {#uniform-scale}
비활성화하면 Nomad는 Scale-X와 Scale-Y에 대한 개별 컨트롤을 표시합니다.