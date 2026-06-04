---
type: protein-evaluation
gene: "OSBPL11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL11 / ORP11, OSBP12 |
| 蛋白名称 | Oxysterol-binding protein-related protein 11 |
| 蛋白大小 | 747 aa / 83.6 kDa |
| UniProt ID | Q9BXB4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Late endosome membrane; Golgi apparatus, trans-Golgi network |
| 蛋白大小 | 10/10 | ×1 | 10 | 747 aa / 83.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.1; PDB: 2D9X |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR001 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Late endosome membrane; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- late endosome membrane (GO:0031902)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ORP11, OSBP12 |

**关键文献**:
1. Severe neurodegenerative disease in brothers with homozygous mutation in POLR1A.. *European journal of human genetics : EJHG*. PMID: 28051070
2. High level expression of OSBPL11 is associated with atherosclerosis and Alzheimer's disease.. *Inflammation*. PMID: 40407857
3. The expression, immune infiltration, prognosis, and experimental validation of OSBPL family genes in liver cancer.. *BMC cancer*. PMID: 36918840
4. OSBPL11 is an African-specific locus associated with 25-hydroxyvitamin D concentrations and cardiometabolic health.. *medRxiv : the preprint server for health sciences*. PMID: 40492082
5. Analysis of the Zika and Japanese Encephalitis Virus NS5 Interactomes.. *Journal of proteome research*. PMID: 31199156

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 45.5% |
| 置信残基 (pLDDT 70-90) 占比 | 22.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 68.1% |
| 可用 PDB 条目 | 2D9X |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=74.1，有序区 68.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR001849; Pfam: PF01237, PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| OSBPL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RAB11A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RAB5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| VAPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALOX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 2D9X | pLDDT=74.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome membrane; Golgi apparatus, trans-Gol / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

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
1. OSBPL11 — Oxysterol-binding protein-related protein 11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小747 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXB4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144909-OSBPL11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXB4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
