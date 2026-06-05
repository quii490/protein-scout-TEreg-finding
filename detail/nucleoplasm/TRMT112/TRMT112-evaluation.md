---
type: protein-evaluation
gene: "TRMT112"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRMT112 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRMT112 |
| 蛋白名称 | Multifunctional methyltransferase subunit TRM112-like protein |
| 蛋白大小 | 125 aa / 14.2 kDa |
| UniProt ID | Q9UI30 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; 额外: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Cytoplasm, perinuclear region |
| 蛋白大小 | 8/10 | ×1 | 8 | 125 aa / 14.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.1; PDB: 6G4W, 6H1D, 6H1E, 6H2U, 6H2V, 6K0X, 6KHS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039127, IPR005651; Pfam: PF03966 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus, nucleoplasm; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- protein-containing complex (GO:0032991)
- tRNA (m2G10) methyltransferase complex (GO:0043528)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. N(6)-methyladenosine (m(6)A) in 18S rRNA promotes fatty acid metabolism and oncogenic transformation.. *Nature metabolism*. PMID: 35999469
2. N 2-methylguanosine modifications on human tRNAs and snRNA U6 are important for cell proliferation, protein translation and pre-mRNA splicing.. *Nucleic acids research*. PMID: 37283053
3. Complexoform-restricted covalent TRMT112 ligands that allosterically agonize METTL5.. *bioRxiv : the preprint server for biology*. PMID: 40475643
4. WBSCR22 and TRMT112 synergistically suppress cell proliferation, invasion and tumorigenesis in pancreatic cancer via transcriptional regulation of ISG15.. *International journal of oncology*. PMID: 35088887
5. Structural insight into HEMK2-TRMT112-mediated glutamine methylation.. *The Biochemical journal*. PMID: 32969463

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 79.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 94.4% |
| 可用 PDB 条目 | 6G4W, 6H1D, 6H1E, 6H2U, 6H2V, 6K0X, 6KHS, 6KMR, 6KMS, 6PED |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6G4W, 6H1D, 6H1E, 6H2U, 6H2V, 6K0X, 6KHS, 6KMR, 6KMS, 6PED）+ AlphaFold极高置信度预测（pLDDT=92.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039127, IPR005651; Pfam: PF03966 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| N6AMT1 | 0.999 | 0.995 | — |
| BUD23 | 0.999 | 0.997 | — |
| TRMT11 | 0.999 | 0.835 | — |
| METTL5 | 0.999 | 0.954 | — |
| ALKBH8 | 0.995 | 0.625 | — |
| TRMT9B | 0.981 | 0.940 | — |
| TRMT12 | 0.977 | 0.954 | — |
| DIMT1 | 0.929 | 0.800 | — |
| BYSL | 0.925 | 0.800 | — |
| HEMK1 | 0.917 | 0.738 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| UPF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| MED8 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HLH4C | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ada3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 6G4W, 6H1D, 6H1E, 6H2U, 6H2V,  | pLDDT=92.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Cytoplasm, perinuclear regio / Microtubules; 额外: Nucleoplasm | 一致 |
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
1. TRMT112 — Multifunctional methyltransferase subunit TRM112-like protein，非常新颖，仅有少数基础研究。
2. 蛋白大小125 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UI30
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173113-TRMT112/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRMT112
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UI30
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UI30-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
