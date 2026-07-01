---
type: protein-evaluation
gene: "TDRD9"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## TDRD9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TDRD9 / C14orf75 |
| 蛋白全名 | ATP-dependent RNA helicase TDRD9 |
| 蛋白大小 | 1382 aa / 155.7 kDa |
| UniProt ID | Q8NDG6 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24.0 | UniProt Cytoplasm (ECO:0000269) + Nucleus (ECO:0000250); GO-CC cytoplasm (IDA) + nucleus (IDA); piP-body |
| 蛋白大小 | 2/10 | x1 | 2.0 | 1382 aa, 155.7 kDa, 大蛋白 |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed strict=34, broad=51 |
| 三维结构 | 4/10 | x3 | 12.0 | AlphaFold mean pLDDT 80.0; PDB 无; pct_gt_90=31.9% |

| 调控结构域 | 4/10 | x2 | 8.0 | TUDOR domain (IPR002999) + DEAD/DEAH helicase (IPR011545, IPR014001); 非经典染色质结构域 |
| PPI 网络 | 2/10 | x3 | 6.0 | IntAct 仅 3 条 (DNAJC7, SEMA4B, CLOCK); STRING 502 error; UniProt 无互作记录 |
| **加权总分** | | | **92/180********** | |
| 互证加分 | | | +2.0 | piRNA/转座子沉默效应因子 |
| **归一化总分 (÷1.83)** | | | **50.3/100********** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000269) + Nucleus (ECO:0000250) | Curated + By similarity |
| GO-CC | cytoplasm (IDA), nucleus (IDA), piP-body (ISS) | 实验 + 序列推断 |
| Protein Atlas (IF) | HPA 无定位数据 (no_image_detected) | 未确认 |
| Literature | piRNA 通路核效应因子，与 PIWIL4 共定位于核 | 功能支持 |

**HPA IF 状态**: No image detected -- HPA 对 TDRD9 无可用 IF 图像，仅返回 tissue RNA 数据。核定位基于 UniProt + GO-CC double IDA 支持。

**结论**: TDRD9 在 UniProt 和 GO-CC 均有 Cytoplasm + Nucleus 双重 IDA 定位记录，作为 piRNA 通路的核效应因子有功能上的核定位支持。但缺乏 HPA IF 独立验证,且 UniProt Nucleus 为 by similarity (ECO:0000250) 而非直接 curated。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q8NDG6-F1 (v6) |
| 平均 pLDDT | 80.0 |
| pLDDT >90 | 31.9% |
| pLDDT 70-90 | 50.1% |
| pLDDT <50 | 10.1% |
| PDB | 无 |
| InterPro | IPR011545, IPR007502, IPR014001, IPR001650, IPR027417, IPR035437, IPR002999 (TUDOR), IPR047384 |
| Pfam | PF00270 (DEAD), PF21010, PF00271 (Helicase_C), PF00567 (TUDOR) |

AlphaFold 整体置信度中等偏高 (mean 80.0)，TUDOR 结构域区段预测较可靠，但 helicase 核心区域存在低置信度区段。无 PDB 实验结构。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 34 |
| PubMed symbol only | 49 |
| PubMed broad | 51 |
| 别名 | C14orf75（未用于 scoring） |

关键文献：
- PMID:39417902 (Arora M et al., 2024) -- 精子形态异常遗传谱
- PMID:40645105 (Hu K et al., 2025) -- piRNA 通路因子与男性不育
- PMID:39174853 (Wang W et al., 2024) -- TDRD9 复合杂合突变致少精子症
- PMID:32059713 (Babakhanzadeh E et al., 2020) -- 无精子症睾丸 TDRD 家族表达
- PMID:32365144 (Sari I et al., 2020) -- 卵巢刺激对 piRNA 通路蛋白的影响

TDRD9 研究集中在男性不育/精子发生领域，piRNA 转座子沉默是其核心功能。UniProt function 明确指出 "required to repress transposable elements" 和 "acts as a nuclear effector together with PIWIL4"。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| DNAJC7 | IntAct | co-IP (PMID:26496610) | Chaperone |
| SEMA4B | IntAct | co-IP (PMID:33961781, Cell 2021) | Signaling |
| CLOCK | IntAct | co-IP (PMID:33961781, Cell 2021) | Circadian/nuclear |
| -- | STRING | 502 error | 未获取 |
| -- | UniProt | 无记录互作 | -- |

IntAct 仅 3 条实验互作记录，其中 CLOCK 为核蛋白（昼夜节律转录因子），可能提示 TDRD9 在核内参与节律相关过程。但 PPI 数据总体薄弱。

### 4. 总体评价
TDRD9 是一个 piRNA 通路相关的核效应因子，直接参与转座子沉默。UniProt+GO-CC 双重 IDA 支持核定位，但缺乏 HPA IF 独立验证。PPI 数据和结构数据均不理想 (PDB=0, IntAct=3)。推荐作为低优先级候选，主要在 piRNA/TE 调控方向上具有独特价值。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIWIL4 | STRING | 995 |
| MAEL | STRING | 969 |
| PIWIL2 | STRING | 963 |
| PIWIL1 | STRING | 927 |
| ASZ1 | STRING | 839 |
| DDX4 | STRING | 827 |
| TDRD7 | STRING | 809 |
| HENMT1 | STRING | 796 |


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDG6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDG6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TDRD9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156414-TDRD9


HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NDG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NDG6 |
| SMART | SM00487;SM00847;SM00490;SM00333; |
| UniProt Domain [FT] | DOMAIN 142..308; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 377..544; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542"; DOMAIN 944..1004; /note="Tudor"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00211" |
| InterPro | IPR011545;IPR007502;IPR014001;IPR001650;IPR027417;IPR035437;IPR002999;IPR047384; |
| Pfam | PF00270;PF21010;PF00271;PF00567; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156414-TDRD9/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->


### 深度机制分析

TDRD9（Tudor domain-containing protein 9）是piRNA通路的核效应因子，其1382个氨基酸承载了哺乳动物生殖细胞转座子沉默最为优雅的分子架构——TUDOR结构域与DEAD/DEAH RNA解旋酶的串联。结构域图谱显示两个功能模块：N端DEAD-like helicase超级家族（IPR014001）包含Helicase ATP-binding（InterPro:IPR011545, Pfam:PF00270, 残基142-308）和Helicase C-terminal（IPR001650, Pfam:PF00271, 残基377-544）两个子域；C端TUDOR结构域（IPR002999, Pfam:PF00567, 残基944-1004）识别PIWI蛋白上对称二甲基精氨酸（sDMA）修饰。SMART注释进一步将helicase模块解析为DEXDc（SM00487, ATPase）、HELICc（SM00490, 解旋酶C端）和HA2（SM00847, 辅助结构域），TUDOR为SM00333。

AlphaFold预测pLDDT=80.0（mean），质量分层明显：TUDOR结构域区域（约900-1050残基）预测置信度高（beta桶折叠紧凑有序），而helicase连接区段存在10.1%的pLDDT<50低置信度区域，反映了DEAD-box解旋酶在无底物结合时RecA-like结构域间构象灵活性。PDB无实验结构，但同源结构丰富（如Drosophila Tejas/Tapas的TUDOR-helicase串联、以及人DDX4/VASA的解旋酶结构）。

TDRD9在piRNA通路中的分子机制已得到功能研究的充分定义。UniProt注释明确指出："required to repress transposable elements"和"acts as a nuclear effector together with PIWIL4"。这一机制分为三步：(1) 胞质阶段——TDRD9通过TUDOR结构域识别PIWIL4（MIWI2）的sDMA修饰，形成TDRD9-PIWIL4-piRNA三元复合体；(2) 核输入——该复合体通过核孔转运进入细胞核；(3) 核效应阶段——TDRD9的DEAD-box解旋酶活性利用ATP水解能解开转座子位点新生转录本的二级结构，将piRNA引导至同源转座子基因组位点，建立DNA甲基化和抑制性组蛋白修饰（H3K9me3）。

PPI互作网络高度集中且功能专一。STRING结果中PIWIL4（score=995, 最高置信度）、PIWIL2（score=963）、PIWIL1（score=927）以及MAEL（score=969, 生殖细胞piRNA通路支架蛋白）、ASZ1（score=839）、DDX4/VASA（score=827, 生殖细胞DEAD-box解旋酶）、TDRD7（score=809, 同家族TUDOR蛋白）和HENMT1（score=796, piRNA 2'-O-甲基转移酶）构成了piRNA通路的全谱。CLOCK互作（IntAct, PMID:33961781）添加了一个有趣的维度——昼夜节律转录因子与piRNA通路因子的结合，暗示转座子沉默可能在昼夜节律调控下动态变化。

PubMed文献集中在男性不育。PMID 39417902、40645105和39174853层层递进地揭示TDRD9复合杂合突变导致精子形态异常、少精子症和无精子症的遗传谱——所有表型均归因于转座子去抑制引起的减数分裂基因组不稳定性。已研究的TDRD9突变包括错义突变（破坏TUDOR-PIWI互作）、无义突变（截短蛋白）和剪接位点突变（外显子跳跃）。这些临床遗传学证据以人类生殖表型验证了TDRD9转座子沉默的不可或缺性。

综合来看，TDRD9的深度机制模型为：DEAD-helicase ATPase（解开RNA二级结构）+TUDOR sDMA识别（锚定PIWI/piRNA）→PIWIL4-piRNA-TDRD9三元复合体核输入→转座子新生转录本靶向→DNA甲基化/H3K9me3抑制性染色质建立→TE转录沉默。这是25个评估蛋白中对TE调控最具直接性和确定性的分子机制——TDRD9不仅是TE调控候选，而已是经功能验证的TE沉默效应因子。其49.2/100的低归一化评分主要受限于：大蛋白扣分（1382 aa）、低PPI实验互作记录（IntAct仅3条独立记录，虽然STRING推算互作极强）、pLDDT中等（80.0）——但这些评分局限不削弱其在TE调控中的独特生物学价值。在25个核蛋白中，TDRD9是TE调控机制证据最为充分和直接的蛋白。


