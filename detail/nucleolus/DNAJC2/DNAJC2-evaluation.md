---
type: protein-evaluation
gene: "DNAJC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC2 / MPHOSPH11, MPP11, ZRF1 |
| 蛋白名称 | DnaJ homolog subfamily C member 2 |
| 蛋白大小 | 621 aa / 72.0 kDa |
| UniProt ID | Q99543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 621 aa / 72.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.0; PDB: 2M2E, 6CGH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR018253, IPR009057, IPR036869, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MPHOSPH11, MPP11, ZRF1 |

**关键文献**:
1. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
2. Association of specific gene mutations derived from machine learning with survival in lung adenocarcinoma.. *PloS one*. PMID: 30419062
3. Genetic Analysis of HSP40/DNAJ Family Genes in Parkinson's Disease: a Large Case-Control Study.. *Molecular neurobiology*. PMID: 35715682
4. Genome-wide identification of alternative splicing associated with histone deacetylase inhibitor in cutaneous T-cell lymphomas.. *Frontiers in genetics*. PMID: 36147491
5. The diversity of the DnaJ/Hsp40 family, the crucial partners for Hsp70 chaperones.. *Cellular and molecular life sciences : CMLS*. PMID: 16952052

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.0 |
| 高置信度残基 (pLDDT>90) 占比 | 54.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 5.8% |
| 有序区域 (pLDDT>70) 占比 | 85.0% |
| 可用 PDB 条目 | 2M2E, 6CGH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2M2E, 6CGH）+ AlphaFold高质量预测（pLDDT=85.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR018253, IPR009057, IPR036869, IPR017930; Pfam: PF00226, PF23082, PF16717 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA14 | 0.998 | 0.837 | — |
| HSPA4 | 0.986 | 0.274 | — |
| HSPA8 | 0.951 | 0.599 | — |
| DNAJB4 | 0.865 | 0.076 | — |
| ZC3H15 | 0.844 | 0.526 | — |
| RPL31 | 0.820 | 0.240 | — |
| HSPA1L | 0.812 | 0.504 | — |
| HSPA1A | 0.806 | 0.504 | — |
| HSPA1B | 0.803 | 0.504 | — |
| HSPA6 | 0.800 | 0.504 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.0 + PDB: 2M2E, 6CGH | pLDDT=85.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC2 — DnaJ homolog subfamily C member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小621 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105821-DNAJC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
