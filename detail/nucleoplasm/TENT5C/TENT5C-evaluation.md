---
type: protein-evaluation
gene: "TENT5C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENT5C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TENT5C / FAM46C |
| 蛋白名称 | Terminal nucleotidyltransferase 5C |
| 蛋白大小 | 391 aa / 44.9 kDa |
| UniProt ID | Q5VWP2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 391 aa / 44.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.2; PDB: 6W36, 6W38, 6W3I, 6W3J, 8EQB |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012937; Pfam: PF07984 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM46C |

**关键文献**:
1. TENT5-mediated polyadenylation of mRNAs encoding secreted proteins is essential for gametogenesis in mice.. *Nature communications*. PMID: 38909026
2. Heme Metabolism-Related Gene TENT5C is a Prognostic Marker and Investigating Its Immunological Role in Colon Cancer.. *Pharmacogenomics and personalized medicine*. PMID: 38152411
3. The Immunity-malignancy equilibrium in multiple myeloma: lessons from oncogenic events in plasma cells.. *The FEBS journal*. PMID: 34117720
4. Mild hypothermia reduces lipopolysaccharide-induced microglial activation via down-regulation of Tent5c.. *Biochemical and biophysical research communications*. PMID: 38484570
5. 3' RNA Uridylation in Epitranscriptomics, Gene Regulation, and Disease.. *Frontiers in molecular biosciences*. PMID: 30057901

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 69.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 8.2% |
| 有序区域 (pLDDT>70) 占比 | 85.4% |
| 可用 PDB 条目 | 6W36, 6W38, 6W3I, 6W3J, 8EQB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6W36, 6W38, 6W3I, 6W3J, 8EQB）+ AlphaFold极高置信度预测（pLDDT=87.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012937; Pfam: PF07984 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLK4 | 0.922 | 0.910 | — |
| CEP192 | 0.832 | 0.800 | — |
| DIS3 | 0.791 | 0.000 | — |
| SP140 | 0.592 | 0.000 | — |
| TRIM58 | 0.590 | 0.000 | — |
| NRAS | 0.583 | 0.000 | — |
| BPGM | 0.557 | 0.000 | — |
| TRAF3 | 0.557 | 0.000 | — |
| GYPB | 0.533 | 0.000 | — |
| CNTROB | 0.519 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AP2B1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLK4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Rad23b | psi-mi:"MI:0096"(pull down) | imex:IM-13769|pubmed:20178748 |
| SF1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:26420826|imex:IM-23671 |
| MVP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| PRKN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| RHOXF2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SPOP | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 6W36, 6W38, 6W3I, 6W3J, 8EQB | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, micro / Nucleoplasm | 一致 |
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
1. TENT5C — Terminal nucleotidyltransferase 5C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小391 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VWP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183508-TENT5C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TENT5C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VWP2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
