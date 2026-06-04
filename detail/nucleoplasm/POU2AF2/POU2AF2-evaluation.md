---
type: protein-evaluation
gene: "POU2AF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POU2AF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POU2AF2 / C11orf53 |
| 蛋白名称 | POU domain class 2-associating factor 2 |
| 蛋白大小 | 288 aa / 31.1 kDa |
| UniProt ID | Q8IXP5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 288 aa / 31.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047571, IPR037655; Pfam: PF17721 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf53 |

**关键文献**:
1. A SWI/SNF-dependent transcriptional regulation mediated by POU2AF2/C11orf53 at enhancer.. *Nature communications*. PMID: 38453939
2. A conserved 3'UTR short motif regulates gene expression in vertebrates.. *Nucleic acids research*. PMID: 41505098
3. Genetic mapping reveals Pou2af2/OCA-T1-dependent tuning of tuft cell differentiation and intestinal type 2 immunity.. *Science immunology*. PMID: 37172102
4. Genetic variation at 11q23.1 confers colorectal cancer risk by dysregulation of colonic tuft cell transcriptional activator POU2AF2.. *Gut*. PMID: 39609081
5. POU2AF2/C11orf53 functions as a coactivator of POU2F3 by maintaining chromatin accessibility and enhancer activity.. *Science advances*. PMID: 36197978

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.3 |
| 高置信度残基 (pLDDT>90) 占比 | 1.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.2% |
| 中等置信 (pLDDT 50-70) 占比 | 37.2% |
| 低置信 (pLDDT<50) 占比 | 56.6% |
| 有序区域 (pLDDT>70) 占比 | 6.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=51.3），有序残基占 6.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047571, IPR037655; Pfam: PF17721 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf6 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| CLIC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FBXO10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 3
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.3 + PDB: 无 | pLDDT=51.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 3 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. POU2AF2 — POU domain class 2-associating factor 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小288 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXP5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150750-POU2AF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POU2AF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXP5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
