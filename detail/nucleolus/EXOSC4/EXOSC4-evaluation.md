---
type: protein-evaluation
gene: "EXOSC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOSC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOSC4 / RRP41, SKI6 |
| 蛋白名称 | Exosome complex component RRP41 |
| 蛋白大小 | 245 aa / 26.4 kDa |
| UniProt ID | Q9NPD3 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC4/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC4/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Vesicles; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 245 aa / 26.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.2; PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001247, IPR015847, IPR036345, IPR027408, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Vesicles | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic exosome (RNase complex) (GO:0000177)
- cytosol (GO:0005829)
- euchromatin (GO:0000791)
- exosome (RNase complex) (GO:0000178)
- nuclear exosome (RNase complex) (GO:0000176)
- nucleolar exosome (RNase complex) (GO:0101019)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RRP41, SKI6 |

**关键文献**:
1. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539
2. A biallelic variant of the RNA exosome gene, EXOSC4, associated with neurodevelopmental defects impairs RNA exosome function and translation.. *The Journal of biological chemistry*. PMID: 39009343
3. Ribosomal Protein RPL29 Promotes Hepatocellular Carcinoma Progression Through Regulation the Expression of Exosome Component 4.. *Biological procedures online*. PMID: 41484694
4. Identification EXOSC4 as a novel autoantigen of interstitial lung disease in rheumatoid arthritis.. *Journal of translational medicine*. PMID: 40640919
5. miR‑148 family members are putative biomarkers for sepsis.. *Molecular medicine reports*. PMID: 31059023

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.2 |
| 高置信度残基 (pLDDT>90) 占比 | 69.8% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 97.1% |
| 可用 PDB 条目 | 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC4/EXOSC4-PAE.png]]

**评价**: PDB实验结构（2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P）+ AlphaFold极高置信度预测（pLDDT=90.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001247, IPR015847, IPR036345, IPR027408, IPR020568; Pfam: PF01138, PF03725 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC3 | 0.999 | 0.999 | — |
| EXOSC2 | 0.999 | 0.999 | — |
| MPHOSPH6 | 0.999 | 0.974 | — |
| EXOSC1 | 0.999 | 0.999 | — |
| DIS3 | 0.999 | 0.999 | — |
| EXOSC10 | 0.999 | 0.999 | — |
| EXOSC9 | 0.999 | 0.999 | — |
| EXOSC6 | 0.999 | 0.998 | — |
| EXOSC5 | 0.999 | 0.998 | — |
| EXOSC8 | 0.999 | 0.999 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| DXO | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| SKIC2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC9 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| SMPD4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| TSEN15 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| FAHD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| NEK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.2 + PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M,  | pLDDT=90.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus; Nucleus, n / Nucleoplasm, Cytosol; 额外: Vesicles | 一致 |
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
1. EXOSC4 — Exosome complex component RRP41，非常新颖，仅有少数基础研究。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPD3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178896-EXOSC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOSC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPD3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC4/EXOSC4-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NPD3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001247;IPR015847;IPR036345;IPR027408;IPR020568;IPR050080; |
| Pfam | PF01138;PF03725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178896-EXOSC4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DIS3L | Biogrid, Bioplex | true |
| EXOSC1 | Intact, Biogrid, Bioplex | true |
| EXOSC10 | Intact, Biogrid | true |
| EXOSC2 | Intact, Biogrid, Bioplex | true |
| EXOSC3 | Intact, Biogrid, Bioplex | true |
| EXOSC5 | Biogrid, Bioplex | true |
| EXOSC6 | Biogrid, Bioplex | true |
| EXOSC7 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
