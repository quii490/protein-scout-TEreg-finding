---
type: protein-evaluation
gene: "FBLIM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBLIM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBLIM1 / FBLP1 |
| 蛋白名称 | Filamin-binding LIM protein 1 |
| 蛋白大小 | 373 aa / 40.7 kDa |
| UniProt ID | Q8WUP2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cell Junctions, Focal adhesion sites; 额外: Nucleoli fibrillar; UniProt: Cell junction, focal adhesion; Cytoplasm, cytoskeleton, stre |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 40.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.5; PDB: 2K9U, 2W0P, 4P3W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions, Focal adhesion sites; 额外: Nucleoli fibrillar center | Enhanced |
| UniProt | Cell junction, focal adhesion; Cytoplasm, cytoskeleton, stress fiber | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cell periphery (GO:0071944)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- focal adhesion (GO:0005925)
- stress fiber (GO:0001725)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBLP1 |

**关键文献**:
1. Longitudinal transcriptomic and epigenetic analysis of the blood in two astronauts.. *Scientific reports*. PMID: 40715343
2. Update on the genetics of nonbacterial osteomyelitis in humans.. *Current opinion in rheumatology*. PMID: 29912021
3. Cytoskeletal-related genes function as checkpoints for the maintenance of VSMC contractile phenotype and prevent pathological remodeling in arterial diseases.. *Journal of advanced research*. PMID: 40516911
4. Integrative analyses of bulk and single-cell RNA-seq identified cancer-associated fibroblasts-related signature as a prognostic factor for immunotherapy in NSCLC.. *Cancer immunology, immunotherapy : CII*. PMID: 37010552
5. FBLIM1 drives bile duct ligation-induced liver fibrosis by regulating the TGF-β signaling pathway through WTAP-mediated m6A modification.. *International immunopharmacology*. PMID: 40334627

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.5 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 37.8% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 36.5% |
| 有序区域 (pLDDT>70) 占比 | 50.1% |
| 可用 PDB 条目 | 2K9U, 2W0P, 4P3W |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.5），有序残基占 50.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLNA | 0.999 | 0.958 | — |
| FLNC | 0.999 | 0.912 | — |
| FERMT2 | 0.999 | 0.299 | — |
| FLNB | 0.996 | 0.425 | — |
| VASP | 0.979 | 0.238 | — |
| FERMT3 | 0.928 | 0.043 | — |
| FERMT1 | 0.804 | 0.095 | — |
| CUTA | 0.737 | 0.734 | — |
| ILK | 0.710 | 0.000 | — |
| TLN1 | 0.624 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| let-756 | psi-mi:"MI:0018"(two hybrid) | pubmed:16672054|imex:IM-17216 |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| LMO3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CUTA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SHISA6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STAM2 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| FGFR1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| ACTMAP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| H3C1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.5 + PDB: 2K9U, 2W0P, 4P3W | pLDDT=66.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell junction, focal adhesion; Cytoplasm, cytoskel / Cell Junctions, Focal adhesion sites; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBLIM1 — Filamin-binding LIM protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162458-FBLIM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBLIM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUP2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
