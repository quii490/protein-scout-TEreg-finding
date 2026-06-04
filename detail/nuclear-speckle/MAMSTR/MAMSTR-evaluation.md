---
type: protein-evaluation
gene: "MAMSTR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAMSTR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAMSTR / MASTR |
| 蛋白名称 | MEF2-activating motif and SAP domain-containing transcriptional regulator |
| 蛋白大小 | 415 aa / 44.6 kDa |
| UniProt ID | Q6ZN01 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 415 aa / 44.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003034, IPR036361, IPR052305; Pfam: PF02037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MASTR |

**关键文献**:
1. Causal associations and shared genetics between hypertension and COVID-19.. *Journal of medical virology*. PMID: 36951353
2. Genome-wide association study identifies FUT2 rs601338 polymorphism linking intra-pancreatic fat deposition to chronic pancreatitis.. *Pancreatology : official journal of the International Association of Pancreatology (IAP) ... [et al.]*. PMID: 40744837
3. Genome-Wide Association Study Identifies New Risk Loci for Progression of Schistosomiasis Among the Chinese Population.. *Frontiers in cellular and infection microbiology*. PMID: 35493725
4. Genome-Wide Analysis of MAMSTR Transcription Factor-Binding Sites via ChIP-Seq in Porcine Skeletal Muscle Fibroblasts.. *Animals : an open access journal from MDPI*. PMID: 37889674
5. Single-step genome-wide association study for carcass quality traits in Angus beef cattle.. *Tropical animal health and production*. PMID: 40751099

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.3 |
| 高置信度残基 (pLDDT>90) 占比 | 9.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 29.6% |
| 低置信 (pLDDT<50) 占比 | 48.2% |
| 有序区域 (pLDDT>70) 占比 | 22.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.3），有序残基占 22.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003034, IPR036361, IPR052305; Pfam: PF02037 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEF2C | 0.682 | 0.000 | — |
| SRF | 0.588 | 0.000 | — |
| MYF5 | 0.553 | 0.000 | — |
| PPP1R3F | 0.489 | 0.000 | — |
| MRTFB | 0.471 | 0.053 | — |
| LRGUK | 0.460 | 0.445 | — |
| SHROOM1 | 0.450 | 0.000 | — |
| CPED1 | 0.441 | 0.000 | — |
| CCDC120 | 0.438 | 0.000 | — |
| MYOCD | 0.424 | 0.053 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000324175.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 1
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.3 + PDB: 无 | pLDDT=57.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 13 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAMSTR — MEF2-activating motif and SAP domain-containing transcriptional regulator，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小415 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZN01
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176909-MAMSTR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAMSTR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZN01
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
