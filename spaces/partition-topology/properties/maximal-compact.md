---
uid: T027122
space: partition-topology
property: maximal-compact
value: false
---
[[Proof]]

* [T000034] [Normal|P000013]
* [T000032] [$T_0$|P000001]
* [I000230] [maximal compact|P000102] => ([Compact|P000016] + [KC|P000100])
* [I000227] [KC|P000100] => [US|P000099]
* [I000226] [US|P000099] => [$T_1$|P000002]
* [I000034] ([$T_1$|P000002] + [Normal|P000013]) => [$T_{3 \frac{1}{2}}$|P000006]
* [I000114] [$T_{3 \frac{1}{2}}$|P000006] => [Urysohn|P000009]
* [I000086] [Urysohn|P000009] => [$T_{2 \frac{1}{2}}$|P000004]
* [I000032] [$T_{2 \frac{1}{2}}$|P000004] => [$T_2$|P000003]
* [I000173] [$T_2$|P000003] => [Sober|P000073]
* [I000174] [Sober|P000073] => [$T_0$|P000001]

