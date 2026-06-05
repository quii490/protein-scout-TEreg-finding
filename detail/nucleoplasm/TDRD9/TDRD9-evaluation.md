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
