---
type: protein-evaluation
gene: "DGCR14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DGCR14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGCR14 / DGCR13, DGCR14, DGSH, DGSI, ES2 |
| 蛋白名称 | Splicing factor ESS-2 homolog |
| 蛋白大小 | 476 aa / 52.6 kDa |
| UniProt ID | Q96DF8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 476 aa / 52.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=67.3; PDB: 8C6J, 8RO2, 9FMD |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR019148; Pfam: PF09751 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DGCR13, DGCR14, DGSH, DGSI, ES2 |

**关键文献**:
1. The Role of ESS2/DGCR14: Is It an Essential Factor in Splicing and Transcription?. *International journal of molecular sciences*. PMID: 40362295
2. DGCR14 induces Il17a gene expression through the RORγ/BAZ1B/RSKS2 complex.. *Molecular and cellular biology*. PMID: 25368387
3. AtDGCR14L contributes to salt-stress tolerance via regulating pre-mRNA splicing in Arabidopsis.. *The Plant journal : for cell and molecular biology*. PMID: 39522174
4. Biallelic FRA10AC1 variants cause a neurodevelopmental disorder with growth retardation.. *Brain : a journal of neurology*. PMID: 34694367
5. A Collection of Pre-mRNA Splicing Mutants in Arabidopsis thaliana.. *G3 (Bethesda, Md.)*. PMID: 32265287

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.3 |
| 高置信度残基 (pLDDT>90) 占比 | 12.2% |
| 置信残基 (pLDDT 70-90) 占比 | 32.4% |
| 中等置信 (pLDDT 50-70) 占比 | 32.8% |
| 低置信 (pLDDT<50) 占比 | 22.7% |
| 有序区域 (pLDDT>70) 占比 | 44.6% |
| 可用 PDB 条目 | 8C6J, 8RO2, 9FMD |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.3），有序残基占 44.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019148; Pfam: PF09751 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DGCR2 | 0.943 | 0.000 | — |
| GATD3A | 0.925 | 0.000 | — |
| SOX2 | 0.838 | 0.000 | — |
| FRA10AC1 | 0.831 | 0.786 | — |
| ESR1 | 0.815 | 0.047 | — |
| SLC25A1 | 0.813 | 0.000 | — |
| HIRA | 0.735 | 0.000 | — |
| SUZ12 | 0.725 | 0.000 | — |
| UFD1 | 0.717 | 0.000 | — |
| TTC14 | 0.713 | 0.607 | — |

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
| 三维结构 | AlphaFold pLDDT=67.3 + PDB: 8C6J, 8RO2, 9FMD | pLDDT=67.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DGCR14 -- Splicing factor ESS-2 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小476 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DF8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100056-ESS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGCR14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DF8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
