# ![](/icons/image.webp) Hintergrund

Dieses Menü steuert die Hintergrundfarbe von Nomad sowie alle Referenzbilder, die verwendet werden sollen.

![](/images/background_overview.webp)

## Hintergrund 
![](/images/background_selector.webp)

Es gibt drei Optionen für den Viewport-Hintergrund.

* `Environment` – Zeigt die in [Shading](shading) ausgewählte Umgebungs-Map an. Dies kann mit den Reglern für Blur und Exposure (Helligkeit) weiter gesteuert werden. 
* `Color` – Eine einfarbige Fläche, die du auswählen kannst
* `Gradient` – Ein Farbverlauf von oben nach unten. Mit dem Faktor-Regler kannst du den Mittelpunkt des Farbverlaufs bestimmen.  

## Referenzbild

![](/images/background_reference.webp)

Du kannst ein Bild deiner Wahl im Hintergrund hinzufügen, das als Referenz verwendet wird.
Du kannst die Position und den Maßstab ändern, zum Beispiel, wenn du es in eine Bildschirmecke verschieben möchtest.

### ![](/icons/tool_transform.webp) Transform 

Mit dieser Schaltfläche kannst du das Referenzbild interaktiv platzieren. Verwende 2 Finger, um das Referenzbild zu verschieben, zu skalieren und zu drehen. Die endgültige Platzierung wird in den folgenden Reglern wiedergegeben:

* `Overlay` – Bei 0 % befindet sich das Referenzbild immer hinter deinen Objekten, bei 100 % davor. 
* `Opacity` – Wie transparent das Bild ist.
* `Position` – Die X- und Y-Position des Bildes.
* `Rotation` – Bildrotation.
* `Scale` – Bildskalierung.


::: tip

Kameras und Referenzbilder sind miteinander verknüpft. 

Das bedeutet: Wenn du dein Referenzbild so einrichtest, dass es mit deiner Skulptur übereinstimmt, und du dann eine Kamera über das [Camera-Menü](camera) erstellst, werden die Position, Rotation und Skalierung des Referenzbildes ebenfalls mit der Kamera gespeichert. Du kannst das Referenzbild ausschalten und zu einem anderen Viewport drehen. Wenn du wieder durch die Kamera schaust, wird das Referenzbild mit den von dir verwendeten Einstellungen aktiviert.

Das schließt sogar ein, dass du für verschiedene Kameras unterschiedliche Bilder auswählen kannst!

 ![](/videos/reference_camera.mp4)

:::
