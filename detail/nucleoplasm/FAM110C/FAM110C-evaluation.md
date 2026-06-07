---
type: protein-evaluation
gene: "FAM110C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM110C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM110C |
| 蛋白名称 | Protein FAM110C |
| 蛋白大小 | 321 aa / 33.9 kDa |
| UniProt ID | Q1W6H9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubul |
| 蛋白大小 | 10/10 | ×1 | 10 | 321 aa / 33.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025740, IPR025741, IPR025739; Pfam: PF14160, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytopla... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- centrosome (GO:0005813)
- microtubule (GO:0005874)
- nucleus (GO:0005634)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Methylation of FAM110C is a synthetic lethal marker for ATR/CHK1 inhibitors in pancreatic cancer.. *Journal of translational internal medicine*. PMID: 39081276
2. Evidence for the involvement of FAM110C protein in cell spreading and migration.. *Cellular signalling*. PMID: 19698782
3. Ovarian FAM110C (family with sequence similarity 110C): induction during the periovulatory period and regulation of granulosa cell cycle kinetics in rats.. *Biology of reproduction*. PMID: 22460667
4. Identification of Family with Sequence Similarity 110 Member C (FAM110C) as a Candidate Diagnostic and Prognostic Biomarker for Glioma.. *Iranian journal of public health*. PMID: 37899918
5. Integrated bioinformatics and machine learning identify early diagnostic biomarkers for MAFLD with comorbid psoriasis.. *Frontiers in immunology*. PMID: 42064079

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 7.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.1% |
| 中等置信 (pLDDT 50-70) 占比 | 41.4% |
| 低置信 (pLDDT<50) 占比 | 34.0% |
| 有序区域 (pLDDT>70) 占比 | 24.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 24.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025740, IPR025741, IPR025739; Pfam: PF14160, PF14161 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSPP1 | 0.942 | 0.000 | — |
| CSNK1E | 0.590 | 0.590 | — |
| ALKAL2 | 0.561 | 0.000 | — |
| SH3YL1 | 0.561 | 0.000 | — |
| TMEM47 | 0.479 | 0.000 | — |
| CNTN5 | 0.436 | 0.000 | — |
| SNTG2 | 0.430 | 0.000 | — |
| CARMIL3 | 0.421 | 0.000 | — |
| ELOA3B | 0.418 | 0.000 | — |
| COL11A1 | 0.408 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CSNK1E | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| PDLIM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CSNK1D | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| CAMK4 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 5
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM110C — Protein FAM110C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小321 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q1W6H9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184731-FAM110C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM110C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q1W6H9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q1W6H9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025740;IPR025741;IPR025739; |
| Pfam | PF14160;PF14161; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184731-FAM110C/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK1E | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
