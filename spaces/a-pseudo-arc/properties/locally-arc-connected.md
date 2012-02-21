---
uid: T023505
space: a-pseudo-arc
property: locally-arc-connected
value: false
---
[[Proof]]

* [T001058] [Totally Path Disconnected|P000046]
* [T000469] [Connected|P000036]
* [T000957] [Metrizable|P000053]
* [I000063] [Locally Arc Connected|P000043] => [Locally Path Connected|P000042]
* [I000089] ([Locally Path Connected|P000042] + ~[Discrete|P000052]) => ~[Totally Path Disconnected|P000046]
* [I000042] [Discrete|P000052] => ([$T_1$|P000002] + [Scattered|P000051])
* [I000043] ([$T_1$|P000002] + [Scattered|P000051]) => [Totally Disconnected|P000047]
* [I000052] [Totally Disconnected|P000047] => ~[Connected|P000036]
* [I000098] [$T_4$|P000007] => ([$T_1$|P000002] + [Normal|P000013])
* [I000157] [Perfectly Normal|P000015] => [$T_4$|P000007]
* [I000070] [Metrizable|P000053] => [Perfectly Normal|P000015]

