---
type: protein-evaluation
gene: "TLK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TLK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TLK2 |
| 蛋白名称 | Serine/threonine-protein kinase tousled-like 2 |
| 蛋白大小 | 772 aa / 87.7 kDa |
| UniProt ID | Q86UE8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus; Nucleus, nucleoplasm; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 772 aa / 87.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.6; PDB: 5O0Y, 7LO0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Supported |
| UniProt | Nucleus; Nucleus, nucleoplasm; Cytoplasm, perinuclear region; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- intermediate filament (GO:0005882)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Proteogenomics connects somatic mutations to signalling in breast cancer.. *Nature*. PMID: 27251275
2. A TLK2-mediated calcium-driven cell death pathway links neuronal degeneration to nuclear envelope disruption.. *Nature communications*. PMID: 40210858
3. The TLK-ASF1 histone chaperone pathway plays a critical role in IL-1β-mediated AML progression.. *Blood*. PMID: 38498025
4. The Genetic Landscape of Children Born Small for Gestational Age with Persistent Short Stature.. *Hormone research in paediatrics*. PMID: 37019085
5. The circadian E3 ligase complex SCF(FBXL3+CRY) targets TLK2.. *Scientific reports*. PMID: 30655559

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 36.1% |
| 有序区域 (pLDDT>70) 占比 | 62.5% |
| 可用 PDB 条目 | 5O0Y, 7LO0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5O0Y, 7LO0）+ AlphaFold高质量预测（pLDDT=71.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASF1A | 0.997 | 0.985 | — |
| TLK1 | 0.995 | 0.994 | — |
| ASF1B | 0.981 | 0.875 | — |
| CABIN1 | 0.821 | 0.784 | — |
| SRSF1 | 0.805 | 0.000 | — |
| CDK13 | 0.658 | 0.000 | — |
| DYNLL2 | 0.651 | 0.628 | — |
| CUL3 | 0.631 | 0.000 | — |
| HIRA | 0.629 | 0.570 | — |
| SPATA1 | 0.623 | 0.623 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000316512.9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ASF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IRF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| IRF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| RPS6KA1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| CEP70 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GMCL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PAX6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DMAP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| UBE2I | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 5O0Y, 7LO0 | pLDDT=71.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Cytoplasm, perinucl / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TLK2 — Serine/threonine-protein kinase tousled-like 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小772 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UE8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146872-TLK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UE8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TLK2/IF_images/TLK2_IF_957_D12_1_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000146872-TLK2/subcellular

![](https://images.proteinatlas.org/56342/941_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/56342/941_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/56342/957_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/56342/957_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/56342/966_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/56342/966_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UE8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86UE8 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 462..741; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146872-TLK2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASF1A | Intact, Biogrid | true |
| ASF1B | Intact, Biogrid | true |
| DYNLL1 | Intact, Biogrid, Opencell | true |
| DYNLL2 | Intact, Biogrid, Opencell | true |
| IRF4 | Intact, Biogrid | true |
| IRF7 | Intact, Biogrid | true |
| TLK1 | Biogrid, Opencell | true |
| AURKA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
