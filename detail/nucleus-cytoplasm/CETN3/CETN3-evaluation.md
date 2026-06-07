---
type: protein-evaluation
gene: "CETN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CETN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CETN3 / CEN3 |
| 蛋白名称 | Centrin-3 |
| 蛋白大小 | 167 aa / 19.6 kDa |
| UniProt ID | O15182 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centrosome; 额外: Basal body; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, ce |
| 蛋白大小 | 8/10 | ×1 | 8 | 167 aa / 19.6 kDa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed strict=21 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.0; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050230, IPR011992, IPR018247, IPR002048; Pfam: PF13499 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **141.2/180** | |
| **归一化总分 (÷1.83)** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | ECO:0000269, ECO:0000269
| UniProt | Nucleus, nucleolus | ECO:0000303
| UniProt | Nucleus envelope | ECO:0000269
| UniProt | Nucleus, nuclear pore complex | ECO:0000269
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole | ECO:0000269, ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- centriole (GO:0005814) [IDA:UniProtKB]
- centrosome (GO:0005813) [IDA:UniProtKB]
- ciliary basal body (GO:0036064) [IDA:HPA]
- microtubule organizing center (GO:0005815) [IBA:GO_Central]
- nuclear pore nuclear basket (GO:0044615) [IDA:UniProtKB]
- nucleolus (GO:0005730) [IEA:UniProtKB-SubCell]
- photoreceptor connecting cilium (GO:0032391) [IEA:Ensembl]
- transcription export complex 2 (GO:0070390) [IDA:UniProtKB]

**结论**: HPA: Centrosome; 额外: Basal body; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Nucleus, nucleolus; Nucleus envelope; Nucleus, nuclear pore complex; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole

#### 3.2 蛋白大小评估

**评价**: 167 aa / 19.6 kDa，大小适合大部分生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed 搜索链接 | [CETN3 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CETN3) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 79.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 88.0% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050230, IPR011992, IPR018247, IPR002048; Pfam: PF13499 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ENY2 | 0.999 | 0.949 | — |
| MCM3AP | 0.999 | 0.979 | — |
| PCID2 | 0.992 | 0.493 | — |
| SFI1 | 0.982 | 0.804 | — |
| CETN2 | 0.967 | 0.426 | — |
| NUP153 | 0.949 | 0.405 | — |
| TPR | 0.945 | 0.409 | — |
| POC5 | 0.942 | 0.847 | — |
| MAD2L1 | 0.924 | 0.000 | — |
| RANBP2 | 0.916 | 0.104 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PDE6D | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| USP49 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SIK2 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-14970|pubmed:20708153 |
| Cetn2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| PA2G4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=89.0, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Nucleus, nucleolus; Nucleus envelope; Nucleus, nuclear pore complex; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole / Centrosome | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 77.2/100

**核心优势**:
1. CETN3 — Centrin-3，极度新颖，几乎未被系统研究（PubMed 21 篇）。
2. 蛋白大小167 aa，适合大部分生化实验。
3. AlphaFold pLDDT=89.0，结构预测质量高。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15182
- Protein Atlas: https://www.proteinatlas.org/search/CETN3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CETN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15182
- STRING: https://string-db.org/network/9606.CETN3
- Packet data timestamp: 2026-06-03 04:53:27

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000153140-CETN3/subcellular

![](https://images.proteinatlas.org/63704/1152_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63704/1152_B2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/63704/1156_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63704/1156_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/63704/1178_A11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/63704/1178_A11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15182-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15182 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 25..60; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 61..96; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 98..133; /note="EF-hand 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 134..167; /note="EF-hand 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR050230;IPR011992;IPR018247;IPR002048; |
| Pfam | PF13499; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153140-CETN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| POC5 | Intact, Biogrid, Opencell, Bioplex | true |
| XPC | Biogrid, Bioplex | true |
| AGR2 | Intact | false |
| ANKS6 | Opencell | false |
| BCKDK | Biogrid | false |
| CALM1 | Opencell | false |
| CALM2 | Opencell | false |
| CALM3 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
