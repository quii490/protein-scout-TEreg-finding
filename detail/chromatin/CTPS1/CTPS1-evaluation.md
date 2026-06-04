---
type: protein-evaluation
gene: "CTPS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTPS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTPS1 / CTPS |
| 蛋白名称 | CTP synthase 1 |
| 蛋白大小 | 591 aa / 66.7 kDa |
| UniProt ID | P17812 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Actin filaments; UniProt: Cytoplasm, cytosol; Nucleus; Chromosome |
| 蛋白大小 | 10/10 | x1 | 10 | 591 aa / 66.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=49 篇 (≤60→6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=91.4; PDB: 2VO1, 5U03, 7MGZ, 7MH0, 7MIF, 7MIG |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR029062, IPR004468, IPR017456, IPR017926, IPR033 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Actin filaments | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoophidium (GO:0097268)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 98 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTPS |

**关键文献**:
1. Pyrimidine synthesis enzyme CTP synthetase 1 suppresses antiviral interferon induction by deamidating IRF3.. *Immunity*. PMID: 39719712
2. Combined inhibition of CTPS1 and ATR is a metabolic vulnerability in p53-deficient myeloma cells.. *HemaSphere*. PMID: 39380841
3. CTPS1 promotes malignant progression of triple-negative breast cancer with transcriptional activation by YBX1.. *Journal of translational medicine*. PMID: 34991621
4. CTPS1 modulates mitophagy to propel diffuse large B-cell lymphoma via reshaping CEPT1-mediated phospholipid metabolism.. *Redox biology*. PMID: 41865720
5. A Novel Synthetic Lethal Approach to Target MYC-Driven Cancers.. *Cancer research*. PMID: 35288735

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 82.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 94.4% |
| 可用 PDB 条目 | 2VO1, 5U03, 7MGZ, 7MH0, 7MIF, 7MIG |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=91.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029062, IPR004468, IPR017456, IPR017926, IPR033828; Pfam: PF06418, PF00117 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTPS2 | 0.983 | 0.836 | — |
| GMPS | 0.960 | 0.420 | — |
| NME1 | 0.951 | 0.000 | — |
| NME2 | 0.951 | 0.000 | — |
| NME6 | 0.947 | 0.000 | — |
| NME7 | 0.940 | 0.000 | — |
| NME4 | 0.940 | 0.000 | — |
| NME3 | 0.939 | 0.000 | — |
| NME1-NME2 | 0.938 | 0.000 | — |
| AK9 | 0.938 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 2VO1, 5U03, 7MGZ, 7MH0, 7MIF,  | pLDDT=91.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Chromosome / Cytosol; 额外: Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CTPS1 -- CTP synthase 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小591 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17812
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171793-CTPS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTPS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17812
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
