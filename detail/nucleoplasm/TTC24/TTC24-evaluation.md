---
type: protein-evaluation
gene: "TTC24"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC24 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC24 |
| 蛋白名称 | Tetratricopeptide repeat protein 24 |
| 蛋白大小 | 582 aa / 63.4 kDa |
| UniProt ID | A2A3L6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 582 aa / 63.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011990, IPR024812, IPR019734; Pfam: PF13424, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genome-wide CRISPR-Cas9 screening identifies the CYTH2 host gene as a potential therapeutic target of influenza viral infection.. *Cell reports*. PMID: 35354039
2. A genome-derived (gaa.ttc)24 trinucleotide block binds nuclear protein(s) specifically and forms triple helices.. *Gene*. PMID: 9714838

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 56.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 64.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 64.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR024812, IPR019734; Pfam: PF13424, PF13176 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GON4L | 0.575 | 0.045 | — |
| LEO1 | 0.475 | 0.398 | — |
| MT-ND4 | 0.472 | 0.398 | — |
| NANS | 0.446 | 0.000 | — |
| IQGAP3 | 0.439 | 0.000 | — |
| HAS2 | 0.420 | 0.255 | — |
| HAS3 | 0.420 | 0.255 | — |
| HAS1 | 0.420 | 0.255 | — |
| CLUAP1 | 0.417 | 0.221 | — |
| ITPRIPL2 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rdgC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ARHGAP21 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| SCRIB | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| HTRA3 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| LIN7A | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| RHPN1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ARHGEF11 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| DLG5 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| LIN7C | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PTPN13 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TTC24 — Tetratricopeptide repeat protein 24，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小582 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

TTC24（Tetratricopeptide repeat protein 24）属于含三十四肽重复序列（TPR）蛋白超家族。结构域分析显示该蛋白包含典型TPR结构域：InterPro注释为IPR011990（TPR-like helical domain）、IPR024812（TPR repeat domain）和IPR019734（TPR repeat），Pfam匹配PF13424（TPR_12）和PF13176（TPR_7），SMART确认SM00028（TPR motif）。TPR结构域由34个氨基酸的串联重复单元组成，形成螺旋-转角-螺旋的超螺旋结构，主要功能是介导蛋白-蛋白相互作用和作为多蛋白复合体的组装支架。AlphaFold v6预测整体pLDDT=73.8，高置信度残基（pLDDT>90）占56.2%，有序区域（pLDDT>70）占64.6%，表明TPR重复区域的折叠预测可信度较高。

PPI网络揭示了TTC24与转录延伸和mRNA加工机制的潜在关联。STRING记录的互作伙伴中，LEO1（combined score=0.475, experimental=0.398）尤为值得关注：LEO1是PAF1复合体（PAF1C）的核心亚基，PAF1C在转录延伸、组蛋白修饰（H2B泛素化、H3K4和H3K36甲基化）和RNA聚合酶II调控中发挥关键作用。GON4L（score=0.575）是转录调控因子，与造血和白血病发生相关。IntAct实验数据记录了15个互作伙伴，主要来自高通量holdup assay筛选（doi:10.1038/s41467-022-33018-0），包括ARHGAP21、SCRIB、LIN7A、LIN7C、DLG5等细胞极性蛋白，以及HTRA3蛋白酶和PTPN13磷酸酶。这些互作提示TTC24可能通过TPR支架功能桥接转录调控与细胞信号网络。

BioGRID额外记录了TTC24与NUP98（核孔蛋白98）的互作，这一发现具有重要的机制意义。NUP98是核孔复合体的组分，其N端含FG重复序列，已知在白血病中通过染色体易位形成NUP98融合蛋白，这些融合蛋白异常招募转录共激活因子和染色质修饰复合体。TTC24-NUP98互作提示TTC24可能参与核质运输或与核孔关联的转录调控。

值得注意的是，TTC24的极早期研究（PMID:9714838，发表于1998年）报道了一个(gaa.ttc)24三核苷酸重复序列能特异性结合核蛋白并形成三链DNA结构。虽然该研究与TTC24蛋白的直接关联尚需验证，但TPR蛋白结合特定DNA结构的功能已有先例（如TPR-containing TFIIIC亚基结合tRNA基因内部启动子）。TTC24的PubMed严格计数仅2篇（broad=4篇），是极为新颖的研究对象。其核质定位（HPA Nucleoplasm, Approved）、TPR介导的多蛋白互作能力，以及潜在的转录调控关联，使其成为TE调控研究中值得优先探索的候选靶点。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NUP98 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A2A3L6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187862-TTC24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A2A3L6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000187862-TTC24/subcellular

![](https://images.proteinatlas.org/29799/1778_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/29799/1778_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A2A3L6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A2A3L6 |
| SMART | SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011990;IPR024812;IPR019734; |
| Pfam | PF13424;PF13176; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187862-TTC24/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
