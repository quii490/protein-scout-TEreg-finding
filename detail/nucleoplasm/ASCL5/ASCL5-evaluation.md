---
type: protein-evaluation
gene: "ASCL5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASCL5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASCL5 / BHLHA47 |
| 蛋白名称 | Achaete-scute homolog 5 |
| 蛋白大小 | 206 aa / 22.5 kDa |
| UniProt ID | Q7RTU5 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:24:05 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 206 aa / 22.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=7 篇 (<=20->10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=63.2 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR011598, IPR050283... |
| PPI 网络 | 3/10 | x3 | 9 | STRING 7 partners; IntAct 2 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **115.0/180** | |
| **归一化总分 (/1.83)** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- chromatin (GO:0000785)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 206 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA47 |

**关键文献**:
1. Identification of the Novel Tooth-Specific Transcription Factor AmeloD.. *Journal of dental research*. PMID: 30426815
2. A detrimental mutation on USP40 unlocks the tumorigenesis in a rare case of lung cancer.. *International journal of clinical and experimental pathology*. PMID: 31933881
3. Transcriptional programs of Pitx2 and Tfap2a/Tfap2b controlling lineage specification of mandibular epithelium during tooth initiation.. *PLoS genetics*. PMID: 39052671
4. Systematic analysis of the achaete-scute complex-like gene signature in clinical cancer patients.. *Molecular and clinical oncology*. PMID: 28123722
5. Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML.. *Annals of hematology*. PMID: 41037101

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 16.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 56.8% |
| 低置信 (pLDDT<50) 占比 | 18.7% |
| 有序区域 (pLDDT>70) 占比 | 24.5% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=63.2），存在部分低置信区域。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF316 | 0.400 | 0.070 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-2 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| H1-5 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 2

**评价**: 互作数据有限：STRING 7 预测 + IntAct 2 实验互作。PPI 评分 3/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=63.2 | 单一来源 |
| 定位 | UniProt | Nucleus | 单一来源 |
| PPI | STRING + IntAct | 7 + 2 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 62.8/100

**核心优势**:
1. ASCL5 -- Achaete-scute homolog 5，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小206 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q7RTU5
- Protein Atlas: https://www.proteinatlas.org/search/ASCL5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASCL5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTU5
- STRING: https://string-db.org/network/9606.ASCL5
- Packet data timestamp: 2026-06-03 03:24:05

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7RTU5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7RTU5 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 83..135; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050283;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000232237-ASCL5/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
