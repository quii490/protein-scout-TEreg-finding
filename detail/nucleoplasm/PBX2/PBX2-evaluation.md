---
type: protein-evaluation
gene: "PBX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PBX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PBX2 / G17 |
| 蛋白名称 | Pre-B-cell leukemia transcription factor 2 |
| 蛋白大小 | 430 aa / 45.9 kDa |
| UniProt ID | P40425 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 430 aa / 45.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=91 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR008422, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 91 |
| PubMed broad count | 186 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: G17 |

**关键文献**:
1. Integrative multi-omics analysis of Crohn's disease and metabolic syndrome: Unveiling the underlying molecular mechanisms of comorbidity.. *Computers in biology and medicine*. PMID: 39541897
2. PRMT1-Mediated SWI/SNF Complex Recruitment via SMARCC1 Drives IGF2BP2 Transcription to Enhance Carboplatin Resistance in Head and Neck Squamous Cell Carcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40270464
3. The TALE homeodomain protein Pbx2 is not essential for development and long-term survival.. *Molecular and cellular biology*. PMID: 15169896
4. Coexpression of HOXA6 and PBX2 promotes metastasis in gastric cancer.. *Aging*. PMID: 33535170
5. HOXA10, Pbx2, and Meis1 protein expression in the human endometrium: formation of multimeric complexes on HOXA10 target genes.. *The Journal of clinical endocrinology and metabolism*. PMID: 15494461

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.0 |
| 高置信度残基 (pLDDT>90) 占比 | 28.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 33.7% |
| 有序区域 (pLDDT>70) 占比 | 54.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.0），有序残基占 54.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR008422, IPR005542; Pfam: PF05920, PF03792 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PKNOX1 | 0.972 | 0.864 | — |
| MEIS2 | 0.964 | 0.909 | — |
| HOXA10 | 0.848 | 0.291 | — |
| HOXA9 | 0.829 | 0.476 | — |
| HOXB7 | 0.814 | 0.290 | — |
| MAB21L1 | 0.811 | 0.806 | — |
| AGPAT1 | 0.809 | 0.000 | — |
| HOXC9 | 0.791 | 0.643 | — |
| PKNOX2 | 0.775 | 0.696 | — |
| SLC38A2 | 0.760 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ELP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| BLOC1S1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| SMYD3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| ZDHHC7 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| MCRS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| MTREX | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| NUP62 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| COPS6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| BAIAP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| RPS6KC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.0 + PDB: 无 | pLDDT=69.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PBX2 — Pre-B-cell leukemia transcription factor 2，研究基础较多，新颖性有限。
2. 蛋白大小430 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 91 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P40425
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204304-PBX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PBX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P40425
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
