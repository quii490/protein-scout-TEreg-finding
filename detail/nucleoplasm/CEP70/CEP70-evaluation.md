---
type: protein-evaluation
gene: "CEP70"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CEP70 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP70 / BITE |
| 蛋白名称 | Centrosomal protein of 70 kDa |
| 蛋白大小 | 597 aa / 69.8 kDa |
| UniProt ID | Q8NHQ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA: Nucleoplasm, Primary cilium, Cytosol; 额外: Centrosome, Basal body; UniProt: Cytoplasm, cytoskele |
| 蛋白大小 | 10/10 | ×1 | 10 | 597 aa / 69.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.8; PDB: 暂无 |
| 调控结构域 | 5/10 | ×2 | 10 | InterPro: IPR037692, IPR019734 |
| PPI 网络 | 9/10 | ×3 | 27 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **143.0/180** | |
| **归一化总分 (÷1.83)** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Primary cilium, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | ECO:0000269, ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- centrosome (GO:0005813) [IDA:UniProtKB]
- cytosol (GO:0005829) [TAS:Reactome]
- microtubule organizing center (GO:0005815) [IBA:GO_Central]

**结论**: HPA: Nucleoplasm, Primary cilium, Cytosol; 额外: Centrosome, Basal body; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome

#### 3.2 蛋白大小评估

**评价**: 597 aa / 69.8 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed 搜索链接 | [CEP70 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CEP70) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 23.5% |
| 置信残基 (pLDDT 70-90) 占比 | 49.4% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 10.9% |
| 有序区域 (pLDDT>70) 占比 | 72.9% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037692, IPR019734 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD19 | 0.979 | 0.000 | — |
| PLK1 | 0.815 | 0.000 | — |
| CD33 | 0.751 | 0.000 | — |
| FOLH1 | 0.732 | 0.000 | — |
| GPRC5D | 0.705 | 0.000 | — |
| TNFRSF17 | 0.684 | 0.000 | — |
| HAUS1 | 0.664 | 0.240 | — |
| EGFR | 0.658 | 0.000 | — |
| HAUS5 | 0.646 | 0.000 | — |
| ERBB2 | 0.643 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000419743.1 | psi-mi:"MI:2215"(barcode fusion genetics two hybrid) | doi:10.15252/msb.20156660|pubmed:27107012|imex:IM-25015 |
| ENSP00000419231.1 | psi-mi:"MI:2215"(barcode fusion genetics two hybrid) | doi:10.15252/msb.20156660|pubmed:27107012|imex:IM-25015 |
| NRIP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ZBTB8A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| KANSL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ENKD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ELOA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| UTP14A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 1/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=76.8, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome / Nucleoplasm, Primary cilium, Cytosol | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域注释 + AlphaFold 预测: +0.25

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 78.1/100

**核心优势**:
1. CEP70 — Centrosomal protein of 70 kDa，极度新颖，几乎未被系统研究（PubMed 20 篇）。
2. 蛋白大小597 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHQ1
- Protein Atlas: https://www.proteinatlas.org/search/CEP70
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP70
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHQ1
- STRING: https://string-db.org/network/9606.CEP70
- Packet data timestamp: 2026-06-03 04:50:08

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000114107-CEP70/subcellular

![](https://images.proteinatlas.org/36941/2179_E1_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/36941/2179_E1_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/36941/2206_B1_184_blue_red_green.jpg)
![](https://images.proteinatlas.org/36941/2206_B1_204_blue_red_green.jpg)
![](https://images.proteinatlas.org/36941/2210_G1_133_blue_red_green.jpg)
![](https://images.proteinatlas.org/36941/2210_G1_162_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHQ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NHQ1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037692;IPR019734; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114107-CEP70/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARHGEF3 | Intact, Biogrid | true |
| C8orf33 | Intact, Biogrid | true |
| CDC73 | Intact, Biogrid | true |
| CDCA7L | Intact, Biogrid | true |
| ENKD1 | Intact, Biogrid | true |
| KANSL1 | Intact, Biogrid | true |
| KDM1A | Intact, Biogrid | true |
| METTL17 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
