---
type: protein-evaluation
gene: "CDIN1"
date: 2026-05-31
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## CDIN1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | CDIN1 / C15orf41 |
| 蛋白全名 | CDAN1-interacting nuclease 1 |
| 蛋白大小 | 281 aa / 32.3 kDa |
| UniProt ID | Q9Y2V0 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt Nucleus + Cytoplasm (ECO:0000269); GO nucleus IDA |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 281 aa, 32.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | Strict=7 |
| 三维结构 | 7/10 | ×3 | 21.0 | 无 PDB; pLDDT 93.5（极高，86.8% >90） |
| 调控结构域 | 2/10 | ×2 | 4.0 | IPR029404 (CDIN1 family), PF14811 |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING CDAN1/ASF1B/ASF1A 有实验支持; IntAct 多重互作 |
| **加权总分** | | | **125/180**** | |
| 互证加分 | | | +1.0 | UniProt/GO 多源实验定位互证（ECO:0000269 + IDA） |
| **归一化总分 (÷1.83)** | | | **68.3/100**** | |

PubMed strict: 7

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269); Cytoplasm (ECO:0000269) | 实验证据 |
| GO-CC | cytoplasm (IDA:UniProtKB); nucleus (IDA:UniProtKB) | 实验证据 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**结论**: CDIN1 核-胞质定位有 UniProt ECO:0000269 + GO IDA 双源实验支持，定位置信度可靠。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9Y2V0-F1 |
| 平均 pLDDT | 93.5 |
| pLDDT >90 | 86.8% |
| pLDDT 70-90 | 11.0% |
| pLDDT 50-70 | 1.1% |
| pLDDT <50 | 1.1% |
| PDB | 无 |
| InterPro | IPR029404 |
| Pfam | PF14811 |

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CDIN1/CDIN1-PAE.png]]
![[CDIN1-PAE.png]]

pLDDT 极高（均值 93.5），86.8% 残基 >90，仅 1.1% <50。AlphaFold 预测质量极佳，蛋白应有明确折叠结构域。但无 PDB 实验结构，结构域功能注释有限。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 7 |
| PubMed broad | 11 |
| 别名 | C15orf41（未用于 scoring） |

关键文献：
- PMID:40091041 — "Mechanism of ASF1 engagement by CDAN1" (Nat Commun, 2025)
- PMID:39149339 — "Mechanism of ASF1 Inhibition by CDAN1" (bioRxiv, 2024)
- PMID:38747503 — "Updates on clinical and laboratory aspects of hereditary dyserythropoietic anemias" (Int J Lab Hematol, 2024)
- PMID:33159567 — "Congenital dyserythropoietic anemia types Ib, II, and III: novel variants in CDIN1 gene" (Ann Hematol, 2021)

功能聚焦于先天性红细胞生成不良性贫血（CDA），CDIN1 与 CDAN1 和组蛋白伴侣 ASF1A/ASF1B 互作。研究量低，高度新颖。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| CDAN1 | STRING | 0.923 (exp 0.239, textmining 0.903) | Codanin-1，CDA 核心互作 |
| ASF1B | STRING | 0.732 (exp 0.534) | 组蛋白伴侣 H3-H4，实验支持 |
| ASF1A | STRING | 0.704 (exp 0.592) | 组蛋白伴侣 H3-H4，实验支持 |
| SEC23B | STRING | 0.722 (textmining) | COPII 囊泡，CDAII 关联 |
| FAM98B | STRING | 0.584 (textmining) | 低置信度 |
| ASF1B | IntAct | anti bait coIP (PMID:17353931) | 组蛋白伴侣，物理互作 |
| ASF1A | IntAct | anti tag coIP (PMID:28514442) | 组蛋白伴侣 |
| TRIP13 | IntAct | validated two hybrid (PMID:32296183) | AAA+ ATPase，减数分裂 |
| ZNF609 | IntAct | anti tag coIP (PMID:33961781) | 锌指转录因子 |
| — | UniProt | 无 curated 互作 | — |

STRING top 为 CDAN1 + 组蛋白伴侣 ASF1A/ASF1B。ASF1B 在 IntAct 中有 anti bait coIP 物理互作记录（PMID:17353931），ASF1A 有 anti tag coIP。PPI 网络指向组蛋白代谢与染色质组装，与核-胞质定位一致，但缺少 UniProt curated 互作。

### 4. 总体评价
CDIN1 是一个实验确认的核-胞质蛋白，AlphaFold 结构预测质量极高（pLDDT 93.5），功能指向红细胞生成与组蛋白代谢。PPI 网络包含 CDAN1、ASF1A、ASF1B 等染色质相关因子。PubMed strict=7，高度新颖。主要局限是无 PDB 实验结构和调控结构域注释有限（仅 IPR029404/PF14811）。建议作为中等优先级核-胞质候选。
![[CDIN1-PAE.png]]

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2V0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2V0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDIN1
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CDIN1/CDIN1-PAE.png]]



![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CDIN1/CDIN1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000186073-CDIN1/subcellular

![](https://images.proteinatlas.org/61023/1112_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/61023/1112_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/61023/1116_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/61023/1116_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/61023/1421_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/61023/1421_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
