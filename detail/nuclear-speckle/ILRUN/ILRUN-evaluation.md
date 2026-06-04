---
type: protein-evaluation
gene: "ILRUN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ILRUN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ILRUN / C6orf106 |
| 蛋白名称 | Protein ILRUN |
| 蛋白大小 | 298 aa / 32.9 kDa |
| UniProt ID | Q9H6K1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Centrosome, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 298 aa / 32.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=71.2; PDB: 6VHI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039517, IPR013783, IPR032350, IPR009060; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Centrosome, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- phagophore assembly site (GO:0000407)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf106 |

**关键文献**:
1. ILRUN Downregulates ACE2 Expression and Blocks Infection of Human Cells by SARS-CoV-2.. *Journal of virology*. PMID: 33963054
2. ILRUN Promotes Atherosclerosis Through Lipid-Dependent and Lipid-Independent Factors.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 35861973
3. ILRUN, a Human Plasma Lipid GWAS Locus, Regulates Lipoprotein Metabolism in Mice.. *Circulation research*. PMID: 32912065
4. Gene-based association analysis identified a novel gene associated with systemic lupus erythematosus.. *Annals of human genetics*. PMID: 34145571
5. Molecular characterisation of ILRUN, a novel inhibitor of proinflammatory and antimicrobial cytokines.. *Heliyon*. PMID: 32518853

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 32.6% |
| 有序区域 (pLDDT>70) 占比 | 56.1% |
| 可用 PDB 条目 | 6VHI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=71.2，有序区 56.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039517, IPR013783, IPR032350, IPR009060; Pfam: PF16158, PF14555 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPDEF | 0.597 | 0.000 | — |
| UHRF1BP1 | 0.595 | 0.000 | — |
| SMIM29 | 0.577 | 0.000 | — |
| NUDT3 | 0.551 | 0.000 | — |
| HSPBP1 | 0.451 | 0.421 | — |
| C17orf67 | 0.446 | 0.000 | — |
| SNRPC | 0.428 | 0.000 | — |
| RSRC2 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPSA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| HSPBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Map3k1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2V1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2N | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| hspa1a_hspa1b_human-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BAG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 11
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 6VHI | pLDDT=71.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 8 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ILRUN — Protein ILRUN，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小298 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6K1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196821-ILRUN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ILRUN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6K1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
