---
type: protein-evaluation
gene: "VBP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## VBP1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VBP1 |
| 蛋白名称 | VBP1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | VBP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genomic organization and chromosomal localization of the human CUL2 gene and the role of von Hippel-Lindau tumor suppressor-binding protein (CUL2 and VBP1) mutation and loss in renal-cell carcinoma development.. *Genes, chromosomes & cancer*. PMID: 10441001
2. VBP1 negatively regulates CHIP and selectively inhibits the activity of hypoxia-inducible factor (HIF)-1α but not HIF-2α.. *The Journal of biological chemistry*. PMID: 37201586
3. Characterization of the gene (VBP1) and transcript for the von Hippel-Lindau binding protein and isolation of the highly conserved murine homologue.. *Genomics*. PMID: 9339366
4. VBP1 modulates Wnt/β-catenin signaling by mediating the stability of the transcription factors TCF/LEFs.. *The Journal of biological chemistry*. PMID: 32989053
5. Expression of the von Hippel-Lindau-binding protein-1 (Vbp1) in fetal and adult mouse tissues.. *Human molecular genetics*. PMID: 9931330

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PFDN6 | 0.999 | 0.997 | — |
| PFDN2 | 0.999 | 0.997 | — |
| PFDN5 | 0.999 | 0.997 | — |
| PFDN4 | 0.999 | 0.997 | — |
| PFDN1 | 0.999 | 0.997 | — |
| CCT8 | 0.982 | 0.920 | — |
| CCT6A | 0.975 | 0.924 | — |
| CCT2 | 0.974 | 0.886 | — |
| CCT4 | 0.972 | 0.849 | — |
| TCP1 | 0.971 | 0.820 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| ORF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| PRPF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PAN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PPP2CB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| TUBA3E | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Tubb4b | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| MAPK7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| TUBA1A | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Cytosol; 额外: Vesicles | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. VBP1 — VBP1 (UniProt未获取)，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/VBP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155959-VBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/VBP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000155959-VBP1/subcellular

![](https://images.proteinatlas.org/23230/236_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23230/236_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23230/237_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23230/237_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23230/268_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23230/268_B6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
