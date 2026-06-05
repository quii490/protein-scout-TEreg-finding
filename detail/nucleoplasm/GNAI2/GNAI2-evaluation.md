---
type: protein-evaluation
gene: "GNAI2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNAI2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNAI2 / GNAI2B |
| 蛋白名称 | Guanine nucleotide-binding protein G(i) subunit alpha-2 |
| 蛋白大小 | 355 aa / 40.5 kDa |
| UniProt ID | P04899 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane, Basal body; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing c |
| 蛋白大小 | 10/10 | ×1 | 10 | 355 aa / 40.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.1; PDB: 6D9H, 7F8V, 7LD3, 7LD4, 7WV9, 7WVV, 7WVW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001408, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane, Basal body | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cell membrane; Membra... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell body (GO:0044297)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- extracellular exosome (GO:0070062)
- extracellular vesicle (GO:1903561)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 87.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 96.9% |
| 可用 PDB 条目 | 6D9H, 7F8V, 7LD3, 7LD4, 7WV9, 7WVV, 7WVW, 7WVX, 7WVY, 7XXI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6D9H, 7F8V, 7LD3, 7LD4, 7WV9, 7WVV, 7WVW, 7WVX, 7WVY, 7XXI）+ AlphaFold极高置信度预测（pLDDT=94.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001408, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB1 | 0.999 | 0.990 | — |
| ADORA1 | 0.994 | 0.932 | — |
| CNR1 | 0.993 | 0.932 | — |
| GNAI3 | 0.992 | 0.844 | — |
| DRD2 | 0.985 | 0.485 | — |
| GNB2 | 0.982 | 0.701 | — |
| GNB4 | 0.977 | 0.885 | — |
| GNAI1 | 0.975 | 0.621 | — |
| GNG2 | 0.974 | 0.908 | — |
| GPSM1 | 0.969 | 0.264 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| ACTB | psi-mi:"MI:0071"(molecular sieving) | pubmed:15047060 |
| MDFI | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| TUBA4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| EBI-5327879 | psi-mi:"MI:0013"(biophysical) | pubmed:22106087|imex:IM-16985 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| NPM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 6D9H, 7F8V, 7LD3, 7LD4, 7WV9,  | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, microtubule or / Cytosol; 额外: Nucleoplasm, Plasma membrane, Basal b | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GNAI2 — Guanine nucleotide-binding protein G(i) subunit alpha-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小355 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P04899
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114353-GNAI2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNAI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P04899
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000114353-GNAI2/subcellular

![](https://images.proteinatlas.org/7704/2131_G3_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/7704/2131_G3_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/7704/2151_B4_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/7704/2151_B4_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/7704/2168_D8_22_blue_red_green.jpg)
![](https://images.proteinatlas.org/7704/2168_D8_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P04899-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
