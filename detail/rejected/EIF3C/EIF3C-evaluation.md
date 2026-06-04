---
type: protein-evaluation
gene: "EIF3C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3C — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3C |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit C |
| 蛋白大小 | 913 aa / 105.3 kDa |
| UniProt ID | Q99613 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 913 aa / 105.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=92 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.2; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.5/180** | |
| **归一化总分** | | | **38.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 92 |
| PubMed broad count | 92 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Novel insights into the assembly of the yeast translation initiation multifactor complex: The critical role of eIF5.. *Protein Sci*. PMID: 41944562
2. Circ-Eif3c Carried by M2 Macrophage-Derived Exosomes Mitigates Asthma Progression via miR-15a-5p/GSS/SOCS6 Axis Inhibition.. *Mediators Inflamm*. PMID: 41783090
3. The promoting roles of GLP1R and GIPR in stemness maintenance and multiple lineage-specific differentiation of PDLSCs.. *Cell Mol Biol Lett*. PMID: 41673566
4. Structural insights into the role of eIF3 in translation mediated by the HCV IRES.. *Proc Natl Acad Sci U S A*. PMID: 41337487
5. Effects of increasing light intensities on the cell growth and the RNA m(6)A upstream regulatory factors in a strain of Alexandrium pacificum.. *Harmful Algae*. PMID: 40935533

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 12.9% |
| 置信残基 (pLDDT 70-90) 占比 | 51.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 64.6% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=71.2，有序区 64.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3A | 0.000 | 0.000 | — |
| EIF3L | 0.000 | 0.000 | — |
| EIF3B | 0.000 | 0.000 | — |
| EIF3J | 0.000 | 0.000 | — |
| EIF3D | 0.000 | 0.000 | — |
| EIF3I | 0.000 | 0.000 | — |
| EIF3G | 0.000 | 0.000 | — |
| EIF3F | 0.000 | 0.000 | — |
| EIF1 | 0.000 | 0.000 | — |
| EIF3H | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A1ZAX1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:Q99613 | psi-mi:"MI:0071"(molecular sieving) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q7K4A8 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:B5DFC8 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Q2G4 | psi-mi:"MI:0096"(pull down) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 无 | pLDDT=71.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF3C — Eukaryotic translation initiation factor 3 subunit C，研究基础较多，新颖性有限。
2. 蛋白大小913 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 92 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99613
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184110-EIF3C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99613
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
