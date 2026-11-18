# ![](/icons/sliders.webp) Interface Menu {#interface-menu}

This menu controls many options to customise Nomad's interface. 

![](/images/interface_overview2.webp)

Nomad can be customized to quite a deep level, this menu is split across 5 tabs; Interface, Shortcuts, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
This page is for the interface menu, not the interface itself! The overall interface is described in [Getting Started](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interface {#interface}

The interface tab controls the color, size and layout of Nomad's user interface. It has two sub-tabs, `Appearance` and `Layout`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Colors {#presets}

![](/images/interface_presets.webp)

The `Appearance` sub-tab starts with a collection of color presets for the interface. Tap one to apply it, then fine tune it with the options below.

#### Accent and Base {#color-widgetcolor-base}
The primary colors used in the interface: `Accent` for selected buttons and slider bars, `Base` for the panels.

#### Text opacity {#text-opacity}
Soften text and icons against the panels.

#### Toggles, Checkbox, Tabs {#high-contrast-button}
The style of the toggle buttons (`Soft` or `Solid`), of the checkboxes (`Outline`, `Accent` or `Fill`) and of the tabs (`Underline`, `Soft` or `Solid`).

#### Colored tools {#colored}
Color code the icons by category, eg all mask tools are brown, split tools are red, flatten tools green etc.

#### Panel shadow {#material-color-preview}
Panels cast a shadow to stand out from the scene.

#### Transparent panel {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
When enabled, extra options will appear to control how menus and panels look in Nomad: `Panel tint` sets their color, `Blur strength` how much the scene behind them is blurred, and `Glass` adds edge refraction and highlights, most visible with a low blur.

::: tip
On small devices it can be useful to make the panel tint nearly white, transparent, and low blur strength, so menus won't obscure the scene.
:::

#### ![](/icons/reset.webp) Reset appearance {#reset-style}
Reset all the appearance options to their default values.

### ![](/icons/panel_detach.webp) Layout {#layout}

The `Layout` sub-tab controls where things are and how big they are.

#### Toolbox {#toolbox}

Options for the tool menu on the right of Nomad's interface.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Resize {#ui-resize-corner}

Toggle a resize handle in the toolbox bottom corner.

##### Hidden {#hidden}
Normally the toolbox icon in the top bar will toggle between a long single column, or a multi-column list of tools. This option will toggle between the multi column list, or being hidden.

##### Reset order {#reset-order}
Reset the default tools in the toolbox to the default order. Custom icons will remain in the toolbox at the end of the list.

#### Top bar {#rows-auto-1}
`Responsive` chooses what the top bar does when it doesn't fit the screen, mostly relevant for small screens: `Multiline` wraps the menus on several lines, `Scroll` keeps one line that you can scroll.

#### Mirror top bar {#mirror-top-bar}
Reverse the order of menus in the top bar.

#### Mirror side bars {#mirror-side-bars}
Swap the side bars so that the toolbox is on the left, tool options on the right.

#### Mirror bottom bar {#mirror-bottom-bar}
Move the bottom bar to the bottom right corner, and reverse the button order.

#### ![](/icons/move.webp) Drag panel {#drag-panel}
A floating panel is always moved by dragging its bar, this option lets you drag its body as well. On `Auto`, a finger or a stylus moves the panel only when the drag is more horizontal than vertical, so a vertical drag still scrolls the content. Set it to `Yes` to also drag with the mouse, in any direction.

#### ![](/icons/pencil.webp) Use Nomad Dialog {#use-nomad-dialog}
Show Nomad's own text dialog instead of the native one when you type a name or a value.

#### ![](/icons/stylus.webp) Hover dot {#hover-dot}
Show a small dot in the UI when a hovering stylus is detected.

#### ![](/icons/help.webp) Help popup on hover {#help-popup-on-hover}

For devices that support hover, enable if the context help in Nomad represented with the ![](/icons/help.webp) icon will appear on hover, or only when clicked.

#### Overall scale {#overall-scale}
A size multiplier on all the UI elements.
#### Panel width {#panel-width}
The width of the menus and panels.
#### Font scale {#font-scale}
Scale the fonts.
#### Vertical spacing {#vertical-spacing}
The spacing between elements in menus and panels.
#### Vertical spacing (left) {#vertical-spacing-left}
The spacing between elements in the left toolbar.

#### Edge offsets {#edge-offset}
You should change these values only if you have issues interacting with the buttons on the screen edges. If these sliders are disabled, Nomad will use the safe area values returned by the device itself.

::: tip
When migrating Nomad to a new device (eg replacing an iPhone 12 with an iPhone 15), make sure to reset edge options to defaults!
:::

#### ![](/icons/reset.webp) Reset layout {#reset-layout}
Reset all the layout options to their default values.

## ![](/icons/window.webp) Shortcuts {#shortcuts}

The shortcuts tab chooses which quick buttons appear around the viewport, and lets you build your own floating toolbars.

### Side bar {#side-bar}
The quick tool buttons at the bottom of the left side bar: `Smooth`, `Mask`, `Hide`, `Face Group` and `Gizmo`. Drag them to change their order.

### Bottom bar {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Tap a shortcut to add it to the bottom bar, or to remove it. These are enabled by default:
* `Undo` - undo the previous operation
* `Redo` - restore the previously undone operation
* `Solo` - Temporarily hide every other object, leaving only the selected one visible. Press again to restore all the objects.
* `X-Ray` - Temporarily make all other objects semi-transparent, leaving only the selected one solid. Press again to restore the default materials.
* `Voxel` - Remesh the current object using the last used voxel resolution. A long tap or a swipe up will bring up a resolution slider and sharp edges toggle.
* `Grid` - Toggle the view grid. A long tap or a swipe up will enable you to change the color and opacity of the grid.
* `Wireframe` - Toggle a wireframe overlay. A long tap or swipe up will enable you to change the color and opacity of the wireframe.
* `Inspect` - allow you to view properties of your mesh like uv's baked textures, other properties, overlaid on the background of Nomad.
* `Face Group` - Toggle the facegroup overlay, more info under [Tools->FaceGroup](tools.md#facegroup)

Other commonly used shortcuts are available too: `Outline`, `Projection` (perspective or orthographic), `MatCap`, `DynTopo`, and the [Multiresolution](topology.md#multiresolution) `Subdivide`, `Reverse` and level buttons.

#### ![](/icons/more.webp) Bindings {#bindings-list}

Almost every function of Nomad can be added to the bottom bar via the bindings button, which shows how many shortcuts the bar holds. A bindings menu will be displayed when the button is clicked:

![](/images/interface_bindings_search.webp)

You can search by category via the icons at the top, or use the search field to find functions by name. Click on a function to add it to the toolbar. Click again to remove it.

#### ![](/icons/eye_open.webp) Visible {#order}

Show or hide the whole bottom bar.

#### ![](/icons/reset.webp) Reset {#reset}

Reset will restore the bottom bar to its default settings.

### Floating windows {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Clicking the + will add a floating toolbar. It won't be visible until you click the bindings button and add some shortcuts to it, then you can make it visible.

You can make many toolbars, each one has a row with these options:

* Drag the handle on the left of a row to reorder the toolbars.
* `Name` - The name of the toolbar.
* `Visible` - Toggle visibility for the toolbar.
* `Bar` - Show a title bar on the toolbar.
* `Minify` - Keep the toolbar on screen when the interface is minified.
* `Bindings` - Display the binding window to select functions to add to or remove from the toolbar.
* `Delete` - Delete the toolbar.


## ![](/icons/gesture.webp) Gesture {#gesture}
The gesture menu controls how your finger, stylus, mouse and trackpad control Nomad.

![](/images/interface_gesture.webp)

### Gesture options {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad can limit operations based on the input device. For example a finger drag could only move the camera, while a stylus drag can only sculpt. If you have a mouse or trackpad, that can also be assigned to control specific operations.

Each row is an operation: toggle `Finger`, `Stylus` and `Mouse` to choose which inputs can do it.

* `Camera` - Move the camera.
* `Node editing` - Drag the handles drawn on the canvas, for example to edit a primitive, a curve, a repeater or a light.
* `Sculpt` - Sculpt with the brushes. Tools with their own row below follow that row instead.
* `Select object` - Tap an object to select it.
* `Material picking` - Long press on the canvas to pick the color or material under the cursor. It only works if the current brush has painting enabled.
* `On tap` - The tap shortcuts of tools like Mask, Hide and Face Group (see below).
* `Paint` - The Paint and Smudge tools.
* `Mask` - The Mask tool.
* `Face` - The Hide and Face Group tools.
* `Create` - The Tube, Lathe and Insert tools.
* `Cut` - The Trim, Split and Project tools.
* `Select` - The Select and Measure tools.
* `Gizmo` - The Gizmo and Lattice tools.
* `Transform` - The Transform and Arrange tools.

::: tip
A common setup on a tablet is to let only the stylus sculpt and paint, and keep your fingers for the camera. That way your palm or a stray finger never leaves a stroke on your model.
:::

### ![](/icons/tool_smooth.webp) Finger always smooths {#finger-always-smooths}
When enabled, your finger always smooths while a sculpting tool is active, whatever the brush. Turning it on removes `Finger` from the `Sculpt` row, so the stylus sculpts and the finger smooths.

### Allow air stroke {#allow-air-stroke}
Let a stroke start even if the cursor first lands off the mesh. Pick the tools it applies to: `Tool` (every other brush), `Smooth`, `Mask` and `Hide`. It only works for inputs that can sculpt but not move the camera, so these buttons are disabled until one of your inputs is set that way.

### ![](/icons/stroke.webp) Stroke snap {#stroke-snap}
Hold the pointer still at the end of a stroke to snap it into a straight line or a smooth curve. Keep dragging to rotate and scale the snapped stroke around its start point.

`Hold delay` sets how long you have to hold still before the stroke snaps, or before a shape switches to editing.

### ![](/icons/stylus.webp) Use extra input samples {#use-extra-input-samples}
Use the additional input samples reported by the device. Disable it if your strokes are jagged or pressure behaves incorrectly. This option isn't shown on iOS.

### ![](/icons/tool_mask.webp) Mask {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Enable the following one tap shortcuts without having to hold the mask button. It will allow the following gestures:
* tap on the background to invert the mask
* tap on a masked area to blur the mask
* tap on an unmasked area to sharpen the mask

#### Long press {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

A long press with the Mask tool switches between the mask brush and the lasso (SelMask):
* `Long press - Sculpt` - Long press, then keep dragging: the stroke is drawn with the other mode, and the previous one comes back at the end of the stroke.
* `Long press - Toggle` - Long press and release without moving to switch between the two.

### ![](/icons/tool_smooth.webp) Smooth {#smooth}
`Long press - Lasso` - A long press with the Smooth tool switches to the Select tool for the duration of the selection stroke.

### ![](/icons/tool_hide.webp) Hide {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` will enable the following shortcuts with the hide tool:
* Tap on a face group to hide it
* Tap in empty space to invert the hidden polygons

### ![](/icons/finger3.webp) Three fingers {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

If your device supports 3 finger gestures, configure shortcuts for that gesture. 

The option matrix allows you to define vertical and horizontal drags as separate shortcuts, or `No` to leave it off. Note that if the same gesture is chosen for 2 options, one will be disabled and its name is crossed out.

* `Rotate lighting` - Rotate the environment, lights, and Matcap.
* `Tool Radius` - Edit the tool radius.
* `Tool Intensity` - Edit the tool intensity. 

### ![](/icons/fingerprint.webp) History 2/3 {#history-23}
`History shortcuts` - when enabled, the following gestures are active:
* Undo - tap with 2 fingers
* Redo - tap with 3 fingers

`Long press` - when enabled, holding 2/3 fingers down will rapidly undo/redo.

### ![](/icons/mouse.webp) Mouse wheel {#mouse-wheel}
`Speed (3d zoom)` sets how fast the wheel zooms the view, and `Speed (2d interface)` how fast it scrolls the menus and panels. The minus button next to each slider reverses the direction.

### ![](/icons/fingerprint.webp) Trackpad {#trackpad}
On a Mac, `Two fingers` chooses what two fingers on the trackpad do. Pinching always zooms and twisting always rolls the view.
* `Off` - Two finger scrolling zooms, like the mouse wheel. The fingers are not read individually.
* `Pan` - Two fingers pan the view, and lifting one of them orbits. Same as on a tablet.
* `Orbit` - Two fingers orbit the view, and lifting one of them pans.

### Accessibility {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` will bring up a floating toolbar to control drag, pinch, roll and camera operations.

### Camera {#camera}
A shortcut to go to the `Camera` menu (camera options used to be here, but were moved to the camera menu).

### Pencil double tap -> Bindings {#pencil-tap}

A shortcut to go to the `Bindings` menu, where you set what the Pencil double tap does. Outside iOS it reads `Pencil button → Bindings`, for the stylus button.

### Palm rejection {#palm-rejection}
On phones and tablets, ignore touches whose contact area is larger than `Max size threshold`, like the palm of your hand resting on the screen. It might not work on every device, so turn it off if you have trouble interacting with the canvas.


## ![](/icons/keyboard.webp) Bindings {#bindings}
Keyboard and button shortcuts can be defined from the bindings menu:

![](/images/interface_bindings.webp)
Nearly all functions in Nomad can be bound to keyboard shortcuts if your device has a keyboard, or to extra buttons on your stylus, or even gamepad controllers.

To create a binding, click the rectangle next to the function, and press the key/button. 

Find functions via the category icons at the top, or via the search bar to find by name. 

Individual bindings can be disabled via the checkbox next to the binding name. Long press the checkbox and drag to reorder the list.

When two enabled bindings use the same shortcut, a ![](/icons/help.webp) icon appears next to them, listing the functions that clash.

### ![](/icons/more.webp) Context menu {#context-menu}
The ![](/icons/more.webp) icon after each binding brings up a context menu:

![](/images/interface_bindings_context.webp)

* `Clone` - Clone the binding, for example to give a function a second shortcut.
* `Reset` - Reset the binding
* `Delete` - Delete the binding. Only possible when the function has more than one binding.

Below them, some bindings have extra options:

* `Sticky keys` - For tool shortcuts and the quick shortcuts (Mask, Smooth, Gizmo, Hide, Face Group, Add/Sub), choose how a key press switches tools. `Auto` uses the default set in the [Advanced](#advanced) options.
  * `Hold` - Hold the key to use the tool, release it to return to the previous tool.
  * `Toggle` - Press once to switch tools.
  * `Quick Press` - Hold to use the tool temporarily, or quick press to switch to it.
* `Hold Revert` - For quick shortcuts, choose if releasing a held key always goes back to the previous tool, even when that tool was already active.
* `Toggle Previous Tool` - For tool shortcuts, pressing the shortcut of the current tool switches back to the last tool. It needs `Sticky keys` on `Toggle` or `Quick Press`.
* `Position` - For floating window shortcuts, open the window where it was (`Retain previous`) or under the cursor (`On cursor`).
* `Translating (on release)` / `Zooming (on release)` - For the camera zoom and pan bindings, switch to the other one when you release the key.
* Drag direction - For `Rotate lighting`, `Tool Radius` and `Tool Intensity`, choose a horizontal or vertical drag.
* `Sync` - For functions that add, clone or instance objects, choose whether to sync the result. By default, it uses the sync value set in the Scene menu.
* `On Background` - For the Smooth and Mask quick shortcuts, drag on the background while holding the key to draw a lasso: a selection lasso for Smooth, a mask lasso for Mask.
* `Force camera` - For the camera bindings, move the camera even if the same shortcut is also used by another binding, typically a tool shortcut or Add/Sub.
* `Linear roll` - For the roll binding, roll with a horizontal, vertical or diagonal drag instead of moving around the pivot.

::: tip
With `Quick Press`, one key does both: hold it for a quick smooth or mask and you're back on your brush when you let go, or tap it to stay on that tool.
:::

### ![](/icons/cog.webp) Advanced {#advanced}
At the bottom of the bindings menu is a gear menu for advanced options:

![](/images/interface_bindings_advanced.webp)

* `Quick shortcuts` - The default `Sticky keys` and `Hold Revert` for the Mask, Smooth, Gizmo, Hide, Face Group and Add/Sub shortcuts.
* `Tool shortcuts` - The default `Sticky keys` and `Toggle Previous Tool` for the tool shortcuts. With `Toggle Previous Tool` you can keep swapping between two tools with the same hotkey.
* `Shortcut window` - The `Sticky keys` mode of the shortcuts that show the floating windows.
* `Flip zoom Y` - Invert the vertical drag direction when zooming with a binding.
* `Linear roll` - Roll the view with a horizontal, vertical or diagonal drag instead of moving around the pivot.
* `SpaceMouse` - Enable 3Dconnexion SpaceMouse support. On some systems, extra options appear: what it moves (`Object`, `Camera`, `First Person`, `Drone`), `Auto-update pivot` to move the pivot to the surface under the cursor when it starts moving, and its `Translation`, `Zooming` and `Rotation` speeds.
* `Dead zones (drift)` - For `Gamepad`, `Joystick` and `Button` controllers. Raise these values if the camera moves while the controller is left untouched.
* `Tool Radius` - How a drag with the radius binding resizes the brush (`Circle`, `Center` or `dx`), then how much the radius bindings add (in pixels) or multiply at each press.
* `Tool Intensity` - How much the intensity bindings add or multiply at each press.
* `Camera - Speed` - The `Translation` and `Rotation` speed of the bindings that pan and rotate the view.
* `Reset bindings` - reset all the bindings to their defaults.
* `Reset order` - restore the default order of the bindings list.


## iOS ⌘ Keyboard shortcuts display {#ios-keyboard-shortcuts-display}

On iOS devices with a keyboard, hold the ⌘ (cmd) key to display a list of shortcuts.

Android keyboard support is a bit experimental.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debug {#debug}
Some experimental and debug options are stored in this menu. Many of these options should be left at their defaults, and only altered after contacting Nomad support. The icons at the top jump to each section.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalize UVs` - Nomad will normalize the UVs of the selected mesh inside the [0-1] tile.

### ![](/icons/sun.webp) Shading {#render}
* `Refraction write depth (back)` - The backface of refraction meshes will be written into the depth buffer.
* `Angle weighted smooth normals` - An adjustment to how smooth shading works that can avoid creases in certain cases.

### ![](/icons/speed.webp) Target FPS {#target-fps}
When disabled, Nomad will sync its frames-per-second with your display's refresh rate.

When enabled, you can set the frame per second Nomad will render.

### ![](/icons/window.webp) Interface {#debug-interface}
* `Toolbox: show all` - Nomad will hide tools that aren't relevant for the current selection, eg all sculpt brushes are hidden on primitives that aren't validated. This option will dim disabled tools rather than hide them.

The other interface options that used to be here are now in the [Interface](#interface) tab.

### ![](/icons/turntable.webp) Turntable {#gif-turntable}
Nomad can export an animated gif turntable. Note that due to limitations of the gif format quality is low. Screen recording is usually a better method.

* `Duration` - how long in seconds the turntable will be
* `Max frame sampling` - Many of Nomad's high quality rendering effects come from combining several frames together. This slider sets how many frames to combine, and its checkbox turns it on or off.
* `Rotation pivot` - what the camera rotates around: `Keep current` keeps the current pivot, `(0, 0, 0)` uses the center of the world, `Scene` the center of the scene.
* `Transparent background` - Use the transparent option for gifs. Note that gif's only support 1 bit transparency, so edges can be badly aliased.
* `Export (GIF)` - start the gif export process.

### ![](/icons/postprocess.webp) Post Process {#post-process}
* `Filtering` - Debug option
* `Format` - Debug option
* `Buffer reuse` - Debug option

### ![](/icons/ram.webp) Performance {#performance}
* `Multithread: general` - Debug option
* `Multithread: sculpting` - Debug option
* `Instanced repeat draw` - Draw all the copies of a repeater in a single draw call. Debug option.

### ![](/icons/star.webp) Feature {#feature}
* `nom: compress multires` - Reduce the size of projects and Nomad exports that use multiresolution. These files can't be opened by older versions of Nomad. This option might be removed and enabled by default in the future.
* `Flip quad split (on tap)` -  Debug option

### ![](/icons/bug.webp) Debug {#dev}
* `Logs` - Popup a log view
* `Log events` - Write your pointer events (finger, stylus, mouse) to the log view, to investigate input issues.
* `FPS` - add a frames-per-second counter to the viewport stats.
* `App review popup` - Debug option, on iOS and Android.

### ![](/icons/image.webp) Custom icons {#custom-icons}
Replace Nomad's icons with your own png files.
* `Import icons` - Import png files into `tmp_session/icons`. Each one replaces the base icon with the same name. They are dropped when Nomad restarts.
* `Export tool icons` - Copy the base `tool_<tool>.png` icons to `tmp_session/icons`, without overwriting. You can edit them there and apply them with `Reload icons`.
* `Reload icons` - Apply the icons from `tmp_session/icons`.

### Quad Remesh {#quad-remesh}
The quad remesh options are no longer in this menu: see [Quad Remesh](topology.md#quad-remesh-instant) in the Topology menu and the [Quad remesher](tools.md#quad-remesher) tool.

### Make store thumbnails {#make-store-thumbnails}
Render screenshots at sizes that fit the iOS App Store.