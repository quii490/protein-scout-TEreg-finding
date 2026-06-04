---
type: protein-evaluation
gene: "Gvin1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Gvin1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Gvin1 / GVIN1, VLIG1 |
| 蛋白名称 | Interferon-induced very large GTPase 1 |
| 蛋白大小 | 2422 aa / 279.0 kDa |
| UniProt ID | Q7Z2Y8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2422 aa / 279.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029028, IPR030383, IPR058641, IPR027417, IPR057 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GVIN1, VLIG1 |

**关键文献**:
1. Human giant GTPase GVIN1 forms an antimicrobial coatomer around the intracellular bacterial pathogen Burkholderia thailandensis.. *bioRxiv : the preprint server for biology*. PMID: 40196472
2. Physiological and transcriptomic analysis provides new insights into osmoregulation mechanism of Ruditapes philippinarum under low and high salinity stress.. *The Science of the total environment*. PMID: 38750748
3. Inefficient type I interferon-mediated antiviral protection of primary mouse neurons is associated with the lack of apolipoprotein l9 expression.. *Journal of virology*. PMID: 24453359
4. Transcriptomic and functional evidence reveals dual-module immune response of human-nasal staphylococcus aureus in Koi Carp (Cyprinus carpio).. *International journal of medical microbiology : IJMM*. PMID: 41687281
5. Single-variant genome-wide association study and regional heritability mapping of protein efficiency and performance traits in Large White pigs.. *Genetics, selection, evolution : GSE*. PMID: 40813973

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 5.1% |
| 置信残基 (pLDDT 70-90) 占比 | 60.3% |
| 中等置信 (pLDDT 50-70) 占比 | 24.8% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 65.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=71.9，有序区 65.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029028, IPR030383, IPR058641, IPR027417, IPR057365; Pfam: PF25496, PF25974, PF25683 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| Lat | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-25620|pubmed:24584089 |
| GVINP1 | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 5
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 无 | pLDDT=71.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 5 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. Gvin1 — Interferon-induced very large GTPase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2422 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z2Y8
- Protein Atlas: https://www.proteinatlas.org/search/Gvin1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Gvin1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z2Y8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
