---
type: protein-evaluation
gene: "BHLHE22"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BHLHE22 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BHLHE22 / BHLHB5, TNRC20 |
| 蛋白名称 | Class E basic helix-loop-helix protein 22 |
| 蛋白大小 | 381 aa / 37.0 kDa |
| UniProt ID | Q8NFJ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear speckles; 额外: Centrosome, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 381 aa / 37.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050359, IPR036638; Pfam: PF00010 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.5/180** | |
| **归一化总分** | | | **69.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles; 额外: Centrosome, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB5, TNRC20 |

**关键文献**:
1. BHLHE22 drives the immunosuppressive bone tumor microenvironment and associated bone metastasis in prostate cancer.. *Journal for immunotherapy of cancer*. PMID: 36941015
2. Transcriptomic analyses of NeuroD1-mediated astrocyte-to-neuron conversion.. *Developmental neurobiology*. PMID: 35606902
3. N-terminal acetylation of transcription factor LIP induces immune therapy resistance via suppression of PD-L1 expression in non-small cell lung cancer.. *Journal for immunotherapy of cancer*. PMID: 39615895
4. Enhancer-driven gene regulatory network of forebrain human development provides insights into autism.. *bioRxiv : the preprint server for biology*. PMID: 40654911
5. BHLHE22 Expression Is Associated with a Proinflammatory Immune Microenvironment and Confers a Favorable Prognosis in Endometrial Cancer.. *International journal of molecular sciences*. PMID: 35806162

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 34.6% |
| 低置信 (pLDDT<50) 占比 | 44.4% |
| 有序区域 (pLDDT>70) 占比 | 21.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.9），有序残基占 21.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050359, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCL18 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| EBI-1566585 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IFNA16 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IFNA21 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IL2 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IL37 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 6
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.9 + PDB: 无 | pLDDT=57.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles; 额外: Centrosome, Cyt | 一致 |
| PPI | STRING + IntAct | 0 + 6 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BHLHE22 — Class E basic helix-loop-helix protein 22，非常新颖，仅有少数基础研究。
2. 蛋白大小381 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFJ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180828-BHLHE22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BHLHE22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFJ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
