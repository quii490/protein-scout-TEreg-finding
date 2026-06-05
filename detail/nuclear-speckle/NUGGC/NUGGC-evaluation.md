---
type: protein-evaluation
gene: "NUGGC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUGGC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUGGC / C8orf80 |
| 蛋白名称 | Nuclear GTPase SLIP-GC |
| 蛋白大小 | 796 aa / 91.1 kDa |
| UniProt ID | Q68CJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 796 aa / 91.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045063, IPR053082, IPR027417; Pfam: PF00350 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf80 |

**关键文献**:
1. Genomic and transcriptomic association studies identify 16 novel susceptibility loci for venous thromboembolism.. *Blood*. PMID: 31420334
2. A genome-wide association study of copy number variations with umbilical hernia in swine.. *Animal genetics*. PMID: 27028052
3. Transcriptome analysis reveals modulation of differentially expressed genes in LPS-treated mouse macrophages (RAW264.7 cells) by grouper (Epinephelus coioides) Epinecidin-1.. *Fish & shellfish immunology*. PMID: 37327978
4. Decoding the B-cell immune landscape in duck hepatitis A virus type 3 through single-cell genomics.. *Poultry science*. PMID: 41056664
5. Genomic profiling of BCOR-rearranged uterine sarcomas reveals novel gene fusion partners, frequent CDK4 amplification and CDKN2A loss.. *Gynecologic oncology*. PMID: 32156473

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.3 |
| 高置信度残基 (pLDDT>90) 占比 | 25.3% |
| 置信残基 (pLDDT 70-90) 占比 | 51.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 76.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.3，有序区 76.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045063, IPR053082, IPR027417; Pfam: PF00350 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUTM2G | 0.626 | 0.045 | — |
| RTL9 | 0.541 | 0.000 | — |
| RALGPS1 | 0.476 | 0.000 | — |
| RHEX | 0.459 | 0.000 | — |
| MAP7D2 | 0.454 | 0.045 | — |
| RFTN2 | 0.454 | 0.000 | — |
| LAX1 | 0.450 | 0.000 | — |
| AICDA | 0.441 | 0.000 | — |
| EFR3B | 0.419 | 0.000 | — |
| C16orf54 | 0.413 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| POLD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FEM1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 2
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.3 + PDB: 无 | pLDDT=78.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus speckle / Nuclear speckles; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 10 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NUGGC — Nuclear GTPase SLIP-GC，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小796 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68CJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189233-NUGGC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUGGC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68CJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000189233-NUGGC/subcellular

![](https://images.proteinatlas.org/24293/2104_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/24293/2104_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/24293/2180_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/24293/2180_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/24293/2198_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/24293/2198_C7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q68CJ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
