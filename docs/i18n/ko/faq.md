# ![](/icons/faq.webp) 자주 묻는 질문 {#faq}

[[toc]]

## 플랫폼 {#platform}
### 내 기기는 프로젝트 파일을 어디에 저장하나요? {#locate}
프로젝트는 메인 Nomad 폴더 안의 `projects` 폴더에 저장됩니다.

iOS에서는 iOS 파일 앱을 통해 Nomad 폴더에 접근할 수 있습니다.

Android에서는 Nomad 폴더가 `Android/data/com.stephaneginier.nomad/files/` 에 있습니다.  
최근 Android 버전(10/11)에서는 더 이상 `Android/data` 폴더에 접근할 수 없습니다.  
예를 들어 [이 앱](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) 같은 별도의 앱을 통해 접근할 수 있습니다.
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### 베타 테스트를 할 수 있는 방법이 있나요? {#beta}
Windows & MacOS의 경우, 베타 버전이 [홈페이지](https://nomadsculpt.com)에 올라올 때가 있습니다.
<br>
iOS의 경우 비공개 TestFlight가 있으며, [Discord](https://discord.com/invite/8h7BwpRz29)의 #beta-ios 채널을 방문하세요.
<br>
[웹 데모](https://nomadsculpt.com/demo)는 보통 최신 기능들로 업데이트됩니다.

### 왜 안드로이드에는 무료 체험이 있고 iOS에는 없나요? {#android-trial}
오래된 Android 기기들(그리고 일부 최신 기기들도...)의 성능이 좋지 않아서, 사람들이 앱을 구매했는데 검은 화면만 보게 되는 상황을 피하고 싶었습니다.  
하지만 주된 이유는, 유료 Android 앱이 그다지 일반적이지 않다고 느꼈기 때문입니다.

### Nomad를 실행하기에 가장 좋은 태블릿은 무엇인가요? {#best-tablet}

요약: iPad.

조금 더 긴 답은 다음과 같습니다.

> "당신이 감당할 수 있는 _가장 최신 iPad_ 가 최선입니다. 애플이 정말 싫다면, 당신이 감당할 수 있는 가장 최신 삼성 태블릿. 그 외의 것은, 먼저 테스트해 보세요."

사람들은 항상 더 많은 정보를 원하므로, 요약을 덧붙입니다.

Nomad는 최신 iPad에서 가장 잘 동작합니다:

* iPad와 iPhone은 [Exoside](https://exoside.com/)의 [Quad Remesher](tools#quad-remesher) 플러그인에 접근할 수 있습니다.
* 최신 펜슬을 지원하는 최근 iPad는 [배럴 롤](https://www.youtube.com/watch?v=XcDQazDYpo0)을 지원하며, Nomad의 특정 도구에서 펜슬을 비틀어 사용할 수 있습니다.
* 최신 M 시리즈 칩의 성능은 매우 빠릅니다.

가장 비싼 최신 iPad는 최종 이미지를 매우 빠르게 렌더링할 수 있고, 매우 높은 디테일로 스컬핑할 수 있게 해줍니다.

하지만 더 저렴하고 오래된 iPad에서의 성능 저하는 사람들이 예상하는 것만큼 심하지 않습니다. Apple Pencil을 지원하는 모든 iPad는 Nomad를 꽤 잘 실행합니다. 예를 들어:

* 2023년형 iPad Pro는 500만 폴리 스컬프를 반응성 있게 다룰 수 있고, 최종 품질 이미지를 5초 안에 렌더링할 수 있습니다.
* 2015년형 iPad Pro는 약간의 랙이 있지만 120만 폴리 오브젝트를 다룰 수 있고, 최종 품질 이미지를 20초 안에 렌더링할 수 있습니다.

성능 차이는 크지만, 가격도 고려해야 합니다:

* 2025년형 iPad Pro는 모든 옵션을 포함하면 새 제품 기준 *2500달러(USD)* 입니다.
* 2023년형 iPad Pro는 현재 eBay에서 *400달러(USD)* 정도입니다.
* 2015년형 iPad Pro는 eBay에서 *250달러(USD)* 정도입니다.

추가 400만 폴리와 15초 절약이 2100달러의 가치가 있는지는 본인 선택입니다.

Pro가 아닌 모델은 더 저렴하면서도 다양한 크기와 성능을 제공합니다. 현재 iPad Air는 2세대 펜슬과 배럴 롤을 지원하며, Pro보다 상당히 저렴합니다. 중고 및 리퍼비시 시장까지 포함하면 선택지는 더 많아집니다.  

즉, 예산이 얼마이든 자신에게 맞는 iPad를 찾을 수 있을 것입니다. 그리고 대부분의 스컬프는 수백만 폴리가 아니라는 점을 기억하세요! 50만 폴리 이하로 유지할 수 있다면, 오래된 iPad에서도 빠르게 스컬핑할 수 있습니다.

`Android는 어떤가요?`

Android의 그래픽 성능은 iPad보다 낮습니다. Nomad 개발자에 따르면, "Samsung Galaxy Tab S9는 iPad Air보다 Nomad를 한 자릿수 정도(10배 수준) 느리게 실행합니다." 그럼에도 많은 사용자가 삼성 태블릿에 만족하고 있으며, 대부분의 스컬핑 작업에서 Nomad는 잘 동작합니다.  

다른 Android 태블릿의 경우 주의가 필요합니다. Android 하드웨어는 성능 편차가 매우 크기 때문에, Nomad가 어떻게 동작할지 예측하기 어렵습니다.

먼저 저장 불가 무료 버전의 Nomad로 꼭 테스트해 보세요. 

`메모리와 저장 용량은 어떤가요?`

대부분의 Nomad 파일은 100MB 이하입니다. 즉, 요즘 판매되는 거의 모든 태블릿(iPad든 Android든)은 Nomad 프로젝트를 저장하기에 충분한 공간을 가지고 있습니다.

### 한 기기에서 Nomad를 샀는데, 다른 기기에서도 사용할 수 있나요? {#multi-devices}
같은 앱 스토어와 같은 계정을 사용한다면 가능합니다.

예를 들어 iOS 앱 스토어에서 구매했다면, 다른 iOS 기기에서도 사용할 수 있습니다.

Android 태블릿에서 Google Play를 통해 구매했다면, 다른 Android 기기에서도 사용할 수 있습니다.

하지만 Android에서 Nomad를 구매한 뒤 iPad를 새로 구입했다면, 다시 구매해야 합니다.

이는 Nomad가 자체 라이선스 서버나 구독 모델을 사용하지 않기 때문입니다. Apple/Google/AppGallery 간에 라이선스 공유를 처리해 주는 협약도 없습니다. 

### 내 구매 내역을 복원하려면 어떻게 하나요? {#restore}
Google Play와 AppGallery는 동기화를 자동으로 처리합니다.

- 상단 왼쪽 Nomad 아이콘의 About 메뉴로 들어가 `restore purchase` 를 누르세요.
- (Google Play에서) Nomad를 구매했던 것과 같은 계정으로 로그인되어 있는지 다시 확인하세요.
- 기기를 재부팅하세요.
- 몇 시간을 기다려야 할 때도 있습니다.
- Google Play 앱이 최신 버전인지 확인하세요.
- Nomad를 재설치하세요(데이터를 잃고 싶지 않다면 반드시 [파일을 백업](#where-are-my-projects-located-on-my-device) 하세요).
- 다시 구매를 시도해 보며 어떤 메시지가 나오는지 확인할 수 있습니다(참고: 같은 계정으로는 동일 항목을 두 번 구매할 수 없습니다).

:::tip
<support@nomadsculpt.com> 로 연락하실 수 있지만, 제가 *유일하게* 할 수 있는 일은 해당 이메일에 구매 내역이 연결되어 있는지 확인하는 것뿐입니다.

새 기기를 구입한 후 라이선스가 제대로 갱신되지 않는다는 보고를 정기적으로 받고 있습니다.  
결제 및 계정 동기화는 전적으로 Google/AppGallery에서 처리하며, 저는 이에 대해 아무런 제어 권한이 없습니다!

결국에는 항상 구매 내역이 복원되지만, 이 과정을 빠르게 만드는 정확한 방법은 불분명합니다.
:::

::: warning
최근 Huawei 기기는 Google 서비스를 사용할 수 없습니다.  
이 경우 AppGallery(Huawei 앱 스토어)에서 앱을 다시 구매해야 합니다.
:::

### [내 언어]를 번역하거나 수정해 줄 수 있나요? {#locale}
다른 언어를 추가하는 것은 비교적 쉽지만, 정기적인 업데이트를 처리하기 위해 AI 번역에 의존하고 있습니다.  
번역 파일은 [여기](https://github.com/stephomi/nomad-translation)에서 찾을 수 있습니다.

## 기능 {#features}

### 왜 기즈모가 움직이지 않나요? {#gizmo-not-moving}
[왼쪽 메뉴 툴바에서 핀을 활성화](tools#left-menu-toolbar)했을 가능성이 있습니다. 

### Nomad 안에서 애니메이션을 할 수 있나요? {#animate}
현재는 불가능합니다. 레이어를 애니메이션할 수 있는 타임라인 기능은 흥미로울 수 있지만, 지금 당장은 계획에 없습니다.  

향후 리깅/스키닝을 지원하고 싶지만, (특히 스컬핑 도구와의 상호작용 등) 몇 가지 난제가 있어서 아직 확실하지 않습니다.

### 제대로 된 로우폴리 모델링을 할 수 있나요? {#lowpoly}
현재는 불가능합니다.  
이는 Nomad *Sculpt*의 주된 범위는 아니지만, 언젠가 몇 가지 도구를 제공할 수도 있습니다.

### UV 작업과 텍스처링을 할 수 있나요? {#texturing}
짧은 답: 가능합니다. 긴 답: 직접적으로는 아니지만, Nomad의 뛰어난 버텍스 페인트 도구를 UV와 텍스처와 결합하는 여러 방법이 있습니다.

* Nomad에서는 색상, 거칠기, 재질 속성을 스컬프의 버텍스에 직접 페인팅할 수 있습니다.
* Nomad는 매우 높은 버텍스 수를 허용하므로, UV를 신경 쓰지 않고도 페인팅할 수 있습니다.
* Nomad는 브러시에 사용할 텍스처를 불러올 수 있어, 텍스처로 스탬핑 및 페인팅이 가능합니다.
* Nomad는 렌더링 목적을 위해, 미리 텍스처가 할당된 오브젝트를 불러올 수 있습니다.
* Nomad는 저폴리 오브젝트를 [UV 언랩](topology.md#uv-unwrap)할 수 있습니다.
* 색상/거칠기/메탈니스는 [프로젝트 옵션](topology.md#reproject-to-vertex)을 통해 텍스처에서 버텍스로 전송할 수 있습니다.
* 색상/거칠기/메탈니스/노멀은 [베이킹 옵션](topology.md#bake-to-texture)을 통해 버텍스에서 텍스처로 베이크할 수 있습니다.
* 베이킹과 프로젝션은 단일 오브젝트 간, 여러 오브젝트 간, 또는 하나의 오브젝트에서 가장 높은/가장 낮은 서브디비전 레벨 간에 처리할 수 있어, 다양한 베이크/프로젝트 워크플로를 지원합니다.
* 베이킹 후 obj를 내보내면 텍스처도 함께 내보내지며, 이를 Procreate 같은 앱으로 가져가 텍스처 위에 직접 페인팅할 수 있습니다.

### 턴테이블 영상을 녹화할 수 있나요? {#video}
현재 계획은 없습니다. iOS에는 사용하기 매우 쉬운 [영상 녹화 기능](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados)이 있습니다.

iOS에서는 왼쪽 상단에서 아래로 스와이프한 뒤, 녹화 버튼을 탭하면 됩니다. 3초 카운트다운 후, 메뉴를 위로 밀어 Nomad를 보이게 하고 턴테이블 기능을 사용하세요. 완료되면 다시 오른쪽 상단에서 아래로 스와이프해 녹화 버튼을 탭해 종료합니다. 사진 앱의 동영상 편집 기능으로 영상의 앞뒤 불필요한 부분을 잘라낼 수 있습니다.

### 내가 좋아하는 기능을 최상위 버튼으로 추가해 줄 수 있나요? {#interface}
네, 이제 [인터페이스](interface.md) 메뉴에서 하단 툴바를 커스터마이즈할 수 있으며, 플로팅 툴바도 생성할 수 있습니다.

### 다음에 추가될 기능은 무엇인가요? {#next-features}
중/장기 로드맵에 대한 아이디어는 많지만, 아직 구체적으로 정해진 것은 없습니다.  

버그 수정과 기존 기능 개선이 항상 새로운 기능 추가보다 우선순위가 높습니다.

### Nomad에서 리깅을 할 수 있나요? {#rigging}
아니요, 하지만 계획 중입니다. 현재는 오브젝트를 서로 부모-자식 관계로 연결하고 피벗 포인트를 조정해, 간단히 포즈를 줄 수 있는 스컬프를 만들 수 있습니다.

### 조명을 4개 이상 사용할 수 있나요? {#lights}
아니요, 이는 Nomad의 실시간 렌더 엔진의 한계입니다. 대신 발광(Emissive) 오브젝트와 포스트 프로세스의 글로벌 일루미네이션을 사용해 이를 흉내낼 수 있으며, [이 튜토리얼](https://www.youtube.com/watch?v=QhrUGH7CuUA)에서 그 방법을 보여줍니다.

### ZBrush 툴을 가져올 수 있나요? {#zbrush-import}
아니요, Zbrush는 독점 포맷을 사용합니다. 대신 알파 맵을 추출해 Nomad에서 사용할 수는 있습니다. 

### 내가 칠한 색과 렌더 색이 왜 다르죠? 왜 렌더에서 흰색이 나오지 않나요? {#paint-pbr}
종이 한 장을 찍은 사진, 책상 조명을 찍은 사진, 태양을 찍은 사진을 상상해 보세요. 오래된 카메라와 화면에서는 이 모든 것이 그냥 ‘흰색’으로 보일 수 있습니다. 더 현대적인 시스템은 종이의 반사된 흰색, 램프의 발광, 태양의 매우 밝은 빛을 구분해 보여줄 수 있습니다.

현대 컴퓨터 그래픽은 비슷한 방식을 따르며, 빛과 표면의 물리적 특성을 모사하려 합니다. 이를 `Physically Based Rendering` 또는 PBR이라고 하며, Nomad의 PBR 렌더러는 여기에 기반합니다. 이는 현실적이고 균형 잡힌 결과를 제공하지만, 종종 밝게 칠한 색이 더 어둡게 보이기도 합니다.

페인팅한 색과 더 비슷한 렌더를 원한다면, 물리 기반/비물리 기반 양쪽 방식으로 조정할 수 있습니다:

비 PBR:
* `라이팅 메뉴에서 'Unlit' 모드를 사용하세요.` 색이 칠한 그대로 표시되지만, 모든 셰이딩을 잃게 됩니다. 빠른 확인이나 그래픽 스타일 출력에 유용합니다.
* `라이팅 메뉴에서 'Matcap' 모드를 사용하세요.` 색상 틴트가 없고 대부분 흰색인 더 밝은 Matcap을 선택하세요.

PBR:
* `중립적인 환경을 사용하세요.` [환경을 변경](shading.md#environment)해 더 중립적인 것으로 바꿀 수 있습니다. 실내 환경은 색이 강한 경우가 많으니 피하고, 야외 주간이나 스튜디오 환경을 사용하는 것이 좋습니다.
* `조명을 강화하세요.` 어두운 방에서 흰 종이를 찍는다면, 단순히 더 많은 빛을 추가할 것입니다. 환경광의 노출 슬라이더를 올려 색이 자연스럽게 느껴질 때까지 조정하거나, 강도가 더 높은 개별 라이트를 추가하세요.
* `카메라 노출을 올리세요.` 어두운 방에서 추가 조명이 없다면, 카메라의 셔터를 더 오래 열어 두거나 ISO를 높일 수 있습니다. Nomad에서는 포스트 프로세싱으로 비슷한 효과를 얻을 수 있습니다. 포스트 프로세스를 켜고, 톤 매핑을 활성화한 뒤, 노출 슬라이더를 올려 색이 자연스럽게 느껴질 때까지 조정하세요.
* `발광 색을 사용하세요.` 머티리얼 메뉴에서 텍스처 항목의 'emissive'를 활성화하면, 오브젝트가 광원처럼 보이게 할 수 있습니다. 포스트 프로세스 설정에서 글로벌 일루미네이션을 켜면, 이 오브젝트가 장면의 다른 오브젝트에 빛을 투사합니다. 또한 해당 머티리얼에 'unlit'을 활성화해, 텍스처 없이도 비슷한 느낌을 낼 수 있습니다.

## 크래시 {#crashes}

### 모델을 저장하거나 리메시할 때 크래시가 발생해요! {#crash-remesh}
기기의 메모리(RAM)가 부족한 상태입니다.  
씬의 메모리 사용량을 줄이려면, [Topology](topology.md) 옵션을 사용해 폴리곤 수를 줄일 수 있습니다.

::: tip RAM/Storage
중요한 것은 RAM 용량이며, 보통 훨씬 더 큰 저장 공간 용량이 아닙니다.
:::

### 프로젝트를 불러올 때 크래시가 발생해요! {#crash-load}
파일이 작다면, 저에게 보내주시면 확인해 보겠습니다(이메일: <support@nomadsculpt.com>).

그렇지 않다면, 기기의 RAM이 부족한 것일 가능성이 큽니다.

- 기기에서 실행 중인 다른 앱을 모두 종료하세요.
- 이미 프로젝트가 열린 상태가 아니라, Nomad에서 새 프로젝트를 시작한 뒤 시도해 보세요.
- 그래도 크래시가 발생한다면, [프로젝트 파일](#where-are-my-projects-located-on-my-device)을 RAM이 더 많은 기기에서 여는 수밖에 없습니다.

::: tip
데스크톱 브라우저에서는 [이 URL](https://nomadsculpt.com/demo_save/)에서 파일을 불러온 뒤, 씬을 단순화하고 다시 내보내 볼 수 있습니다.

일부 브라우저는 단일 탭이 사용할 수 있는 RAM 양을 제한하므로, 이 방법이 통하지 않을 수도 있습니다.

프로젝트에서 [레이어](layers.md)를 사용 중이라면, 메모리 사용량을 줄이기 위해 레이어를 합치는 것을 고려해 보세요.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Nomad를 시작할 때 크래시가 발생해요! {#crash-start}
시작 시 크래시가 발생한다면, Nomad 폴더 안에 있는 특정 파일을 불러오는 과정에서 문제가 생긴 것입니다.

대부분의 경우, 프로젝트가 너무 무거워 RAM 한도를 초과하기 때문에 발생합니다.

[Nomad 폴더](#where-are-my-projects-located-on-my-device)를 찾은 뒤, 문제의 원인을 찾기 위해 일부 파일의 이름을 바꾸거나 다른 곳으로 옮기세요.

먼저 `settings.json` 의 이름을 바꿔 보세요. 이렇게 하면 마지막 프로젝트를 자동으로 불러오지 않게 됩니다.

그래도 해결되지 않으면, 최근 파일들을 각 리소스 폴더(`projects`, `matcaps`, `environments` 등) 밖으로 옮겨 보세요.

폴더 이름 자체를 바꿔 Nomad가 완전히 무시하게 만들 수도 있습니다.  
Nomad 폴더 안의 모든 파일을 옮기거나 이름을 바꾸면, 사실상 깨끗한 재설치와 같은 효과를 얻을 수 있습니다.

::: tip
Nomad가 시작 시 파일을 불러올 때는 항상 그 파일을 `can_be_deleted/` 폴더로 먼저 옮깁니다.  
작업이 성공하면, 다시 원래 폴더로 되돌립니다.

로딩이 끝나기 전에 크래시가 발생하면, 다음 실행 시 Nomad는 `can_be_deleted/` 폴더를 무시하기 때문에 정상적으로 실행됩니다.

성공할 수 있다고 생각된다면, 해당 파일을 다시 불러오는 것을 시도해 볼 수 있습니다.
:::