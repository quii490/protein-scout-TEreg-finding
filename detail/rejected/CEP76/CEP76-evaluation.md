---
type: protein-evaluation
gene: "CEP76"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEP76 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP76 / C18orf9 |
| 蛋白名称 | Centrosomal protein of 76 kDa |
| 蛋白大小 | 659 aa / 74.4 kDa |
| UniProt ID | Q8TAP6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 659 aa / 74.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.9; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052299, IPR028926, IPR056288, IPR056289, IPR056 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, c... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- protein-containing complex (GO:0032991)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf9 |

**关键文献**:
1. CEP76 impairment at the centrosome-cilium interface contributes to a spectrum of ciliopathies.. *Science advances*. PMID: 41105778
2. Identification and classification of papain-like cysteine proteinases.. *The Journal of biological chemistry*. PMID: 37164157
3. The centriole protein CEP76 negatively regulates PLK1 activity in the cytoplasm for proper mitotic progression.. *Journal of cell science*. PMID: 32878946
4. Genetic mutation of Cep76 results in male infertility due to abnormal sperm tail composition.. *Life science alliance*. PMID: 38570187
5. Evaluating the association between placenta DNA methylation and cognitive functions in the offspring.. *Translational psychiatry*. PMID: 39304652

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.9 |
| 高置信度残基 (pLDDT>90) 占比 | 68.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 85.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CEP76/CEP76-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=86.9，有序区 85.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052299, IPR028926, IPR056288, IPR056289, IPR056290; Pfam: PF15627, PF24652, PF24654 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCP110 | 0.937 | 0.747 | — |
| CEP290 | 0.868 | 0.771 | — |
| PLK1 | 0.846 | 0.000 | — |
| CEP97 | 0.838 | 0.676 | — |
| PLK4 | 0.657 | 0.230 | — |
| SASS6 | 0.648 | 0.000 | — |
| POC5 | 0.640 | 0.000 | — |
| HAUS2 | 0.637 | 0.000 | — |
| NEURL4 | 0.635 | 0.292 | — |
| CEP135 | 0.634 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000095149.3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DCTD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCNK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KIFBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SALL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GFAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PAICS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| COIL | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| GNAI1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.9 + PDB: 无 | pLDDT=86.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CEP76 — Centrosomal protein of 76 kDa，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小659 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAP6
- Protein Atlas: https://www.proteinatlas.org/search/CEP76
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP76
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAP6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-01 00:19:32


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CEP76/CEP76-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (uncertain)。来源: https://www.proteinatlas.org/ENSG00000101624-CEP76/subcellular

![](https://images.proteinatlas.org/39395/2072_E3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39395/2072_E3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39395/2096_H1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39395/2096_H1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/39395/2120_A11_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/39395/2120_A11_44_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
