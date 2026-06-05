---
type: protein-evaluation
gene: "PCID2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCID2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCID2 |
| 蛋白名称 | PCI domain-containing protein 2 |
| 蛋白大小 | 399 aa / 46.0 kDa |
| UniProt ID | Q5JVF3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Cytoplasm; Nucleus, nuclear pore complex |
| 蛋白大小 | 10/10 | ×1 | 10 | 399 aa / 46.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.5; PDB: 3T5X, 9DLP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045114, IPR000717, IPR036388; Pfam: PF01399 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Cytoplasm; Nucleus, nuclear pore complex | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear pore nuclear basket (GO:0044615)
- nucleus (GO:0005634)
- transcription export complex 2 (GO:0070390)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PCID2 dysregulates transcription and viral RNA processing to promote HIV-1 latency.. *iScience*. PMID: 38384833
2. PCID2 is essential for spermatogonial differentiation by regulating alternative splicing.. *Cellular and molecular life sciences : CMLS*. PMID: 41526677
3. Structural mechanism of DDX39B regulation by human TREX-2 and a related complex in mRNP remodeling.. *Nature communications*. PMID: 40595470
4. Gene expression dynamics before and after zygotic gene activation in Drosophila early embryogenesis.. *iScience*. PMID: 40894916
5. Increased chemosensitivity via BRCA2-independent DNA damage in DSS1- and PCID2-depleted breast carcinomas.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 34031538

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.5 |
| 高置信度残基 (pLDDT>90) 占比 | 93.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.3% |
| 可用 PDB 条目 | 3T5X, 9DLP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3T5X, 9DLP）+ AlphaFold高质量预测（pLDDT=95.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045114, IPR000717, IPR036388; Pfam: PF01399 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCM3AP | 0.999 | 0.870 | — |
| CETN2 | 0.999 | 0.493 | — |
| ENY2 | 0.999 | 0.795 | — |
| SEM1 | 0.994 | 0.835 | — |
| CETN3 | 0.992 | 0.493 | — |
| MAD1L1 | 0.968 | 0.000 | — |
| MAD2L1 | 0.966 | 0.000 | — |
| LENG8 | 0.966 | 0.945 | — |
| NUP153 | 0.939 | 0.000 | — |
| NUP98 | 0.928 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SEM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| "Fs | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NEK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMAD2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| NS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| NS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.5 + PDB: 3T5X, 9DLP | pLDDT=95.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nuclear pore complex / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PCID2 — PCI domain-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小399 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JVF3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126226-PCID2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCID2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JVF3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000126226-PCID2/subcellular

![](https://images.proteinatlas.org/73074/1398_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73074/1398_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73074/1403_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73074/1403_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73074/1411_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73074/1411_H8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JVF3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
