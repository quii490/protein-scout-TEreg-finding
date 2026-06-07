---
type: protein-evaluation
gene: "CERT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CERT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERT1 / CERT / COL4A3BP / STARD11 |
| 蛋白名称 | Ceramide transfer protein |
| 蛋白大小 | 624 aa / 70.8 kDa |
| UniProt ID | Q9Y5P4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cytoplasm; Golgi apparatus; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 624 aa / 70.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.0; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR011993, IPR001849, IPR041952, IPR023393, IPR002913, IPR051213; Pfam: PF00169, PF01852 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **146.2/180** | |
| **归一化总分 (÷1.83)** | | | **79.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Enhanced |
| UniProt | Cytoplasm | ECO:0000269, ECO:0000269
| UniProt | Golgi apparatus | ECO:0000269, ECO:0000269, ECO:0000269
| UniProt | Endoplasmic reticulum | ECO:0000269, ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829) [IBA:GO_Central]
- endoplasmic reticulum membrane (GO:0005789) [TAS:Reactome]
- endoplasmic reticulum-trans-Golgi network membrane contact site (GO:0160258) [IDA:UOS_MCB]
- Golgi apparatus (GO:0005794) [IDA:HPA]
- mitochondrion (GO:0005739) [IEA:Ensembl]
- nucleoplasm (GO:0005654) [IDA:HPA]

**结论**: HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cytoplasm; Golgi apparatus; Endoplasmic reticulum

#### 3.2 蛋白大小评估

**评价**: 624 aa / 70.8 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed 搜索链接 | [CERT1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERT1) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.0 |
| 高置信度残基 (pLDDT>90) 占比 | 45.5% |
| 置信残基 (pLDDT 70-90) 占比 | 24.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 21.2% |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR041952, IPR023393, IPR002913, IPR051213; Pfam: PF00169, PF01852 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAPA | 0.990 | 0.100 | — |
| CSNK1G2 | 0.960 | 0.769 | — |
| VAPB | 0.930 | 0.100 | — |
| APCS | 0.862 | 0.405 | — |
| COL4A3 | 0.831 | 0.000 | — |
| PCTP | 0.798 | 0.000 | — |
| COL18A1 | 0.797 | 0.000 | — |
| PRKD3 | 0.751 | 0.000 | — |
| PLEK | 0.751 | 0.000 | — |
| PLEK2 | 0.749 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000495760.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ENSP00000496243.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ITGB3BP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| RTN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| POM121 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| TGM2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| polA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RTN3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| CSNK1G2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| MARK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=77.0, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm; Golgi apparatus; Endoplasmic reticulum / Golgi apparatus | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 79.9/100

**核心优势**:
1. CERT1 — Ceramide transfer protein，极度新颖，几乎未被系统研究（PubMed 15 篇）。
2. 蛋白大小624 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5P4
- Protein Atlas: https://www.proteinatlas.org/search/CERT1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CERT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5P4
- STRING: https://string-db.org/network/9606.CERT1
- Packet data timestamp: 2026-06-03 04:52:12

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (enhanced)。来源: https://www.proteinatlas.org/ENSG00000113163-CERT1/subcellular

![](https://images.proteinatlas.org/35645/380_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/35645/380_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/35645/382_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/35645/382_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/35645/397_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/35645/397_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y5P4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y5P4 |
| SMART | SM00233;SM00234; |
| UniProt Domain [FT] | DOMAIN 23..117; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 389..618; /note="START"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00197" |
| InterPro | IPR011993;IPR001849;IPR041952;IPR023393;IPR002913;IPR051213; |
| Pfam | PF00169;PF01852; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000113163-CERT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARL6IP1 | Intact, Biogrid | true |
| CSNK1G2 | Intact, Biogrid | true |
| ITGB3BP | Intact, Biogrid | true |
| RTN3 | Intact, Biogrid | true |
| RTN4 | Intact, Biogrid | true |
| ACTL8 | Intact | false |
| APCS | Intact | false |
| MARK2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
