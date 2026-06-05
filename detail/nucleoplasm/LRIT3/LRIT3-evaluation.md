---
type: protein-evaluation
gene: "LRIT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRIT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRIT3 |
| 蛋白名称 | Leucine-rich repeat, immunoglobulin-like domain and transmembrane domain-containing protein 3 |
| 蛋白大小 | 679 aa / 74.8 kDa |
| UniProt ID | Q3SXY7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria, Cytosol; UniProt: Cell projection, dendrite; Perikaryon; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 679 aa / 74.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003961, IPR036116, IPR007110, IPR036179, IPR013 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.5/180** | |
| **归一化总分** | | | **58.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria, Cytosol | Approved |
| UniProt | Cell projection, dendrite; Perikaryon; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell tip (GO:0051286)
- dendrite (GO:0030425)
- endoplasmic reticulum membrane (GO:0005789)
- perikaryon (GO:0043204)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. LRIT3 is Required for Nyctalopin Expression and Normal ON and OFF Pathway Signaling in the Retina.. *eNeuro*. PMID: 31959619
2. Substantial restoration of night vision in adult mice with congenital stationary night blindness.. *Molecular therapy. Methods & clinical development*. PMID: 34401402
3. Gene augmentation therapy treats mature mice with complete congenital stationary night blindness (cCSNB), improving retinal function and visual acuity.. *bioRxiv : the preprint server for biology*. PMID: 40766553
4. Presynaptic Expression of LRIT3 Transsynaptically Organizes the Postsynaptic Glutamate Signaling Complex Containing TRPM1.. *Cell reports*. PMID: 31189098
5. Extended functional rescue following AAV gene therapy in a canine model of LRIT3-congenital stationary night blindness.. *Vision research*. PMID: 37220680

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.6 |
| 高置信度残基 (pLDDT>90) 占比 | 34.2% |
| 置信残基 (pLDDT 70-90) 占比 | 24.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 58.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.6），有序残基占 58.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR007110, IPR036179, IPR013783; Pfam: PF13927, PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BIRC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPR107 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NCDN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| rep | psi-mi:"MI:1313"(proximity labelling technology) | pubmed:34232536|imex:IM-29365 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 5
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.6 + PDB: 无 | pLDDT=69.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, dendrite; Perikaryon; Endoplasmic / Nucleoplasm, Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 5 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRIT3 — Leucine-rich repeat, immunoglobulin-like domain and transmembrane domain-containing protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小679 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3SXY7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183423-LRIT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRIT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3SXY7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000183423-LRIT3/subcellular

![](https://images.proteinatlas.org/13454/102_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/13454/102_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/13454/103_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/13454/103_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/13454/104_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/13454/104_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3SXY7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
