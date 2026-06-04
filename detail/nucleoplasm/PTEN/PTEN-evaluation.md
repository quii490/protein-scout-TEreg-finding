---
type: protein-evaluation
gene: "PTEN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTEN — REJECTED (研究热度过高 (PubMed strict=14754，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTEN / MMAC1, TEP1 |
| 蛋白名称 | Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase and dual-specificity protein phosphatase PTEN |
| 蛋白大小 | 403 aa / 47.2 kDa |
| UniProt ID | P60484 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Mid piece, Principal piece; UniProt: Cytoplasm; Nucleus; Nucleus, PML body; Cell projection, dend |
| 蛋白大小 | 10/10 | ×1 | 10 | 403 aa / 47.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=14754 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.0; PDB: 1D5R, 2KYL, 4O1V, 5BUG, 5BZX, 5BZZ, 7JTX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017361, IPR035892, IPR051281, IPR029021, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Mid piece, Principal piece | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus, PML body; Cell projection, dendritic spine; Postsynaptic density; Secre... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- cell projection (GO:0042995)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- extracellular region (GO:0005576)
- myelin sheath adaxonal region (GO:0035749)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14754 |
| PubMed broad count | 27991 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MMAC1, TEP1 |

**关键文献**:
1. Mechanisms of PTEN loss in cancer: It's all about diversity.. *Seminars in cancer biology*. PMID: 30738865
2. Characterization of cryptic splicing in germline PTEN intronic variants in Cowden syndrome.. *Human mutation*. PMID: 28677221
3. PTEN: A Novel Diabetes Nephropathy Protective Gene Related to Cellular Senescence.. *International journal of molecular sciences*. PMID: 40243723
4. PTEN proteoforms in biology and disease.. *Cellular and molecular life sciences : CMLS*. PMID: 28289760
5. PTEN defects in cancer, from gene to protein molecular causes and therapeutic targets.. *Discover oncology*. PMID: 40877546

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.0 |
| 高置信度残基 (pLDDT>90) 占比 | 68.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 17.1% |
| 有序区域 (pLDDT>70) 占比 | 77.6% |
| 可用 PDB 条目 | 1D5R, 2KYL, 4O1V, 5BUG, 5BZX, 5BZZ, 7JTX, 7JUK, 7JUL, 7JVX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1D5R, 2KYL, 4O1V, 5BUG, 5BZX, 5BZZ, 7JTX, 7JUK, 7JUL, 7JVX）+ AlphaFold极高置信度预测（pLDDT=83.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017361, IPR035892, IPR051281, IPR029021, IPR045101; Pfam: PF10409, PF22785 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TP53 | 0.999 | 0.748 | — |
| MAGI2 | 0.998 | 0.523 | — |
| PIK3R1 | 0.997 | 0.554 | — |
| DLG1 | 0.996 | 0.636 | — |
| PTK2 | 0.995 | 0.801 | — |
| PIK3CA | 0.995 | 0.134 | — |
| MAST2 | 0.993 | 0.948 | — |
| PREX2 | 0.990 | 0.000 | — |
| SPOP | 0.990 | 0.972 | — |
| AKT1 | 0.988 | 0.648 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000518242.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11846|pubmed:17218262 |
| ENSMUSP00000013807.8 | psi-mi:"MI:0404"(comigration in non denaturing gel | pubmed:24766807|imex:IM-22849 |
| Epac | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Zn72D | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ten-m | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Magi2 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Magi3 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Dlg1 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Mast2 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| MAST3 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.0 + PDB: 1D5R, 2KYL, 4O1V, 5BUG, 5BZX,  | pLDDT=83.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, PML body; Cell projec / Nucleoplasm, Cytosol; 额外: Mid piece, Principal pie | 一致 |
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
1. PTEN — Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase and dual-specificity protein phosphatase PTEN，研究基础较多，新颖性有限。
2. 蛋白大小403 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14754 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 14754 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P60484
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171862-PTEN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTEN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60484
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
