---
type: protein-evaluation
gene: "THAP5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THAP5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THAP5 |
| 蛋白名称 | THAP domain-containing protein 5 |
| 蛋白大小 | 395 aa / 45.4 kDa |
| UniProt ID | Q7Z6K1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 395 aa / 45.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052224, IPR006612; Pfam: PF05485 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Response and acquired resistance to MET inhibitors in de novo MET fusion-positive advanced non-small cell lung cancer.. *Lung cancer (Amsterdam, Netherlands)*. PMID: 36806896
2. THAP5 is a DNA-binding transcriptional repressor that is regulated in melanoma cells during DNA damage-induced cell death.. *Biochemical and biophysical research communications*. PMID: 21110952
3. Analysis of whole-genome re-sequencing data of ducks reveals a diverse demographic history and extensive gene flow between Southeast/South Asian and Chinese populations.. *Genetics, selection, evolution : GSE*. PMID: 33849442
4. Transcriptomic integration nominates FOXN2 as a candidate schizophrenia risk gene.. *Behavioural brain research*. PMID: 41616909
5. The CCAAT binding factor can mediate interactions between CONSTANS-like proteins and DNA.. *The Plant journal : for cell and molecular biology*. PMID: 16623906

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 26.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.9% |
| 低置信 (pLDDT<50) 占比 | 50.4% |
| 有序区域 (pLDDT>70) 占比 | 36.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 36.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052224, IPR006612; Pfam: PF05485 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABRAXAS2 | 0.725 | 0.230 | — |
| THAP11 | 0.651 | 0.000 | — |
| PNPLA8 | 0.650 | 0.094 | — |
| THAP12 | 0.648 | 0.045 | — |
| DNAJB9 | 0.583 | 0.059 | — |
| THAP10 | 0.583 | 0.000 | — |
| GPR141 | 0.511 | 0.000 | — |
| THAP6 | 0.500 | 0.094 | — |
| TRERF1 | 0.478 | 0.052 | — |
| CLUL1 | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rpoH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EXOC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| S | psi-mi:"MI:0096"(pull down) | pubmed:34099652|imex:IM-29052 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| WHAMMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PICK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 6
- 调控相关比例: 1 / 14 = 7%

**评价**: STRING 14 个预测互作，IntAct 6 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 无 | pLDDT=58.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 6 interactions | 数据充分 |

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
1. THAP5 — THAP domain-containing protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小395 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6K1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177683-THAP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THAP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6K1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000177683-THAP5/subcellular

![](https://images.proteinatlas.org/51488/756_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/51488/756_H4_6_red_green.jpg)
![](https://images.proteinatlas.org/51488/760_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/51488/760_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/51488/775_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/51488/775_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z6K1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z6K1 |
| SMART | SM00692;SM00980; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052224;IPR006612; |
| Pfam | PF05485; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177683-THAP5/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
