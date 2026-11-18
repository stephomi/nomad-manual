# ![](/icons/history.webp) History {#history}
![](/images/history_overview.webp)

Like most content creation tools, you can undo/redo all editing in Nomad.
The history can grow large, so you control how much of it stays in memory, how much is kept on storage, and whether it's saved with your project.

::: tip
You can use quick gestures to undo/redo:
- 2 fingers tap to undo
- 3 fingers tap to redo
:::

## ![](/icons/history.webp) History {#history-panel}
![](/images/history_history.webp)

This panel displays the history stack, showing the number of steps, the operation name, the object it applied to, and the amount of memory that step is using.

Tap an entry to jump back (or forward) to that state. Long press an entry to permanently delete it and all the older history, a quick way to free memory once you're happy with your sculpt.

### ![](/icons/speed.webp) Replay {#replay}
The play button at the bottom left rewinds to the root, then redoes the operations one by one, a fun way to watch your sculpt being built. The slider sets the speed in operations per second. Tap the button again to stop, an undo/redo or a tap on an entry also stops it.

Before it starts, a popup lets you choose:
* `Reverse` - Undo from the current state back to the root, instead of replaying from the root.
* `Restore camera` - The camera follows the replayed operations, even when [Restore camera](#restore-camera) is off.
* `Camera smoothing` - The camera glides between the views instead of jumping to each one. Higher values give a calmer camera.

::: warning
Replay is experimental.
:::

## Include actions {#include-actions}

The icons at the bottom of the History panel choose which kind of edits are recorded in the history:

| Action      | Icon                          | Description                                                                         |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Lights      | ![](/icons/light.webp)        | Light edits. Moving a light with the Gizmo is always recorded, as it can impact other objects in the scene hierarchy |
| Shading     | ![](/icons/sun.webp)          | The PBR, MatCap and Unlit mode, MatCaps and HDRIs                                   |
| PostProcess | ![](/icons/postprocess.webp)  | PostProcess edits                                                                   |
| Selection   | ![](/icons/tool_lattice.webp) | Lattice selection edits, such as clicks, lasso selections and deselection          |

## Settings {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Restore camera {#restore-camera}
For each operation, the viewpoint of the camera is saved.
If you enable this option, undoing or redoing an operation will reset the camera to the saved viewpoint.

### ![](/icons/history.webp) Save history {#save-history}
Keep the undo history when the project is saved, so it survives reopening the project. Turn it off to keep your project files smaller.

### ![](/icons/ram.webp) RAM limit {#history-limit-mb}
The maximum amount of history kept in RAM. Older states are moved to storage and loaded again when needed, they are not deleted.

### ![](/icons/save.webp) Storage limit {#storage-limit}
The maximum amount of storage used by this project's history. When the limit is reached, the oldest operations are permanently deleted.

::: tip
A new limit takes effect after the next edit, undo or redo.
:::

### ![](/icons/undo.webp) Undo warning {#maximum-undoable}
Jumping back more than this many operations in one go asks for a confirmation first. If you make an edit afterwards, all the operations after that point are lost, so this protects you from an accidental tap far down the list.

## Memory stats {#memory-stats}

This section gives a breakdown of memory used by Nomad.
