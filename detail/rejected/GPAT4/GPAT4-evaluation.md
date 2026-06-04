---
type: protein-evaluation
gene: "GPAT4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPAT4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPAT4 / AGPAT6, TSARG7 |
| 蛋白名称 | Glycerol-3-phosphate acyltransferase 4 |
| 蛋白大小 | 456 aa / 52.1 kDa |
| UniProt ID | Q86UL3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 456 aa / 52.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045252, IPR002123; Pfam: PF01553 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 88 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AGPAT6, TSARG7 |

**关键文献**:
1. GPAT4 sustains endoplasmic reticulum homeostasis in endocardial cells and safeguards heart development.. *Nature communications*. PMID: 40199910
2. Organelle bridges and nanodomain partitioning govern targeting of membrane-embedded proteins to lipid droplets.. *bioRxiv : the preprint server for biology*. PMID: 40894689
3. Function identification of Arabidopsis GPAT4 and GPAT8 in the biosynthesis of suberin and cuticular wax.. *Plant science : an international journal of experimental plant biology*. PMID: 38036221
4. Hippocampal Glycerol-3-Phosphate Acyltransferases 4 and BDNF in the Progress of Obesity-Induced Depression.. *Frontiers in endocrinology*. PMID: 34054732
5. Functional analysis of the GPAT4 gene mutation predicted to affect splicing.. *Animal biotechnology*. PMID: 37906284

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 48.2% |
| 置信残基 (pLDDT 70-90) 占比 | 39.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 87.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 87.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045252, IPR002123; Pfam: PF01553 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPAM | 0.992 | 0.000 | — |
| GPAT2 | 0.981 | 0.000 | — |
| MBOAT2 | 0.958 | 0.169 | — |
| GPD1 | 0.932 | 0.000 | — |
| GPD1L | 0.932 | 0.000 | — |
| GK2 | 0.920 | 0.049 | — |
| AGPAT1 | 0.918 | 0.000 | — |
| GK | 0.916 | 0.049 | — |
| GPD2 | 0.915 | 0.000 | — |
| AGK | 0.908 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sams | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HSD17B7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| Q8W4N0 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| GSDME | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPAT4 — Glycerol-3-phosphate acyltransferase 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小456 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UL3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158669-GPAT4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPAT4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UL3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
