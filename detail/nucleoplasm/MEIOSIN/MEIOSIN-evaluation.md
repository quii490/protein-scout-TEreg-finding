---
type: protein-evaluation
gene: "MEIOSIN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEIOSIN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEIOSIN / BHMG1 |
| 蛋白名称 | Meiosis initiator protein |
| 蛋白大小 | 638 aa / 70.2 kDa |
| UniProt ID | C9JSJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 638 aa / 70.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR009071, IPR036910; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHMG1 |

**关键文献**:
1. Mechanisms of meiosis initiation and meiotic prophase progression during spermatogenesis.. *Molecular aspects of medicine*. PMID: 38797021
2. Histone demethylase KDM2A recruits HCFC1 and E2F1 to orchestrate male germ cell meiotic entry and progression.. *The EMBO journal*. PMID: 39160277
3. MEIOSIN Directs the Switch from Mitosis to Meiosis in Mammalian Germ Cells.. *Developmental cell*. PMID: 32032549
4. MEIOSIN directs initiation of meiosis and subsequent meiotic prophase program during spermatogenesis.. *Genes & genetic systems*. PMID: 34955498
5. Destabilization of mRNAs enhances competence to initiate meiosis in mouse spermatogenic cells.. *Development (Cambridge, England)*. PMID: 38884383

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.4 |
| 高置信度残基 (pLDDT>90) 占比 | 10.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 70.7% |
| 有序区域 (pLDDT>70) 占比 | 18.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.4），有序残基占 18.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR009071, IPR036910; Pfam: PF00010, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STRA8 | 0.786 | 0.000 | — |
| ZGLP1 | 0.598 | 0.053 | — |
| DMWD | 0.495 | 0.000 | — |
| SIX5 | 0.482 | 0.091 | — |
| QPCTL | 0.472 | 0.000 | — |
| SYCP3 | 0.465 | 0.094 | — |
| SYMPK | 0.453 | 0.000 | — |
| DAZL | 0.453 | 0.000 | — |
| TICAM1 | 0.433 | 0.000 | — |
| ZNF469 | 0.408 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 11，IntAct interactions: 0
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.4 + PDB: 无 | pLDDT=51.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 0 interactions | 数据有限 |

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
1. MEIOSIN — Meiosis initiator protein，非常新颖，仅有少数基础研究。
2. 蛋白大小638 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=51.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C9JSJ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000237452-MEIOSIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEIOSIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C9JSJ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000237452-MEIOSIN/subcellular

![](https://images.proteinatlas.org/49521/1892_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/49521/1892_F2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-C9JSJ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | C9JSJ3 |
| SMART | SM00398; |
| UniProt Domain [FT] | DOMAIN 62..116; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638;IPR009071;IPR036910; |
| Pfam | PF00010;PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000237452-MEIOSIN/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
