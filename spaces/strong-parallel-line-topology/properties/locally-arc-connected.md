---
uid: T022762
space: strong-parallel-line-topology
property: locally-arc-connected
value: false
---
[[Proof]]

* [T000313] [Totally Separated|P000048]
* [T000310] [Regular|P000011]
* [I000063] [Locally Arc Connected|P000043] => [Locally Path Connected|P000042]
* [I000089] ([Locally Path Connected|P000042] + ~[Discrete|P000052]) => ~[Totally Path Disconnected|P000046]
* [I000047] [Totally Disconnected|P000047] => [Totally Path Disconnected|P000046]
* [I000143] [Discrete|P000052] => [Metrizable|P000053]
* [I000046] [Totally Separated|P000048] => [Totally Disconnected|P000047]
* [I000069] [Metrizable|P000053] => [$T_5$|P000008]
* [I000112] [$T_5$|P000008] => [$T_4$|P000007]
* [I000113] [$T_4$|P000007] => [$T_{3 \frac{1}{2}}$|P000006]
* [I000149] [$T_{3 \frac{1}{2}}$|P000006] => [Completely Regular|P000012]
* [I000035] [Completely Regular|P000012] => [Regular|P000011]

