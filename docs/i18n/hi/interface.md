# ![](/icons/interface.webp) इंटरफ़ेस मेनू {#interface-menu}

यह मेनू Nomad के इंटरफ़ेस को कस्टमाइज़ करने के लिए कई विकल्पों को नियंत्रित करता है। 

![](/images/interface_overview2.webp)

Nomad को काफ़ी गहराई तक कस्टमाइज़ किया जा सकता है, यह मेनू 4 सेक्शनों में बँटा है; Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
यह पेज इंटरफ़ेस मेनू के लिए है, खुद इंटरफ़ेस के लिए नहीं! समग्र इंटरफ़ेस का वर्णन [Getting Started](gettingstarted.md) में किया गया है।
:::

## इंटरफ़ेस {#interface}

इंटरफ़ेस सेक्शन आपको शॉर्टकट जोड़ने, फ़्लोटिंग टूलबार बनाने, और Nomad के यूज़र इंटरफ़ेस के रंग, आकार, और रूप को नियंत्रित करने देता है।

![](/images/interface_overview3.webp)

### नीचे शॉर्टकट जोड़ें... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

नीचे वाले टूलबार में डिफ़ॉल्ट रूप से ये शॉर्टकट सक्षम होते हैं:
* `Undo` - पिछला ऑपरेशन वापस लें
* `Redo` - पहले से वापस लिए गए ऑपरेशन को पुनर्स्थापित करें
* `Solo` - अस्थायी रूप से बाकी सभी ऑब्जेक्ट छुपाएँ, केवल चयनित ऑब्जेक्ट दिखाई देगा। दोबारा दबाने पर सभी ऑब्जेक्ट वापस आ जाएँगे।
* `X-ray` - अस्थायी रूप से बाकी सभी ऑब्जेक्ट को अर्ध-पारदर्शी बना दें, केवल चयनित ऑब्जेक्ट ठोस रहेगा। दोबारा दबाने पर डिफ़ॉल्ट मटेरियल वापस आ जाएँगे।
* `Voxel remesh` - वर्तमान ऑब्जेक्ट को आख़िरी इस्तेमाल की गई voxel resolution से रीमेश करें। लंबा टैप या ऊपर की ओर स्वाइप करने पर resolution स्लाइडर और sharp edges टॉगल दिखाई देगा।
* `Grid` - व्यू ग्रिड को टॉगल करें। लंबा टैप या ऊपर की ओर स्वाइप करने पर आप ग्रिड का रंग और अपारदर्शिता बदल सकते हैं।
* `Wireframe` - वायरफ़्रेम ओवरले को टॉगल करें। लंबा टैप या ऊपर की ओर स्वाइप करने पर आप वायरफ़्रेम का रंग और अपारदर्शिता बदल सकते हैं।
* `Inspector` - आपको अपने मेष की प्रॉपर्टीज़ जैसे uv, baked textures, अन्य प्रॉपर्टीज़ को Nomad की बैकग्राउंड पर ओवरले के रूप में देखने देता है।
* `Face Group` - फेसग्रुप ओवरले को टॉगल करें, अधिक जानकारी [Tools->FaceGroup](tools.md#facegroup) के अंतर्गत।

अन्य सामान्य रूप से उपयोग किए जाने वाले शॉर्टकट इस मेनू से उपलब्ध हैं, और भी कई शॉर्टकट bindings बटन के अंदर मिल सकते हैं।

#### ![](/icons/more.webp) बाइंडिंग्स {#bindings-list}

Nomad के लगभग हर फ़ंक्शन को bindings बटन के ज़रिए शॉर्टकट टूलबार में जोड़ा जा सकता है। बटन क्लिक करने पर bindings मेनू दिखाई देगा:

![](/images/interface_bindings_search.webp)

आप ऊपर दिए गए आइकन से श्रेणी के अनुसार खोज सकते हैं, या नाम से फ़ंक्शन ढूँढने के लिए सर्च फ़ील्ड का उपयोग कर सकते हैं। किसी फ़ंक्शन पर क्लिक करने से वह टूलबार में जुड़ जाएगा। दोबारा क्लिक करने से वह हट जाएगा।

#### ![](/icons/list.webp) क्रम {#order}

यह शॉर्टकट्स की सूची दिखाएगा। शॉर्टकट्स को पुनः क्रमित करने के लिए लंबे समय तक दबाकर खींचें।

#### ![](/icons/reset.webp) रीसेट {#reset}

Reset नीचे वाले टूलबार को उसकी डिफ़ॉल्ट सेटिंग्स पर वापस ले आएगा।

### विंडो में शॉर्टकट जोड़ें... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

+ पर क्लिक करने से एक फ़्लोटिंग टूलबार जुड़ जाएगा। यह तब तक दिखाई नहीं देगा जब तक आप bindings बटन पर क्लिक करके इसमें कुछ शॉर्टकट नहीं जोड़ते, फिर आप इसे visible कर सकते हैं। 

आप कई टूलबार बना सकते हैं, हर टूलबार के लिए इस मेनू में निम्न विकल्प होते हैं:

* ![](/icons/checked.webp) `Visible` - टूलबार की visibility टॉगल करें
* ![](/icons/more.webp)`Bindings` - टूलबार में फ़ंक्शन जोड़ने या हटाने के लिए binding विंडो दिखाएँ।
* ![](/icons/list.webp)`Order` - टूलबार को पुनः क्रमित करने के लिए मेनू दिखाएँ।
* ![](/icons/reset.webp) `Reset` - टूलबार को उसकी डिफ़ॉल्ट स्थिति पर रीसेट करें।
* ![](/icons/resize_bottom_right.webp) `Resize corner` - टूलबार के निचले दाएँ कोने में resize हैंडल टॉगल करें।
* ![](/icons/sort_down.webp) `Collapsable` - ऊपर दाएँ कोने में collapse हैंडल टॉगल करें।
* ![](/icons/trash.webp) `Delete` - टूलबार हटाएँ।

### टूलबॉक्स {#toolbox}

Nomad के इंटरफ़ेस के दाएँ तरफ़ वाले टूल मेनू के विकल्प।

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) यूआई रिसाइज़ कॉर्नर {#ui-resize-corner}

टूलबार के निचले कोने में resize हैंडल टॉगल करें।

#### छिपा हुआ {#hidden}
आम तौर पर ऊपर वाले बार में toolbox आइकन एक लंबा सिंगल कॉलम और मल्टी-कॉलम टूल सूची के बीच टॉगल करेगा। यह विकल्प मल्टी-कॉलम सूची और पूरी तरह छुपे होने के बीच टॉगल करेगा।

#### रंगीन {#colored}
आइकन को श्रेणी के अनुसार रंग-कोड करें, जैसे सभी mask टूल भूरे, split टूल लाल, flatten टूल हरे आदि।

#### पंक्तियाँ: ऑटो (>1) {#rows-auto-1}

#### क्रम रीसेट करें {#reset-order}
टूलबॉक्स में डिफ़ॉल्ट टूल्स को उनकी डिफ़ॉल्ट क्रम में रीसेट करें। कस्टम आइकन सूची के अंत में टूलबॉक्स में बने रहेंगे।


### प्रीसेट्स {#presets}

![](/images/interface_presets.webp)

इंटरफ़ेस के लिए रंग प्रीसेट्स का संग्रह।

#### हाई-कॉन्ट्रास्ट बटन {#high-contrast-button}
बटनों के लिए एक वैकल्पिक स्टाइल जो उन्हें enabled होने पर ज़्यादा स्पष्ट बनाता है। Auto पर सेट होने पर, जब UI रंग कंट्रास्ट enabled/disabled के बीच कम होगा, Nomad इस मोड का उपयोग करेगा।

#### रंग विजेट/रंग बेस {#color-widgetcolor-base}
इंटरफ़ेस में उपयोग किए जाने वाले प्राथमिक रंग।

#### पारदर्शी पैनल, रंग पैनल, ब्लर स्ट्रेंथ {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
सक्रिय होने पर, Nomad में मेनू और पैनल कैसे दिखें, इसे नियंत्रित करने के लिए अतिरिक्त विकल्प दिखाई देंगे। उनका रंग, पारदर्शिता और blur मात्रा समायोजित की जा सकती है।

::: tip
छोटे डिवाइस पर color panel को लगभग सफ़ेद, पारदर्शी और कम blur strength पर रखना उपयोगी हो सकता है, ताकि मेनू सीन को न ढकें।
:::

----

### मिरर टॉप बार {#mirror-top-bar}
ऊपर वाले बार में मेनू के क्रम को उलट दें।

### मिरर साइड बार्स {#mirror-side-bars}
साइड बार को बदलें ताकि toolbox बाएँ और tool options दाएँ हों।

### मिरर बॉटम बार {#mirror-bottom-bar}
नीचे वाले बार को निचले दाएँ कोने में ले जाएँ, और बटन क्रम उलट दें।

### मटेरियल रंग प्रीव्यू {#material-color-preview}
जब आप किसी मटेरियल के लिए रंग चुनते हैं, तो इस मटेरियल का प्रीव्यू वर्तमान चयनित ऑब्जेक्ट पर दिखाया जाता है।

----
### होवर पर सहायता पॉपअप {#help-popup-on-hover}

जो डिवाइस hover सपोर्ट करते हैं, उन पर यह नियंत्रित करें कि Nomad में ![](/icons/help.webp) आइकन से दर्शाई गई context help hover पर दिखाई दे या केवल क्लिक करने पर।

----

### समग्र स्केल {#overall-scale}
सभी UI एलिमेंट्स पर आकार गुणक।
### पैनल चौड़ाई {#panel-width}
मेनू और पैनल की चौड़ाई।
### फ़ॉन्ट स्केल {#font-scale}
फ़ॉन्ट का स्केल।
### ऊर्ध्वाधर स्पेसिंग {#vertical-spacing}
मेनू और पैनल में एलिमेंट्स के बीच की दूरी।
### ऊर्ध्वाधर स्पेसिंग (बायाँ) {#vertical-spacing-left}
बाएँ टूलबार में एलिमेंट्स के बीच की दूरी।

----

### एज ऑफ़सेट {#edge-offset}
आपको ये मान केवल तभी बदलने चाहिए जब आपको स्क्रीन के किनारों पर बटनों के साथ इंटरैक्ट करने में समस्या हो। यदि ये स्लाइडर disabled हैं, तो Nomad डिवाइस द्वारा लौटाए गए safe area मानों का उपयोग करेगा।

::: tip
Nomad को नए डिवाइस पर माइग्रेट करते समय (जैसे iPhone 12 को iPhone 15 से बदलते समय), edge विकल्पों को ज़रूर डिफ़ॉल्ट पर रीसेट करें!
:::

### शैली रीसेट करें {#reset-style}
सभी UI एलिमेंट्स को उनकी डिफ़ॉल्ट वैल्यू पर रीसेट करें।


## जेस्चर {#gesture}
Gesture मेनू नियंत्रित करता है कि स्टायलस और उँगली के प्रेस Nomad को कैसे नियंत्रित करें।

![](/images/interface_gesture.webp)

### जेस्चर विकल्प {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad इनपुट डिवाइस के आधार पर ऑपरेशन्स को सीमित कर सकता है। उदाहरण के लिए उँगली से drag केवल कैमरा को हिला सकता है, जबकि स्टायलस से drag केवल sculpt कर सकता है। यदि आपके पास माउस या ट्रैकपैड है, तो उसे भी विशिष्ट ऑपरेशन्स को नियंत्रित करने के लिए असाइन किया जा सकता है।

Nomad वर्तमान में आपको इन मोड्स को उँगली, स्टायलस या माउस gesture के किसी भी संयोजन पर सेट करने देता है:

* Camera
* Sculpt
* Gizmo
* Material picking (लंबे प्रेस के ज़रिए)
* Select object


`Finger always smooths` - Smooth को केवल उँगली से drag पर काम करने के लिए सेट किया जा सकता है।

### ![](/icons/tool_mask.webp) मास्क {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - निम्न one tap शॉर्टकट्स को mask बटन को दबाए बिना सक्षम करें। यह निम्न gestures की अनुमति देगा:
* बैकग्राउंड पर टैप करने से mask invert होगा
* masked क्षेत्र पर टैप करने से mask blur होगा
* unmasked क्षेत्र पर टैप करने से mask sharpen होगा

### मास्क <-> SelMask टॉगल करें {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - लंबा प्रेस Mask और SelMask के बीच टॉगल करेगा और एक नया stroke शुरू करेगा। stroke के अंत में, पिछला टूल फिर से चुना जाएगा। 
* `Tool` - बिना हिलाए लंबा प्रेस और रिलीज़ करने से Mask और SelMask के बीच स्विच होगा। 

### ![](/icons/tool_hide.webp) हाइड {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` hide टूल के साथ निम्न शॉर्टकट्स सक्षम करेगा:
* किसी face group पर टैप करने से वह छुप जाएगी
* खाली जगह पर टैप करने से hidden polygons invert हो जाएँगे

### ![](/icons/finger3.webp) तीन उंगलियाँ {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

यदि आपका डिवाइस 3 उँगली gesture सपोर्ट करता है, तो उस gesture के लिए शॉर्टकट कॉन्फ़िगर करें। 

विकल्प मैट्रिक्स आपको वर्टिकल और हॉरिज़ॉन्टल drag को अलग-अलग शॉर्टकट के रूप में परिभाषित करने देता है। ध्यान दें कि यदि एक ही gesture 2 विकल्पों के लिए चुना जाता है, तो एक disable हो जाएगा।

* `Rotate lighting` - environment, lights, और Matcap को घुमाएँ।
* `Tool Radius` - टूल radius एडिट करें।
* `Tool Intensity` - टूल intensity एडिट करें। 

### ![](/icons/fingerprint.webp) हिस्ट्री 2/3 {#history-23}
`History shortcuts` - सक्षम होने पर, निम्न gestures सक्रिय होंगे:
* Undo - 2 उँगलियों से टैप
* Redo - 3 उँगलियों से टैप

`Long press` - सक्षम होने पर, 2/3 उँगलियाँ दबाए रखने से तेज़ी से undo/redo होगा।

### एक्सेसिबिलिटी {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` drag, pinch, roll और camera ऑपरेशन्स को नियंत्रित करने के लिए एक फ़्लोटिंग टूलबार लाएगा।

### कैमरा {#camera}
`Camera` मेनू पर जाने के लिए शॉर्टकट (कैमरा विकल्प पहले यहाँ थे, लेकिन अब कैमरा मेनू में स्थानांतरित कर दिए गए हैं)।

### पेंसिल डबल टैप -> बाइंडिंग्स {#pencil-tap}

`Bindings` मेनू पर जाने के लिए शॉर्टकट (Pencil tap और double tap विकल्प पहले यहाँ थे, लेकिन अब bindings मेनू में स्थानांतरित कर दिए गए हैं)।


## बाइंडिंग्स {#bindings}
कीबोर्ड और बटन शॉर्टकट bindings मेनू से परिभाषित किए जा सकते हैं:

![](/images/interface_bindings.webp)
Nomad के लगभग सभी फ़ंक्शन्स को कीबोर्ड शॉर्टकट (यदि आपके डिवाइस में कीबोर्ड है), या आपके स्टायलस के अतिरिक्त बटनों, या यहाँ तक कि गेमपैड कंट्रोलर से बाँधा जा सकता है।

किसी binding को बनाने के लिए, फ़ंक्शन के बगल वाले rectangle पर क्लिक करें, और key/button दबाएँ। 

ऊपर दिए गए category आइकन के ज़रिए फ़ंक्शन्स ढूँढें, या नाम से ढूँढने के लिए सर्च बार का उपयोग करें। 

व्यक्तिगत bindings को binding नाम के बगल वाले checkbox से disable किया जा सकता है।

### ![](/icons/more.webp) कॉन्टेक्स्ट मेनू {#context-menu}
हर binding के बाद ![](/icons/more.webp) आइकन एक context मेनू लाता है:

![](/images/interface_bindings_context.webp)

* `Clone` - binding की कॉपी बनाएँ
* `Reset` - binding रीसेट करें
* `Delete` - binding हटाएँ
* `Toggle shortcut on key tap` - कॉन्फ़िगर करें कि tap और long press को अलग-अलग तरह से ट्रीट किया जाए या नहीं। सक्षम होने पर, tap टूल को सक्रिय करेगा। long press टूल को केवल key दबे रहने तक सक्रिय रखेगा, key छोड़ने पर यह पिछले टूल पर लौट आएगा। अन्य 3D ऐप्स में इसे कभी-कभी 'sticky keys' कहा जाता है।

### उन्नत {#advanced}
Bindings मेनू के नीचे advanced विकल्पों के लिए गियर मेनू है:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - mask, smooth, gizmo, hide, sub के लिए मानक शॉर्टकट्स पर tap उस मोड पर टॉगल करेगा, लेकिन key दबाए रखने पर उस मोड पर स्विच होगा, और key छोड़ने पर मोड पिछले मोड पर लौट आएगा। अन्य 3D ऐप्स में इसे कभी-कभी 'sticky keys' कहा जाता है।
* `Toggle tool shortcuts` - किसी टूल शॉर्टकट का उपयोग करते समय, यदि वही शॉर्टकट दो बार दबाया जाता है, तो यह पिछले टूल पर टॉगल करेगा। इस तरह आप एक ही hotkey से दो टूल्स के बीच बार-बार स्विच कर सकते हैं।
* `Invert Y (Zooming)` - zoom को invert करेगा
* `Reset bindings` - सभी bindings को उनकी डिफ़ॉल्ट स्थिति पर रीसेट करें।


## iOS ⌘ कीबोर्ड शॉर्टकट डिस्प्ले {#ios-keyboard-shortcuts-display}

कीबोर्ड वाले iOS डिवाइस पर, शॉर्टकट्स की सूची दिखाने के लिए ⌘ (cmd) key दबाकर रखें।

Android कीबोर्ड सपोर्ट थोड़ा experimental है।

![](/images/shortcuts.webp)


## डिबग {#debug}
कुछ experimental और debug विकल्प इस मेनू में रखे गए हैं। इनमे से कई विकल्पों को उनकी डिफ़ॉल्ट स्थिति पर ही छोड़ना चाहिए, और केवल Nomad सपोर्ट से संपर्क करने के बाद ही बदला जाना चाहिए।

![](/images/interface_debug.webp)
### यूवी {#uv}
* `Normalize Uvs` - Nomad UVs को [0-1] टाइल के अंदर normalize करेगा।

### क्वाड रीमेश {#quad-remesh}
* `Instant Mesh` - instant remesh algorithm सक्षम करें
* `Quadriflow` - एक वैकल्पिक quad remesh विधि।

### रेंडर {#render}
* `Heightmap` - viewport को सीन की depth रेंडर करने के लिए बदलें। इसे brushes के लिए alpha maps बनाने में उपयोग किया जा सकता है।
* `Refraction write depth (back)` - refraction meshes के backface को depth buffer में लिखा जाएगा।
* `Flip Y (normal map)` - normal maps bake करते समय y चैनल को invert करें, कुछ गेम और रेंडर इंजनों के लिए आवश्यक।
* `Angle weighted smooth normals` - smooth shading के काम करने के तरीके में एक समायोजन जो कुछ मामलों में creases से बचा सकता है।

### लक्ष्य FPS {#target-fps}
disabled होने पर, Nomad अपने frames-per-second को आपके डिस्प्ले की refresh rate के साथ sync करेगा।

enabled होने पर, आप वह frame per second सेट कर सकते हैं जिस पर Nomad रेंडर करेगा।

### इंटरफ़ेस {#debug-interface}
* `Top: layout` 
  * Collapse: छोटे डिवाइस पर ऊपर वाला बार और ज़्यादा sub menus में collapse हो जाएगा। 
  * Scroll: यदि आप बड़े डिस्प्ले पर Nomad के आदी हैं और सामान्य लेआउट पसंद करते हैं, तो इसे enable करने पर standard चौड़ा top bar उपयोग होगा, और इसे स्क्रॉल किया जा सकेगा।
  * Multiline: पूरे top मेनू को कई लाइनों में दिखाएँ।
* `Bottom: draggable popup` - नीचे वाले टूलबार में कई बटन हैं जो dialog पॉपअप करते हैं। यदि यह विकल्प enabled है, तो वे dialogs स्क्रीन पर कहीं और खिसकाए जा सकते हैं।  
* `Toolbox: show all` - Nomad उन टूल्स को छुपा देगा जो वर्तमान selection के लिए प्रासंगिक नहीं हैं, जैसे validate न किए गए primitives पर सभी sculpt brushes छुप जाते हैं। यह विकल्प टूल्स को छुपाने के बजाय उन्हें dim करेगा।
* `Toolbox: colored` - toolbox आइकन को उनके प्रकार के आधार पर रंग-कोड करें।
* `Panel: Drop shadows` - मेनू और पैनल के चारों ओर drop shadows ड्रॉ करें। कुछ पुराने डिवाइस पर इससे performance पर असर पड़ सकता है।
* `Panel: Blending` - Debug विकल्प
* `Pointer: hovering dot` - जो डिवाइस stylus hover सपोर्ट करते हैं, उन पर मेनू और पैनल के ऊपर stylus hover होने पर एक dot दिखाएँ।

### GIF टर्नटेबल {#gif-turntable}
Nomad animated gif turntable एक्सपोर्ट कर सकता है। ध्यान दें कि gif फ़ॉर्मेट की सीमाओं के कारण गुणवत्ता कम होती है। स्क्रीन रिकॉर्डिंग आम तौर पर बेहतर तरीका है।

* `Duration` - turntable कितने सेकंड लंबा होगा
* `Rotation center` - कैमरा pivot कहाँ है, यानी सीन के किस हिस्से के चारों ओर कैमरा घूमेगा
* `Transparent background` - gifs के लिए transparent विकल्प का उपयोग करें। ध्यान दें कि gif केवल 1 bit transparency सपोर्ट करते हैं, इसलिए किनारे काफ़ी alias हो सकते हैं।
* `Max frame sampling` - Nomad के कई high quality rendering इफ़ेक्ट्स कई फ़्रेमों को मिलाकर आते हैं। यह स्लाइडर तय करता है कि कितने फ़्रेम मिलाए जाएँ।
* `Export (GIF)` - gif export प्रक्रिया शुरू करें।

### पोस्ट प्रोसेस {#post-process}
* `Filtering` - Debug विकल्प
* `Format` - Debug विकल्प
* `Buffer reuse` - Debug विकल्प

### परफॉर्मेंस {#performance}
* `Multicore general` - Debug विकल्प
* `Multicore sculpting` - Debug विकल्प
* `Partial Drawing` - Experimental फ़ीचर! इसका उपयोग तब करें जब आप high poly mesh के अपेक्षाकृत छोटे हिस्से को sculpt कर रहे हों। इससे sculpting स्मूद होनी चाहिए, लेकिन आपको wireframe enable नहीं करना चाहिए! साथ ही brush strokes के दौरान विज़ुअल artifacts आ सकते हैं।

### फीचर {#feature}
* `Flip quad split (on tap)` -  Debug विकल्प
* `Join: merge radius` - meshes को join करते समय यदि vertices काफ़ी क़रीब हैं तो वे अपने आप weld हो जाएँगे। आप इस स्लाइडर से radius समायोजित कर सकते हैं।

### डिबग {#dev}
* `Logs` - log view popup करें
* `App review popup` - Debug विकल्प
* `FPS` - viewport stats में frames-per-second काउंटर जोड़ें।