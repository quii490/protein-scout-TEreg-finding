---
type: protein-evaluation
gene: "PTF1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTF1A — REJECTED (研究热度过高 (PubMed strict=232，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTF1A / BHLHA29, PTF1P48 |
| 蛋白名称 | Pancreas transcription factor 1 subunit alpha |
| 蛋白大小 | 328 aa / 35.0 kDa |
| UniProt ID | Q7RTS3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 328 aa / 35.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=232 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 232 |
| PubMed broad count | 432 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA29, PTF1P48 |

**关键文献**:
1. Combined MEK and STAT3 Inhibition Uncovers Stromal Plasticity by Enriching for Cancer-Associated Fibroblasts With Mesenchymal Stem Cell-Like Features to Overcome Immunotherapy Resistance in Pancreatic Cancer.. *Gastroenterology*. PMID: 35948109
2. Transcription factor Ptf1a in development, diseases and reprogramming.. *Cellular and molecular life sciences : CMLS*. PMID: 30470852
3. Pancreatic cancer cell-intrinsic transglutaminase-2 promotes T cell suppression through microtubule-dependent secretion of immunosuppressive cytokines.. *Journal for immunotherapy of cancer*. PMID: 39824529
4. Mechanisms regulating GABAergic neuron development.. *Cellular and molecular life sciences : CMLS*. PMID: 24196748
5. Multiscale 3D genome rewiring during PTF1A-mediated somatic cell reprogramming into neural stem cells.. *Communications biology*. PMID: 39537822

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 32.0% |
| 低置信 (pLDDT<50) 占比 | 39.9% |
| 有序区域 (pLDDT>70) 占比 | 28.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 28.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBPJL | 0.994 | 0.331 | — |
| RBPJ | 0.987 | 0.285 | — |
| HNF1B | 0.891 | 0.000 | — |
| PDX1 | 0.855 | 0.053 | — |
| FGF10 | 0.831 | 0.000 | — |
| HNF1A | 0.801 | 0.000 | — |
| NKX6-1 | 0.795 | 0.000 | — |
| INS | 0.756 | 0.000 | — |
| NKX6-2 | 0.755 | 0.000 | — |
| FOXN4 | 0.754 | 0.053 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 无 | pLDDT=60.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PTF1A — Pancreas transcription factor 1 subunit alpha，研究基础较多，新颖性有限。
2. 蛋白大小328 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 232 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 232 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7RTS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168267-PTF1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTF1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTS3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
