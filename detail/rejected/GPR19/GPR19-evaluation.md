---
type: protein-evaluation
gene: "GPR19"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR19 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR19 |
| 蛋白名称 | Probable G-protein coupled receptor 19 |
| 蛋白大小 | 415 aa / 47.7 kDa |
| UniProt ID | Q15760 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 415 aa / 47.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452, IPR047829; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- neuron projection (GO:0043005)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Expression of G protein-coupled receptor GPR19 in normal and neoplastic human tissues.. *Scientific reports*. PMID: 37923782
2. Attenuation of fibroblast activation and fibrosis by adropin in systemic sclerosis.. *Science translational medicine*. PMID: 38536934
3. G-protein coupled receptor 19 (GPR19) knockout mice display sex-dependent metabolic dysfunction.. *Scientific reports*. PMID: 37061564
4. G protein-coupled receptor GPR19 regulates E-cadherin expression and invasion of breast cancer cells.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 28476646
5. Intersection of the Orphan G Protein-Coupled Receptor, GPR19, with the Aging Process.. *International journal of molecular sciences*. PMID: 36362387

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 35.4% |
| 置信残基 (pLDDT 70-90) 占比 | 29.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 22.7% |
| 有序区域 (pLDDT>70) 占比 | 64.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.4，有序区 64.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR047829; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ENHO | 0.903 | 0.000 | — |
| ETV6 | 0.736 | 0.000 | — |
| CDKN1B | 0.572 | 0.000 | — |
| CREBL2 | 0.528 | 0.000 | — |
| MTFR1 | 0.520 | 0.000 | — |
| GPR82 | 0.515 | 0.000 | — |
| GPR22 | 0.467 | 0.000 | — |
| GPR88 | 0.456 | 0.000 | — |
| CNTN6 | 0.453 | 0.044 | — |
| ZNF396 | 0.435 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 无 | pLDDT=74.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. GPR19 — Probable G-protein coupled receptor 19，非常新颖，仅有少数基础研究。
2. 蛋白大小415 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15760
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183150-GPR19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15760
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15760-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
