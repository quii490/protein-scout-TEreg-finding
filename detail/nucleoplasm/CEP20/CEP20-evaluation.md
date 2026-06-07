---
type: protein-evaluation
gene: "CEP20"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CEP20 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP20 / C16orf63 / FOPNL / FOR20 / PHSECRG2 |
| 蛋白名称 | Centrosomal protein 20 |
| 蛋白大小 | 174 aa / 19.8 kDa |
| UniProt ID | Q96NB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centriolar satellite, Centrosome, Basal body; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 174 aa / 19.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.7; PDB: 暂无 |
| 调控结构域 | 6/10 | ×2 | 12 | InterPro: IPR018993, IPR006594; Pfam: PF09398 |
| PPI 网络 | 5/10 | ×3 | 15 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **123.0/180** | |
| **归一化总分 (÷1.83)** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite, Centrosome, Basal body | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole | ECO:0000269
| UniProt | Cell projection, cilium | ECO:0000250
| UniProt | Cytoplasm, cytoskeleton, cilium basal body | ECO:0000250
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | ECO:0000269, ECO:0000269
| UniProt | Cytoplasmic granule | ECO:0000269
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar satellite | ECO:0000269, ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- centriolar satellite (GO:0034451) [IDA:HPA]
- centriole (GO:0005814) [IEA:UniProtKB-SubCell]
- centrosome (GO:0005813) [IDA:HPA]
- ciliary basal body (GO:0036064) [IDA:HPA]
- motile cilium (GO:0031514) [ISS:UniProtKB]
- nucleoplasm (GO:0005654) [IDA:HPA]

**结论**: HPA: Centriolar satellite, Centrosome, Basal body; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Cell projection, cilium; Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasmic granule; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar satellite

#### 3.2 蛋白大小评估

**评价**: 174 aa / 19.8 kDa，大小适合大部分生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed 搜索链接 | [CEP20 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CEP20) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.7 |
| 高置信度残基 (pLDDT>90) 占比 | 42.0% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 12.6% |
| 低置信 (pLDDT<50) 占比 | 26.4% |
| 有序区域 (pLDDT>70) 占比 | 61.0% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018993, IPR006594; Pfam: PF09398 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| — | — | 暂无数据 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORF46 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CCDC116 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Cep43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| OFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DYNLL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CEP135 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep131 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep120 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CSNK1E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Dlg5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/1。

**评价**: PPI 数据有限，互作网络信息不足。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=73.7, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Cell projection, cilium; Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasmic granule; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar satellite / Centriolar satellite, Centrosome, Basal body | 部分一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- 单源PPI数据: +0.25
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**归一化总分**: 67.2/100

**核心优势**:
1. CEP20 — Centrosomal protein 20，极度新颖，几乎未被系统研究（PubMed 1 篇）。
2. 蛋白大小174 aa，适合大部分生化实验。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。
2. PubMed 1 篇，研究基础极有限，功能注释不完整
3. PPI 数据缺失，互作网络未知

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] Co-IP/MS 实验鉴定互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96NB1
- Protein Atlas: https://www.proteinatlas.org/search/CEP20
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NB1
- STRING: https://string-db.org/network/9606.CEP20
- Packet data timestamp: 2026-06-03 04:48:40

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centriolar satellite (supported)。来源: https://www.proteinatlas.org/ENSG00000133393-CEP20/subcellular

![](https://images.proteinatlas.org/40599/2121_A12_102_blue_red_green.jpg)
![](https://images.proteinatlas.org/40599/2121_A12_91_blue_red_green.jpg)
![](https://images.proteinatlas.org/40599/2127_B2_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/40599/2127_B2_50_blue_red_green.jpg)
![](https://images.proteinatlas.org/40599/2175_C9_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/40599/2175_C9_65_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96NB1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96NB1 |
| SMART | SM00667; |
| UniProt Domain [FT] | DOMAIN 49..81; /note="LisH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00126" |
| InterPro | IPR018993;IPR006594; |
| Pfam | PF09398; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133393-CEP20/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC116 | Intact | false |
| CEP135 | Biogrid | false |
| KIAA0753 | Biogrid | false |
| OFD1 | Biogrid | false |
| PCM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
