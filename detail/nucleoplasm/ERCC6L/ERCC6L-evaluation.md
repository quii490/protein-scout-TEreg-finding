---
type: protein-evaluation
gene: "ERCC6L"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERCC6L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERCC6L / PICH |
| 蛋白名称 | DNA excision repair protein ERCC-6-like |
| UniProt ID | Q2NKX8 |
| 蛋白大小 | 1250 aa |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA Nucleoplasm + UniProt Centromere/Kinetochore + GO Kinetochore |
| 蛋白大小 | 5/10 | ×1 | 5 | 1250 aa (偏大) |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 41 篇 (21-50) |
| 三维结构 | 8/10 | ×3 | 24 | AF pLDDT=62.1 + PDB:5JNO |
| 调控结构域 | 9/10 | ×2 | 18 | SNF2 家族 ATPase/Helicase, 染色质重塑 |
| PPI 网络 | 8/10 | ×3 = 24 | PLK1,RMI1,TOP3A,BLM - 着丝粒/染色质 |
| 互证加分 | — | max +3 | +2.0 | SNF2染色质重塑 + GO Kinetochore + PPI确认 |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| TEreg 筛选 | 核评分 6 | Tier1 |
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Chromosome, Centromere, Kinetochore | Reviewed |
| GO-Cellular Component | Kinetochore | IDA |


**HPA IF 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERCC6L/IF_images/116854_A_7_3_rna_selected.jpg|HPA IF]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERCC6L/IF_images/116854_A_8_4_rna_selected.jpg|HPA IF]]

**结论**: 多源确认染色质/着丝粒定位。作为 SNF2 家族染色质重塑 ATPase，其染色质定位是功能必需的。

#### 3.2 蛋白大小评估
**评价**: 1250 aa，偏大。典型 SNF2 家族 ATPase 大小。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 41 |
| 主要研究方向 | 有丝分裂染色质分离, 着丝粒, 超细DNA桥 |

**主要研究方向**:
- SNF2 家族 DNA 转位酶/ATPase
- 有丝分裂染色体分离
- 超细 DNA 桥 (UFB) 的解离

**关键文献**:
1. Baumann et al. (2007). "PICH in chromosome segregation". PMID: 17276046
2. Biebricher et al. (2013). "PICH DNA translocase activity". PMID: 23893135
3. Nielsen et al. (2015). "PICH and BLM in UFB resolution". PMID: 25919578

**评价**: 研究较少（41篇），但功能极其明确——SNF2 染色质重塑 ATPase 直接作用于染色质。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| 平均 pLDDT | 62.1 |
| 有序区域 (pLDDT>70) 占比 | 51% |
| 可用 PDB 条目 | 5JNO |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERCC6L/ERCC6L-PAE.png]]

**评价**: AF 预测中等（SNF2 ATPase 域有序，但连接区域无序）。1个 PDB 实验结构。典型大蛋白特征。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| InterPro | SNF2 N-terminal domain (IPR000330) |
| InterPro | Helicase C-terminal (IPR001650) |
| InterPro | Helicase ATP-binding (IPR014001) |
| Pfam | SNF2_N, Helicase_C |

**染色质调控潜力分析**: SNF2 家族是经典染色质重塑 ATPase 家族（与 SWI/SNF, ISWI, CHD 同家族）。直接利用 ATP 水解能量进行 DNA 转位/染色质重塑。染色质调控潜力极高。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PLK1 | 1.00 | 有丝分裂激酶 | 是 |
| RMI1 | 0.97 | Bloom复合体 | 是 |
| TOP3A | 0.96 | 拓扑异构酶 | 是 |
| BLM | 0.95 | Bloom 解旋酶 | 是 |
| CENPI | 0.94 | 着丝粒蛋白 | 是 |

**已知复合体成员** (GO Cellular Component):
- Kinetochore (GO:0000776)
- Membrane (GO:0016020)

**PPI 互证分析**:
- PLK1 + BLM/TOP3A/RMI1 (Bloom 复合体) = 有丝分裂染色质分离核心网络
- 调控相关比例: 极高 (~80%)

**评价**: PPI 极其富集有丝分裂染色质调控因子，与 BLM 解旋酶和 PLK1 激酶互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF + PDB(5JNO) | SNF2 ATPase fold | 一致 |
| 结构域 | InterPro/Pfam | SNF2 染色质重塑家族 | 一致 |
| PPI | STRING + GO | 着丝粒/Bloom 复合体 | 一致 |
| 定位 | UniProt / GO | Centromere/Kinetochore | 一致 |

**互证加分明细**:
- SNF2 域 + GO Kinetochore 一致 (+0.5)
- PPI Bloom 复合体 + BLM/TOP3A/RMI1 一致 (+0.5)
- 多源一致染色质定位 (+0.5)
- 多项证据交叉验证 (+0.5)
- **总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: 4 / 5

**核心优势**:
1. SNF2 家族染色质重塑 ATPase（与 SWI/SNF 同家族）
2. 直接作用于染色质/DNA，功能极其明确
3. PPI 极富集着丝粒染色质调控因子
4. 研究新颖（41篇）

**风险/不确定性**:
1. 蛋白大（1250 aa）
2. 以有丝分裂功能为主，间期 TE 调控角色待确认

**下一步建议**:
- [ ] 检测 ERCC6L 在间期染色质上的结合（非仅着丝粒）
- [ ] 通过 ATPase 实验验证其染色质重塑活性
- [ ] 评估其在 TE 区域的可能调控角色

### 5. 数据来源
- UniProt: Q2NKX8 (https://www.uniprot.org/uniprotkb/Q2NKX8)
- AlphaFold: AF-Q2NKX8-F1 v6 (https://alphafold.ebi.ac.uk/entry/Q2NKX8)
- Protein Atlas: ERCC6L (https://www.proteinatlas.org/)
- PubMed: ERCC6L (https://pubmed.ncbi.nlm.nih.gov/)
- STRING: ERCC6L (https://string-db.org/)
- InterPro: Q2NKX8 (https://www.ebi.ac.uk/interpro/)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ERCC6L-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERCC6L/ERCC6L-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2NKX8 |
| SMART | SM00487;SM00490; |
| UniProt Domain [FT] | DOMAIN 109..277; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 464..620; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR014001;IPR001650;IPR027417;IPR038718;IPR049730;IPR000330;IPR050496; |
| Pfam | PF00271;PF00176; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186871-ERCC6L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PLK1 | Biogrid, Opencell | true |
| BRD2 | Opencell | false |
| EEF1AKMT3 | Bioplex | false |
| HTT | Intact | false |
| LMO4 | Intact | false |
| MINK1 | Opencell | false |
| PASK | Opencell | false |
| RB1CC1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
