---
type: protein-evaluation
gene: "CENPW"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CENPW 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPW / C6orf173 / CUG2 |
| 蛋白名称 | Centromere protein W |
| 蛋白大小 | 88 aa / 10.1 kDa |
| UniProt ID | Q5EE01 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | ×4 | 40 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore; Nuc |
| 蛋白大小 | 6/10 | ×1 | 6 | 88 aa / 10.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=50 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.7; PDB: 暂无 |
| 调控结构域 | 10/10 | ×2 | 20 | InterPro: IPR028847, IPR052484, IPR009072; Pfam: PF15510 |
| PPI 网络 | 9/10 | ×3 | 27 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **161.5/180** | |
| **归一化总分 (÷1.83)** | | | **88.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | ECO:0000269
| UniProt | Chromosome, centromere | ECO:0000269, ECO:0000269, ECO:0000269
| UniProt | Chromosome, centromere, kinetochore | ECO:0000269, ECO:0000269
| UniProt | Nucleus matrix | ECO:0000269
| UniProt | Nucleus, nucleolus | ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- chromosome, centromeric region (GO:0000775) [IDA:UniProtKB]
- inner kinetochore (GO:0000939) [IPI:ComplexPortal]
- kinetochore (GO:0000776) [IDA:UniProtKB]
- nuclear matrix (GO:0016363) [IEA:UniProtKB-SubCell]
- nucleolus (GO:0005730) [IEA:UniProtKB-SubCell]
- nucleoplasm (GO:0005654) [IDA:HPA]
- nucleus (GO:0005634) [NAS:ComplexPortal]

**结论**: HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore; Nucleus matrix; Nucleus, nucleolus

#### 3.2 蛋白大小评估

**评价**: 88 aa / 10.1 kDa，蛋白大小稍偏，但可进行常规生化分析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed 搜索链接 | [CENPW PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CENPW) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 83.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 86.4% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028847, IPR052484, IPR009072; Pfam: PF15510 |

**染色质调控潜力分析**: 存在染色质/调控相关结构域/功能特征: nucleosome, histone, centromere, kinetochore

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPT | 0.999 | 0.987 | — |
| CENPN | 0.999 | 0.900 | — |
| CENPS | 0.999 | 0.955 | — |
| CENPX | 0.999 | 0.927 | — |
| CENPC | 0.997 | 0.800 | — |
| CENPH | 0.997 | 0.800 | — |
| CENPU | 0.997 | 0.800 | — |
| CENPI | 0.996 | 0.900 | — |
| CENPK | 0.996 | 0.800 | — |
| CENPM | 0.995 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CENPT | psi-mi:"MI:0071"(molecular sieving) | pubmed:22304917|imex:IM-17361 |
| CENPS | psi-mi:"MI:0071"(molecular sieving) | pubmed:22304917|imex:IM-17361 |
| centoromere protein C | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-12152|pubmed:19070575 |
| Cenph | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PMVK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0/15。

**评价**: PPI 网络数据较好。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=89.7, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore; Nucleus matrix; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 88.3/100

**核心优势**:
1. CENPW — Centromere protein W，较新颖，PubMed 50 篇。
2. AlphaFold pLDDT=89.7，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计 ChIP-seq/CUT&RUN 验证染色质结合
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5EE01
- Protein Atlas: https://www.proteinatlas.org/search/CENPW
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPW
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5EE01
- STRING: https://string-db.org/network/9606.CENPW
- Packet data timestamp: 2026-06-03 04:47:54

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000203760-CENPW/subcellular

![](https://images.proteinatlas.org/67285/1237_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/67285/1237_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/67285/1284_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/67285/1284_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5EE01-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5EE01 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028847;IPR052484;IPR009072; |
| Pfam | PF15510; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203760-CENPW/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CENPT | Intact, Biogrid | true |
| BTRC | Biogrid | false |
| COPS5 | Biogrid | false |
| CUL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
