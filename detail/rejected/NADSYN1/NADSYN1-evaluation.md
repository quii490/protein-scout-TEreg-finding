---
type: protein-evaluation
gene: "NADSYN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NADSYN1 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NADSYN1 |
| 蛋白名称 | NADSYN1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | NADSYN1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=98 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.5/180** | |
| **归一化总分** | | | **41.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 98 |
| PubMed broad count | 98 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Metabolic Alterations in NADSYN1-Deficient Cells.. *Metabolites*. PMID: 38132878
2. A metabolic signature for NADSYN1-dependent congenital NAD deficiency disorder.. *J Clin Invest*. PMID: 38357931
3. Genetic variants of vitamin D metabolism-related DHCR7/NADSYN1 locus and CYP2R1 gene are associated with clinical features of Parkinson's disease.. *Int J Neurosci*. PMID: 32938288
4. Differential expression and methylation patterns of NFATC1, NADSYN1 and JAK3 gene in equine chondrocytes expanded in monolayer culture.. *Res Vet Sci*. PMID: 35917593
5. Disruptive NADSYN1 Variants Implicated in Congenital Vertebral Malformations.. *Genes (Basel)*. PMID: 34681008

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.9 |
| 高置信度残基 (pLDDT>90) 占比 | 92.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 98.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.9，有序区 98.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q92900 | psi-mi:"MI:0018" | - |
| intact:EBI-741027 | psi-mi:"MI:0398" | - |
| uniprotkb:Q6IA69 | psi-mi:"MI:0398" | - |
| chebi:"CHEBI:18348" | psi-mi:"MI:0096" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q96HA8 | psi-mi:"MI:0397" | - |
| uniprotkb:P27658 | psi-mi:"MI:1356" | - |
| uniprotkb:Q96JP2 | psi-mi:"MI:0397" | - |
| uniprotkb:P31273 | psi-mi:"MI:1356" | - |
| uniprotkb:Q02930-3 | psi-mi:"MI:1112" | - |
| uniprotkb:O43559 | psi-mi:"MI:1356" | - |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.9 + PDB: 无 | pLDDT=95.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

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
1. NADSYN1 — NADSYN1 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 98 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/NADSYN1
- Protein Atlas: https://www.proteinatlas.org/search/NADSYN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NADSYN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/NADSYN1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000172890-NADSYN1/subcellular

![](https://images.proteinatlas.org/17798/620_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17798/620_G9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17798/623_G9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17798/623_G9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38524/2166_D7_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/38524/2166_D7_30_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
