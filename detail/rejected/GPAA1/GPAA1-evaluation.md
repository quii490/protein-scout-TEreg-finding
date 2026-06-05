---
type: protein-evaluation
gene: "GPAA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPAA1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPAA1 / GAA1 |
| 蛋白名称 | GPI-anchor transamidase component GPAA1 |
| 蛋白大小 | 621 aa / 67.6 kDa |
| UniProt ID | O43292 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum, Cytosol; 额外: Centrosome, Mitochondria; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 621 aa / 67.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.2; PDB: 7W72, 7WLD, 8IMX, 8IMY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007246; Pfam: PF04114 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Cytosol; 额外: Centrosome, Mitochondria | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- GPI-anchor transamidase complex (GO:0042765)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

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
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 90.5% |
| 可用 PDB 条目 | 7W72, 7WLD, 8IMX, 8IMY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7W72, 7WLD, 8IMX, 8IMY）+ AlphaFold高质量预测（pLDDT=87.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007246; Pfam: PF04114 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PIGK | 0.999 | 0.997 | — |
| PIGU | 0.999 | 0.974 | — |
| PIGT | 0.999 | 0.997 | — |
| PIGS | 0.999 | 0.996 | — |
| PIGO | 0.977 | 0.067 | — |
| PGAP1 | 0.964 | 0.067 | — |
| PIGF | 0.916 | 0.000 | — |
| PIGV | 0.754 | 0.095 | — |
| PIGL | 0.744 | 0.000 | — |
| PIGB | 0.731 | 0.070 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF3E | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PRR13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GRIK5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| YIPF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TREH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GABRG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SOAT1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ACAP2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| STOM | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 7W72, 7WLD, 8IMX, 8IMY | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Endoplasmic reticulum, Cytosol; 额外: Centrosome, Mi | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPAA1 — GPI-anchor transamidase component GPAA1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小621 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43292
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197858-GPAA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPAA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43292
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43292-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000197858-GPAA1/subcellular

![](https://images.proteinatlas.org/77224/1605_D4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77224/1605_D4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/77224/1615_D4_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/77224/1615_D4_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/77224/1719_C7_18_cr5804b8c2a143e_blue_red_green.jpg)
![](https://images.proteinatlas.org/77224/1719_C7_8_cr5804b8b8d4d43_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
