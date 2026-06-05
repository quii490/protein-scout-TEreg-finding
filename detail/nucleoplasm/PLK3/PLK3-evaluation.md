---
type: protein-evaluation
gene: "PLK3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PLK3 — REJECTED (研究热度过高 (PubMed strict=152，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLK3 / CNK, FNK, PRK |
| 蛋白名称 | Serine/threonine-protein kinase PLK3 |
| 蛋白大小 | 646 aa / 71.6 kDa |
| UniProt ID | Q9H4B4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Nucleus, nucleolus; Golgi apparatus; Cyt |
| 蛋白大小 | 10/10 | ×1 | 10 | 646 aa / 71.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=152 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.7; PDB: 4B6L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR042703, IPR033701, IPR033695, IPR000 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleolus; Golgi apparatus; Cytoplasm, cytoskeleton, microtubule organi... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- Golgi stack (GO:0005795)
- kinetochore (GO:0000776)
- neuronal cell body (GO:0043025)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 152 |
| PubMed broad count | 291 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CNK, FNK, PRK |

**关键文献**:
1. Finding Plk3.. *Cell cycle (Georgetown, Tex.)*. PMID: 17568195
2. ALDH1A1 drives prostate cancer metastases and radioresistance by interplay with AR- and RAR-dependent transcription.. *Theranostics*. PMID: 38169509
3. The role of Plk3 in oncogenesis.. *Oncogene*. PMID: 25915845
4. Pachytene piRNAs control discrete meiotic events during spermatogenesis and restrict gene expression in space and time.. *Science advances*. PMID: 39356768
5. Polo-like kinase 3, hypoxic responses, and tumorigenesis.. *Cell cycle (Georgetown, Tex.)*. PMID: 28857653

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 58.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 20.7% |
| 有序区域 (pLDDT>70) 占比 | 75.4% |
| 可用 PDB 条目 | 4B6L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=79.7，有序区 75.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR042703, IPR033701, IPR033695, IPR000959; Pfam: PF00069, PF00659 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| VRK1 | psi-mi:"MI:0096"(pull down) | imex:IM-9274|pubmed:19103756 |
| 22249" | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-9274|pubmed:19103756 |
| PRNP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18482256|imex:IM-19010 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| RAD52 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POU2F1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| RNF141 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LSM5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MFF | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 4B6L | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, nucleolus; Golgi appa / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PLK3 — Serine/threonine-protein kinase PLK3，研究基础较多，新颖性有限。
2. 蛋白大小646 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 152 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 152 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4B4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173846-PLK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4B4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4B4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
