---
type: protein-evaluation
gene: "RORA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RORA — REJECTED (研究热度过高 (PubMed strict=389，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RORA / NR1F1, RZRA |
| 蛋白名称 | Nuclear receptor ROR-alpha |
| 蛋白大小 | 523 aa / 59.0 kDa |
| UniProt ID | P35398 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 523 aa / 59.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=389 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.3; PDB: 1N83, 1S0X, 4S15 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035500, IPR044101, IPR000536, IPR001723, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 389 |
| PubMed broad count | 925 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1F1, RZRA |

**关键文献**:
1. Stargardt's Disease: Molecular Pathogenesis and Current Therapeutic Landscape.. *International journal of molecular sciences*. PMID: 40725253
2. Cancer cells avoid ferroptosis induced by immune cells via fatty acid binding proteins.. *Molecular cancer*. PMID: 39901247
3. The single-cell transcriptomic atlas and RORA-mediated 3D epigenomic remodeling in driving corneal epithelial differentiation.. *Nature communications*. PMID: 38177186
4. Combining single-cell RNA sequencing and network pharmacology to explore the target of cangfu daotan decoction in the treatment of obese polycystic ovary syndrome from an immune perspective.. *Frontiers in pharmacology*. PMID: 39539629
5. Secretome from estrogen-responding human placenta-derived mesenchymal stem cells rescues ovarian function and circadian rhythm in mice with cyclophosphamide-induced primary ovarian insufficiency.. *Journal of biomedical science*. PMID: 39390588

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 55.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 30.2% |
| 有序区域 (pLDDT>70) 占比 | 66.1% |
| 可用 PDB 条目 | 1N83, 1S0X, 4S15 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1N83, 1S0X, 4S15）+ AlphaFold高质量预测（pLDDT=75.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035500, IPR044101, IPR000536, IPR001723, IPR003079; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WNT5A | 0.992 | 0.000 | — |
| NRIP1 | 0.982 | 0.900 | — |
| NPAS2 | 0.981 | 0.113 | — |
| ARNTL | 0.962 | 0.113 | — |
| EP300 | 0.960 | 0.292 | — |
| KAT5 | 0.942 | 0.000 | — |
| RORB | 0.941 | 0.000 | — |
| CRY1 | 0.935 | 0.095 | — |
| RORC | 0.934 | 0.000 | — |
| CLOCK | 0.923 | 0.113 | — |

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
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 1N83, 1S0X, 4S15 | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. RORA — Nuclear receptor ROR-alpha，研究基础较多，新颖性有限。
2. 蛋白大小523 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 389 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 389 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35398
- Protein Atlas: https://www.proteinatlas.org/ENSG00000069667-RORA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RORA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35398
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000069667-RORA/subcellular

![](https://images.proteinatlas.org/74448/1565_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74448/1565_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74448/1569_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74448/1569_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74448/1697_D3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74448/1697_D3_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P35398-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P35398 |
| SMART | SM00430;SM00399; |
| UniProt Domain [FT] | DOMAIN 272..510; /note="NR LBD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01189" |
| InterPro | IPR035500;IPR044101;IPR000536;IPR001723;IPR003079;IPR001628;IPR013088; |
| Pfam | PF00104;PF00105; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000069667-RORA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NR0B1 | Intact, Biogrid | true |
| PSMC5 | Intact, Biogrid | true |
| DCAF1 | Biogrid | false |
| DDB1 | Biogrid | false |
| EP300 | Biogrid | false |
| GFAP | Intact | false |
| ITCH | Biogrid | false |
| NCOA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
