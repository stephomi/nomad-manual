# ![](/icons/material.webp) マテリアル

このメニューでは、現在のオブジェクトのマテリアル、オブジェクト／マテリアルのレンダー特性を変更したり、マテリアルにテクスチャを割り当てたりできます。

![](/images/material_overview.webp)

マテリアルは、オブジェクトが光や他のオブジェクトに対してどのように反応するかを制御することで、その見た目を定義します。オブジェクトの見た目は次のプロパティによって制御されます。

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

これらのプロパティを組み合わせることで、フォトリアルからカートゥーン調、実験的な表現まで、非常に幅広い結果を得ることができます。

Color、roughness、metalness、opacity はペイント可能です。詳しくは [Vertex Paint options](painting.md) を参照してください。

Material type、reflectance、emssive/unlit は、以下で説明するマテリアルプロパティです。

このメニュー上部のコピー／ペーストボタンを使うと、あるオブジェクトから別のオブジェクトへマテリアルをコピーできます。

Nomad のレンダラーはリアルタイムレンダラーであることに注意してください。強力ではありますが、特定の効果においては精度よりも速度を優先します。

## マテリアルタイプ

![](/images/material_types.webp)

Nomad のマテリアルタイプには、Opaque、Subsurface、Blending、Additive、Refraction、Dithering、Shadow Catcher があります。

### ![](/icons/material_opaque.webp) Opaque
デフォルトのモードで、ペイントされた color、roughness、metalness、opacity をサポートするシンプルなマテリアルとしてサーフェスを扱います。

### ![](/icons/material_subsurface.webp) Subsurface
このモードは、肌、ろう、翡翠のように、光が内部でぼやけたり散乱したりするマテリアルをシミュレートできます。

最良の結果を得るには、PBR シェーディングモードに切り替え、少なくとも 1 つのディレクショナルライトまたはスポットライトを使用し、理想的には環境光を弱めてください。

`Depth` は、光が表面の前面から内部へ散乱し、再び前面から出てくるまでの距離を制御します。これにより、硬い影が柔らかくなり、表面ディテールがぼやけたように見えます。

`Translucency` は、葉の裏側を通る散乱光や、耳が強く逆光で照らされているときのように、光が形状の前面から背面へどのように散乱するかを制御します。

### ![](/icons/material_blending.webp) Blending

Opaque に似ていますが、opacity スライダーをサポートしており、マテリアルをソリッドから透明まで連続的に変化させることができます。これは、Opaque マテリアルがサポートするペイント可能な opacity とは異なり、単一のシンプルなスライダーです。

::: warning
Blending モードは、複雑な形状や交差する形状でちらつきやポッピングを引き起こすことがあります。
:::

### ![](/icons/material_additive.webp) Additive
このマテリアルを使うと、メッシュを半透明にできます。Blending マテリアルに似ていますが、Blending が周囲と混ざり合うのに対し、Additive は常に背後のオブジェクトよりも明るくなります。光の筋、炎、爆発などの明るいエフェクトに適しています。

Opacity 値を 1 より大きく設定することができ、その場合オブジェクトはより明るくなります。  
[bloom](postprocess.md#bloom) と `threshold parameter` を使って、このオブジェクトだけをエミッシブオブジェクトのように発光させたい場合に便利です。

このモードは、[Blending](#blending) よりもアーティファクトが少ない傾向があります（順序非依存トランスペアレンシー）。

### ![](/icons/material_refraction.webp) Refraction
このモードはガラスのようなマテリアルをシミュレートするために使用できます。リアルタイム処理の制約により、自己屈折や多層屈折にはある程度の制限があります。

モデルにペイントされた roughness は、屈折のぼやけ具合に影響します。  
デフォルトでは、Nomad で作成されるすべてのオブジェクトには、roughness が約 25% に設定されているため、屈折は完全にはっきりせず、ややぼやけた状態になります。  
`paint glossy` ボタンを使うと、roughness と metalness を 0 にしてモデルを塗り直すことができます（色は影響を受けません）。

ここでは 2 種類の roughness が関係します。1 つは表面の反射のぼやけ具合を制御し、もう 1 つは内部（屈折）のぼやけ具合を制御します。  
しかし、Nomad にはペイント用の roughness チャンネルが 1 つしかないため、内部と外部の roughness は同じ値を共有します。  
異なる値（たとえば、表面はシャープだが内部はぼやけたロリポップのような表現）にしたい場合は、`Surface glossiness` と `Interior roughness` スライダーを使って、ペイントされた roughness を上書きします。

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering
ランダムにいくつかのピクセルを破棄することで、オブジェクトを半透明にします。

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher

オブジェクトを不可視にし、影だけを受け取るようにします。Nomad のレンダーを他の画像と合成する際に便利です。

::: tip

透明度とブレンディングモードに関する詳細情報は https://support.fab.com/s/article/Transparency-Opacity を参照してください。

:::

## コントロール

![](/images/material_controls.webp)

### Always unlit
有効にすると、オブジェクトは PBR や Matcap を無視し、シェーディングなしでペイントされた色のみを表示します。  
[Additive](#additive) を使用している場合、黒色を使って直接透明度をペイントできることに注意してください。

### Opacity
オブジェクトがどれだけソリッド（不透明）に見えるかを制御します。100% は完全にソリッド、0% は完全に透明です。より細かく制御したい場合は、opacity をペイントすることもできます。

### Reflectance
非金属マテリアルが受け取る反射の量を制御します。通常はデフォルト値（標準的な正面角での 4% の反射光に相当）を使用しますが、キャラクターの目の反射やハイライトを強調したい場合などに値を上げることができます。

### Inverse culling
サーフェスの法線を反転させます。通常は不要ですが、モデルが裏返しに見える場合や、`Two sided` を無効にした状態と組み合わせて、カメラに最も近い壁が常に非表示になるようなインテリア表現に使用できます。

### Smooth Shading
[グローバルオプション](settings.md#smooth-shading) を参照してください。  
`Auto` 値はグローバルオプションを使用します。

### Two sided
[グローバルオプション](settings.md#two-sided) を参照してください。  
`Auto` 値はグローバルオプションを使用します。

### Coloured backface
[グローバルオプション](settings#two-sided) を参照してください。  
`Auto` 値はグローバルオプションを使用します。

### Casts shadows
現時点では `Auto` は `On` と同じです。  
透明オブジェクトも影を落とします（ブレンドされた影をエミュレートするためにディザパターンで描画されます）。  
シーン内に、影を落とす必要のない大きなオブジェクト（たとえば大きな床）がある場合は、必ず影のキャストを無効にしてください。

### Recieve shadows
現時点では `Auto` は `On` と同じです。

### Wireframe
[グローバルオプション](settings.md#wireframe) を参照してください。  
`Auto` 値はグローバルオプションを使用します。


## テクスチャ

![](/images/material_textures.webp)

オブジェクトに UV がある場合、頂点の color／roughness／metalness／opacity に加えて、マテリアルにテクスチャを適用できます。通常、これらはテクスチャベイクの結果ですが、Nomad の外部で作成された画像を使用することもできます。

テクスチャを適用できるのは次の項目です。

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

テクスチャスロットをクリックするとセレクターが表示されます。テクスチャがマテリアルスロットに割り当てられた後、再度クリックするとテクスチャパネルが表示されます。

### テクスチャパネルオプション

![](/images/material_texture_panel.webp)

### Open
別のテクスチャを選択します。

### None
テクスチャを削除します。

### Opacity

画像にアルファチャンネルがある場合、それを Opacity に使用するか、無視するかを選択できます。

### ![](/icons/link.webp) チェーン／リンクアイコン 

以下のセクションにあるリンクアイコンを有効にすると、そのテクスチャに対して使用されるオプションが、リンクアイコンが有効になっている他のテクスチャ（color、normal、roughness、metalness、opacity、emissive）と共有されます。

これにより、位置合わせされたテクスチャ同士が、パラメータやプロジェクションタイプを変更してもずれないようにできます。


### Projection
![](/images/material_projection.webp)

テクスチャをオブジェクトにどのように適用するかを設定します。

* `Auto` - オブジェクトに UV があれば UV、なければ Triplanar
* `UV` - メッシュの UV 座標を使ってテクスチャを適用します。メッシュとテクスチャが Nomad の外部から来ている場合や、Nomad から外部で使用するためにエクスポートする場合は、UV が正しい選択です。
* `Triplanar` - X、Y、Z 軸に沿ってテクスチャを投影し、継ぎ目をブレンドします。

### Triplanar
![](/images/material_triplanar.webp)

Triplanar プロジェクションは、テクスチャをオブジェクトに適用するための、強力でありながらシンプルな方法です。

Triplanar は、同じ画像を持つ 6 台のビデオプロジェクターが、オブジェクトの前面、背面、左、右、上、下に向けて投影しているようなものです。

必要に応じて、これを UV や頂点カラーにベイクすることができます。

![](/images/material_triplanar_example.webp)

#### Method

* `Local` - プロジェクションはオブジェクトのトランスフォームと一緒に移動します。
* `World` - プロジェクションは固定され、オブジェクトを動かすと、オブジェクトがプロジェクションの中をスライドしていくように見えます。

#### Hardness

プロジェクション同士の混ざり方を制御します。100% ではブレンドが行われず、プロジェクションの境界はシャープになります。0% では広い角度にわたって境界がブレンドされます。デフォルトは 90% で、境界を隠すのに十分なブレンドを行いつつ、それ以外の部分はシャープに保ちます。

### Uniform

オンにすると、すべてのプロジェクションに同じ Hardness が使用されます。オフにすると、X、Y、Z プロジェクションごとに個別の Hardness コントロールが表示されます。


### Parameter
![](/images/material_parameter.webp)

#### Filtering
使用するテクスチャフィルタ方式です。`Auto` がデフォルトで、`Nearest`、`Linear`、`Mipmap` があります。Nearest はフィルタリングを行わないため、テクスチャを近くで見るとギザギザのアーティファクトが発生することがあります。Linear と Mipmap はより良いフィルタリングを行うため、近くで見たときにギザギザではなくぼやけて見えます。

#### Tiling-X
Scale パラメータが 1 より大きく、テクスチャがオブジェクトの UV より小さくなっている場合、X 軸方向にテクスチャをどのようにタイルするかを指定します。`None` は繰り返しなし、`Repeat` はテクスチャをコピーして繰り返します。`Mirror` はテクスチャをコピーし、2 枚目ごとに反転させて配置することで、タイルの繰り返しによるアーティファクトを目立たなくできます。

#### Tiling-Y
Tiling-X と同様ですが、Y 軸方向に対する設定です。

### Transform
![](/images/material_transform.webp)

UV 空間でテクスチャに適用される 2D 変換です。リセットボタンでデフォルト値に戻せます。チェーンアイコン（color 以外のテクスチャが選択されている場合）は、Transform を color テクスチャとリンクさせるかどうかを切り替えます。

#### Translation
テクスチャの X および Y 方向のオフセットです。

#### Rotation
テクスチャの回転です。

#### Scale
テクスチャのスケールです。値を大きくすると、オブジェクト上でテクスチャが小さく表示されます。Tiling-X と Tiling-Y スライダーを使って、その際の挙動を制御します。

### Uniform scale
オフにすると、Scale-X と Scale-Y の個別コントロールが表示されます。
