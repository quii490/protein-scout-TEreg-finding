---
type: protein-evaluation
gene: "DDX19A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX19A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX19A / DDX19L |
| 蛋白名称 | ATP-dependent RNA helicase DDX19A |
| 蛋白大小 | 478 aa / 54.0 kDa |
| UniProt ID | Q9NUU7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 478 aa / 54.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=80.7; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Cytoplasm; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic stress granule (GO:0010494)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDX19L |

**关键文献**:
1. The RNA helicases DDX19A/B modulate selinexor sensitivity by regulating MCL1 mRNA nuclear export in leukemia cells.. *Leukemia*. PMID: 38987275
2. The Cardiac Syndecan-2 Interactome.. *Frontiers in cell and developmental biology*. PMID: 32984315
3. DDX19A promotes gastric cancer cell proliferation and migration by activating the PI3K/AKT pathway.. *Cancer cell international*. PMID: 39097730
4. DDX19A Senses Viral RNA and Mediates NLRP3-Dependent Inflammasome Activation.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 26538395
5. A functional LSD1 coregulator screen reveals a novel transcriptional regulatory cascade connecting R-loop homeostasis with epigenetic regulation.. *Nucleic acids research*. PMID: 33823549

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 43.7% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 10.0% |
| 有序区域 (pLDDT>70) 占比 | 79.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.7，有序区 79.1%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014014; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUP214 | 0.970 | 0.949 | — |
| MIF4GD | 0.932 | 0.929 | — |
| DDX19B-2 | 0.919 | 0.165 | — |
| CTIF | 0.906 | 0.905 | — |
| GLE1 | 0.889 | 0.780 | — |
| NUP88 | 0.848 | 0.813 | — |
| NLRP3 | 0.825 | 0.000 | — |
| DDX25 | 0.782 | 0.776 | — |
| GOSR1 | 0.764 | 0.000 | — |
| NUP62 | 0.715 | 0.628 | — |

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
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 无 | pLDDT=80.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DDX19A -- ATP-dependent RNA helicase DDX19A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小478 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUU7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168872-DDX19A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX19A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUU7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000168872-DDX19A/subcellular

![](https://images.proteinatlas.org/66668/1250_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/66668/1250_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/66668/1255_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/66668/1255_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/66668/1495_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/66668/1495_G1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NUU7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
