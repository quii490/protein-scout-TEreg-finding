---
type: protein-evaluation
gene: "EXOSC8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOSC8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOSC8 / OIP2, RRP43 |
| 蛋白名称 | Exosome complex component RRP43 |
| 蛋白大小 | 276 aa / 30.0 kDa |
| UniProt ID | Q96B26 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC8/IF_images/HEL_1.jpg|HEL]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC8/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center, Mitotic chromosome; 额外: Nucleopla; UniProt: Cytoplasm; Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 276 aa / 30.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=85.9; PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001247, IPR015847, IPR036345, IPR050590, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Mitotic chromosome; 额外: Nucleoplasm, Vesicles, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytoplasmic exosome (RNase complex) (GO:0000177)
- cytosol (GO:0005829)
- exosome (RNase complex) (GO:0000178)
- fibrillar center (GO:0001650)
- nuclear exosome (RNase complex) (GO:0000176)
- nucleolar exosome (RNase complex) (GO:0101019)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OIP2, RRP43 |

**关键文献**:
1. Pontocerebellar Hypoplasia Type 1 and Associated Neuronopathies.. *Genes*. PMID: 40428407
2. The RNA Exosome and Human Disease.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 31768969
3. ZNF692 organizes a hub specialized in 40S ribosomal subunit maturation enhancing translation in rapidly proliferating cells.. *Cell reports*. PMID: 37851577
4. EXOSC8 mutations alter mRNA metabolism and cause hypomyelination with spinal muscular atrophy and cerebellar hypoplasia.. *Nature communications*. PMID: 24989451
5. EXOSC8 promotes colorectal cancer tumorigenesis via regulating ribosome biogenesis-related processes.. *Oncogene*. PMID: 36348012

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.9 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 64.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 95.3% |
| 可用 PDB 条目 | 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC8/EXOSC8-PAE.png]]

**评价**: PDB实验结构（2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P）+ AlphaFold极高置信度预测（pLDDT=85.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001247, IPR015847, IPR036345, IPR050590, IPR027408; Pfam: PF01138, PF03725 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC10 | 0.999 | 0.999 | — |
| EXOSC9 | 0.999 | 0.997 | — |
| DIS3 | 0.999 | 0.999 | — |
| C1D | 0.999 | 0.992 | — |
| MPHOSPH6 | 0.999 | 0.979 | — |
| EXOSC1 | 0.999 | 0.997 | — |
| EXOSC2 | 0.999 | 0.997 | — |
| EXOSC3 | 0.999 | 0.998 | — |
| DIS3L | 0.999 | 0.998 | — |
| EXOSC4 | 0.999 | 0.999 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000374354.3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| ZFP36 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| DIS3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| LSM1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| LSM7 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| XRN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.9 + PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M,  | pLDDT=85.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, nucleolus / Nucleoli fibrillar center, Mitotic chromosome; 额外: | 一致 |
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
1. EXOSC8 — Exosome complex component RRP43，非常新颖，仅有少数基础研究。
2. 蛋白大小276 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96B26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120699-EXOSC8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOSC8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96B26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC8/EXOSC8-PAE.png]]




