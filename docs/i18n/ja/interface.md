# ![](/icons/interface.webp) インターフェイスメニュー {#interface-menu}

このメニューでは、Nomad のインターフェイスをカスタマイズするための多くのオプションを制御できます。 

![](/images/interface_overview2.webp)

Nomad はかなり深いレベルまでカスタマイズ可能で、このメニューは「Interface」「Gesture」「Bindings」「Debug」の 4 つのセクションに分かれています。

![](/images/interface_menu.webp)


::: tip
このページはインターフェイス“メニュー”についてであり、インターフェイスそのものについてではありません！全体的なインターフェイスについては [Getting Started](gettingstarted.md) を参照してください。
:::

## インターフェイス {#interface}

Interface セクションでは、ショートカットの追加、フローティングツールバーの作成、Nomad のユーザーインターフェイスの色・サイズ・外観の制御ができます。

![](/images/interface_overview3.webp)

### ショートカットを追加（下部）... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

下部ツールバーには、デフォルトで次のショートカットが有効になっています:
* `Undo` - 直前の操作を取り消します
* `Redo` - 直前に取り消した操作をやり直します
* `Solo` - 一時的に他のすべてのオブジェクトを非表示にし、選択中のオブジェクトだけを表示します。もう一度押すと、すべてのオブジェクトが復元されます。
* `X-ray` - 一時的に他のすべてのオブジェクトを半透明にし、選択中のオブジェクトだけを不透明にします。もう一度押すと、デフォルトのマテリアルに戻ります。
* `Voxel remesh` - 直前に使用したボクセル解像度で現在のオブジェクトをリメッシュします。長押しまたは上方向へのスワイプで、解像度スライダーとシャープエッジのトグルが表示されます。
* `Grid` - ビューグリッドの表示/非表示を切り替えます。長押しまたは上方向へのスワイプで、グリッドの色と不透明度を変更できます。
* `Wireframe` - ワイヤーフレームオーバーレイの表示/非表示を切り替えます。長押しまたは上方向へのスワイプで、ワイヤーフレームの色と不透明度を変更できます。
* `Inspector` - メッシュの UV、ベイクされたテクスチャ、その他のプロパティを Nomad の背景上にオーバーレイ表示して確認できます。
* `Face Group` - フェイスグループオーバーレイの表示/非表示を切り替えます。詳細は [Tools->FaceGroup](tools.md#facegroup) を参照してください。 

その他のよく使われるショートカットもこのメニューから利用でき、さらに多くは Bindings ボタン内にあります。

#### ![](/icons/more.webp) バインド {#bindings-list}

Nomad のほぼすべての機能は、Bindings ボタンを通じてショートカットツールバーに追加できます。ボタンをクリックすると Bindings メニューが表示されます:

![](/images/interface_bindings_search.webp)

上部のアイコンでカテゴリ別に検索するか、検索フィールドで名前から機能を探せます。機能をクリックするとツールバーに追加され、もう一度クリックすると削除されます。

#### ![](/icons/list.webp) 並び順 {#order}

ショートカットの一覧を表示します。長押ししてドラッグすることでショートカットの順序を変更できます。

#### ![](/icons/reset.webp) リセット {#reset}

Reset は下部ツールバーをデフォルト設定に戻します。

### ショートカットを追加（ウィンドウ）... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

+ をクリックするとフローティングツールバーが追加されます。Bindings ボタンをクリックしてショートカットを追加し、可視化するまで表示されません。 

複数のツールバーを作成でき、それぞれのツールバーにはこのメニュー内で次のオプションがあります:

* ![](/icons/checked.webp) `Visible` - ツールバーの表示/非表示を切り替えます
* ![](/icons/more.webp)`Bindings` - ツールバーに追加・削除する機能を選択するための Bindings ウィンドウを表示します。
* ![](/icons/list.webp)`Order` - ツールバー内の順序を変更するメニューを表示します。
* ![](/icons/reset.webp) `Reset` - ツールバーをデフォルト状態にリセットします。
* ![](/icons/resize_bottom_right.webp) `Resize corner` - ツールバー右下隅にリサイズハンドルを表示/非表示します。
* ![](/icons/sort_down.webp) `Collapsable` - 右上隅に折りたたみハンドルを表示/非表示します。
* ![](/icons/trash.webp) `Delete` - ツールバーを削除します。

### ツールボックス {#toolbox}

Nomad インターフェイス右側のツールメニューに関するオプションです。

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) UIリサイズコーナー {#ui-resize-corner}

ツールバーの下隅にリサイズハンドルを表示/非表示します。

#### 非表示 {#hidden}
通常、上部バーのツールボックスアイコンは、縦長の 1 列表示と複数列のツールリスト表示を切り替えます。このオプションは、複数列リスト表示と非表示の切り替えを行います。

#### 色付き {#colored}
カテゴリごとにアイコンに色分けを行います。例: マスクツールは茶色、スプリットツールは赤、フラット系ツールは緑など。

#### 行数: 自動（>1） {#rows-auto-1}

#### 並び順をリセット {#reset-order}
ツールボックス内のデフォルトツールをデフォルトの順序にリセットします。カスタムアイコンはリスト末尾に残ります。


### プリセット {#presets}

![](/images/interface_presets.webp)

インターフェイス用のカラープリセット集です。

#### ハイコントラストボタン {#high-contrast-button}
有効時のボタンをより見やすくする代替スタイルです。Auto に設定すると、有効/無効間の UI カラーコントラストが低い場合に Nomad が自動的にこのモードを使用します。

#### カラーユニット / ベースカラー {#color-widgetcolor-base}
インターフェイスで使用される基本色です。

#### 透明パネル、カラーパネル、ぼかし強度 {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
有効にすると、Nomad 内のメニューやパネルの見た目（色・透明度・ぼかし量）を制御するための追加オプションが表示されます。

::: tip
小型デバイスでは、カラーパネルをほぼ白・高い透明度・低いぼかし強度に設定すると、メニューがシーンを隠しにくくなり便利です。
:::

----

### 上部バーをミラー {#mirror-top-bar}
上部バー内のメニューの並び順を反転します。

### サイドバーをミラー {#mirror-side-bars}
サイドバーを入れ替え、ツールボックスを左側、ツールオプションを右側に配置します。

### 下部バーをミラー {#mirror-bottom-bar}
下部バーを右下隅に移動し、ボタンの順序を反転します。

### マテリアル色プレビュー {#material-color-preview}
マテリアルの色を選択すると、そのマテリアルのプレビューが現在選択中のオブジェクトに表示されます。

----
### ホバー時にヘルプポップアップ {#help-popup-on-hover}

ホバーをサポートするデバイス向けに、Nomad 内の ![](/icons/help.webp) アイコンで表されるコンテキストヘルプをホバーで表示するか、クリック時のみ表示するかを切り替えます。

----

### 全体スケール {#overall-scale}
すべての UI 要素に対するサイズ倍率です。
### パネル幅 {#panel-width}
メニューやパネルの幅です。
### フォントスケール {#font-scale}
フォントサイズの倍率です。
### 垂直間隔 {#vertical-spacing}
メニューやパネル内の要素間の縦方向スペースです。
### 垂直間隔（左） {#vertical-spacing-left}
左側ツールバー内の要素間の縦方向スペースです。

----

### エッジオフセット {#edge-offset}
画面端のボタン操作に問題がある場合のみ、これらの値を変更してください。スライダーが無効な場合、Nomad はデバイス自身が返すセーフエリア値を使用します。

::: tip
Nomad を新しいデバイスに移行する際（例: iPhone 12 から iPhone 15 に買い替えた場合）は、エッジオプションを必ずデフォルトにリセットしてください！
:::

### スタイルをリセット {#reset-style}
すべての UI 要素をデフォルト値にリセットします。


## ジェスチャ {#gesture}
Gesture メニューでは、スタイラスや指での操作が Nomad をどのように制御するかを設定します。

![](/images/interface_gesture.webp)

### ジェスチャオプション {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad では、入力デバイスに基づいて操作を制限できます。たとえば、指でのドラッグはカメラ移動のみに、スタイラスでのドラッグはスカルプトのみに限定できます。マウスやトラックパッドがある場合、それらにも特定の操作を割り当てられます。

現在 Nomad では、以下のモードを指・スタイラス・マウスの任意の組み合わせのジェスチャーで制御するよう設定できます:

* Camera
* Sculpt
* Gizmo
* Material picking（長押しで実行）
* Select object


`Finger always smooths` - Smooth を指ドラッグでのみ動作させるように設定できます。

### ![](/icons/tool_mask.webp) マスク {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Mask ボタンを押し続けなくても、以下のワンタップショートカットを有効にします。次のジェスチャーが可能になります:
* 背景をタップしてマスクを反転
* マスクされた領域をタップしてマスクをぼかす
* マスクされていない領域をタップしてマスクをシャープにする

### マスク <-> SelMask の切り替え {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - 長押しで Mask と SelMask を切り替え、新しいストロークを開始します。ストローク終了時に、前のツールが再選択されます。 
* `Tool` - 動かさずに長押しして離すと、Mask と SelMask を切り替えます。 

### ![](/icons/tool_hide.webp) 非表示 {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` を有効にすると、Hide ツールで次のショートカットが使えます:
* フェイスグループをタップしてそのグループを非表示
* 何もない空間をタップして非表示ポリゴンを反転

### ![](/icons/finger3.webp) 3本指 {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

3 本指ジェスチャーをサポートするデバイスでは、そのジェスチャーに対するショートカットを設定できます。 

オプションマトリクスでは、縦方向ドラッグと横方向ドラッグを別々のショートカットとして定義できます。同じジェスチャーが 2 つのオプションに選択されている場合、一方は無効になります。

* `Rotate lighting` - 環境、ライト、Matcap を回転させます。
* `Tool Radius` - ツール半径を編集します。
* `Tool Intensity` - ツール強度を編集します。 

### ![](/icons/fingerprint.webp) 履歴 2/3 {#history-23}
`History shortcuts` - 有効にすると、次のジェスチャーが有効になります:
* Undo - 2 本指でタップ
* Redo - 3 本指でタップ

`Long press` - 有効にすると、2/3 本指を押し続けることで高速に Undo/Redo を行います。

### アクセシビリティ {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` を有効にすると、ドラッグ・ピンチ・ロール・カメラ操作を制御するためのフローティングツールバーが表示されます。

### カメラ {#camera}
`Camera` メニューへのショートカットです（カメラオプションは以前ここにありましたが、Camera メニューに移動しました）。

### ペンシルのダブルタップ -> バインド {#pencil-tap}

`Bindings` メニューへのショートカットです（Pencil のタップおよびダブルタップオプションは以前ここにありましたが、Bindings メニューに移動しました）。


## バインド {#bindings}
キーボードやボタンのショートカットは Bindings メニューから定義できます:

![](/images/interface_bindings.webp)
デバイスにキーボードがある場合、Nomad のほぼすべての機能をキーボードショートカットに割り当てられます。また、スタイラスの追加ボタンやゲームパッドコントローラーにも割り当て可能です。

バインディングを作成するには、機能の横の四角をクリックし、キー/ボタンを押します。 

上部のカテゴリアイコンから機能を探すか、検索バーで名前から探せます。 

個々のバインディングは、バインディング名の横のチェックボックスで無効化できます。

### ![](/icons/more.webp) コンテキストメニュー {#context-menu}
各バインディングの後ろにある ![](/icons/more.webp) アイコンはコンテキストメニューを表示します:

![](/images/interface_bindings_context.webp)

* `Clone` - バインディングを複製します
* `Reset` - バインディングをリセットします
* `Delete` - バインディングを削除します
* `Toggle shortcut on key tap` - タップと長押しを別扱いにするかどうかを設定します。有効にすると、タップでツールを有効化し、長押しではキーを押している間だけツールを有効化し、離すと前のツールに戻ります。他の 3D アプリで「sticky keys」と呼ばれる動作に相当します。

### 詳細 {#advanced}
Bindings メニューの下部には、高度なオプション用のギアメニューがあります:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Mask、Smooth、Gizmo、Hide、Sub など標準ショートカットをタップするとそのモードに切り替わりますが、キーを押し続けるとその間だけそのモードになり、キーを離すと前のモードに戻ります。他の 3D アプリで「sticky keys」と呼ばれる動作に相当します。
* `Toggle tool shortcuts` - ツールショートカットを使用中に、同じショートカットを 2 回押すと前のツールに戻ります。このようにして、同じホットキーで 2 つのツールを行き来できます。
* `Invert Y (Zooming)` - ズーム方向を反転します
* `Reset bindings` - すべてのバインディングをデフォルトにリセットします。


## iOS ⌘ キーボードショートカット表示 {#ios-keyboard-shortcuts-display}

キーボード付きの iOS デバイスでは、⌘（cmd）キーを押し続けるとショートカット一覧が表示されます。

Android のキーボードサポートはやや実験的です。

![](/images/shortcuts.webp)


## デバッグ {#debug}
このメニューには、いくつかの実験的・デバッグ用オプションが含まれています。多くのオプションはデフォルトのままにしておき、Nomad サポートに連絡したうえでのみ変更することを推奨します。

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - UV を [0-1] タイル内に正規化します。

### クアッドリメッシュ {#quad-remesh}
* `Instant Mesh` - Instant Remesh アルゴリズムを有効にします
* `Quadriflow` - 代替のクアッドリメッシュ手法です。

### レンダー {#render}
* `Heightmap` - ビューポートをシーンの深度をレンダリングするモードに変更します。ブラシ用のアルファマップを作成する際に使用できます。
* `Refraction write depth (back)` - 屈折メッシュの裏面をデプスバッファに書き込みます。
* `Flip Y (normal map)` - 法線マップをベイクする際に Y チャンネルを反転します。一部のゲームエンジンやレンダリングエンジンで必要です。
* `Angle weighted smooth normals` - スムースシェーディングの処理方法を調整し、特定のケースでの折れ目を回避します。

### 目標FPS {#target-fps}
無効時、Nomad はフレームレートをディスプレイのリフレッシュレートに同期します。

有効時、Nomad がレンダリングするフレームレートを指定できます。

### インターフェイス {#debug-interface}
* `Top: layout` 
  * Collapse: 小型デバイスでは上部バーを折りたたみ、より多くのサブメニューに分割します。 
  * Scroll: 大画面での Nomad に慣れており通常レイアウトを好む場合、これを有効にすると標準の横長トップバーが使用され、スクロール可能になります。
  * Multiline: 上部メニュー全体を複数行にわたって表示します。
* `Bottom: draggable popup` - 下部ツールバーにはダイアログをポップアップするボタンがいくつかあります。このオプションを有効にすると、それらのダイアログを画面上の別の場所に移動できます。  
* `Toolbox: show all` - Nomad は、現在の選択に関係しないツール（例: 未バリデートのプリミティブではすべてのスカルプトブラシを非表示）を隠します。このオプションを有効にすると、非表示にする代わりに無効なツールを減光表示します。
* `Toolbox: colored` - ツールボックスアイコンを種類に応じて色分けします。
* `Panel: Drop shadows` - メニューやパネルの周囲にドロップシャドウを描画します。一部の古いデバイスではパフォーマンスに影響する場合があります。
* `Panel: Blending` - デバッグ用オプション
* `Pointer: hovering dot` - スタイラスホバーをサポートするデバイスで、スタイラスがメニューやパネル上にホバーしているときにドットを表示します。

### GIFターンテーブル {#gif-turntable}
Nomad はアニメーション GIF のターンテーブルをエクスポートできます。ただし GIF 形式の制限により画質は低くなります。通常は画面録画の方が高品質です。

* `Duration` - ターンテーブルの長さ（秒）
* `Rotation center` - カメラのピボット位置、つまりカメラが回転するシーン上の中心位置
* `Transparent background` - GIF に透過背景を使用します。ただし GIF は 1 ビット透過のみサポートするため、エッジが大きくジャギーになる場合があります。
* `Max frame sampling` - Nomad の高品質レンダリング効果の多くは複数フレームの合成によって実現されています。このスライダーは合成するフレーム数を設定します。
* `Export (GIF)` - GIF エクスポートプロセスを開始します。

### ポストプロセス {#post-process}
* `Filtering` - デバッグ用オプション
* `Format` - デバッグ用オプション
* `Buffer reuse` - デバッグ用オプション

### パフォーマンス {#performance}
* `Multicore general` - デバッグ用オプション
* `Multicore sculpting` - デバッグ用オプション
* `Partial Drawing` - 実験的機能です！高ポリメッシュの一部のみをスカルプトしている場合に使用してください。スカルプトをよりスムーズにできるはずですが、ワイヤーフレームは有効にしないでください。また、ブラシストローク中に視覚的なアーティファクトが発生する場合があります。

### 機能 {#feature}
* `Flip quad split (on tap)` -  デバッグ用オプション
* `Join: merge radius` - メッシュ結合時に、十分近い頂点を自動的にウェルドします。このスライダーで半径を調整できます。

### デバッグ {#dev}
* `Logs` - ログビューをポップアップ表示します
* `App review popup` - デバッグ用オプション
* `FPS` - ビューポート統計にフレームレートカウンターを追加します。