# ![](/icons/history.webp) 历史 {#history}
![](/images/history_overview.webp)

与大多数内容创作工具一样，你可以在 Nomad 中撤销/重做所有编辑操作。  
可撤销操作的数量是有限的，但你可以控制这一行为。

::: tip
你可以使用快捷手势来撤销/重做：
- 两指轻点撤销
- 三指轻点重做
:::

## 历史 {#history-panel}
![](/images/history_history.webp)

此面板显示历史堆栈，展示步骤数量、操作名称以及该步骤所占用的内存大小。

## 设置 {#settings}
![](/images/history_settings.webp)

### 历史限制（Mb） {#history-limit-mb}
如果历史堆栈超过该数值，较早的操作将被移除，以便内存占用符合此限制。

### 最大可撤销次数 {#maximum-undoable}
你可以控制可撤销操作的最大数量。

## 恢复相机 {#restore-camera}
对于每个操作，相机的视角都会被保存。  
如果启用此选项，撤销或重做某个操作时，相机会重置到保存的视角。

## 包含操作 {#include-actions}

* `Lights` - 禁用时，与灯光相关的操作（gizmo 移动除外）将不会记录到历史堆栈中
* `Matcaps & HDRIs` - 禁用时，对 matcap 和 HDRI 的更改将不会记录到历史堆栈中
* `PostProcess` - 禁用时，对后期处理选项的更改将不会记录到历史堆栈中

## 内存统计 {#memory-stats}

本节提供 Nomad 使用内存的详细分解。