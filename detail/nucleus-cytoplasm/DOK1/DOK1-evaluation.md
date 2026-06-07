---
type: protein-evaluation
gene: "DOK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOK1 — REJECTED (研究热度过高 (PubMed strict=126，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOK1 |
| 蛋白名称 | Docking protein 1 |
| 蛋白大小 | 481 aa / 52.4 kDa |
| UniProt ID | Q99704 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 481 aa / 52.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=126 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.3; PDB: 2V76 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050996, IPR037751, IPR002404, IPR011993, IPR001 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **77.0/180** | |
| **归一化总分** | | | **42.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 126 |
| PubMed broad count | 246 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Dynamic regulation of integrin β1 phosphorylation supports invasion of breast cancer cells.. *Nature cell biology*. PMID: 40419795
2. DOK1 facilitates the advancement of ccRCC.. *Journal of Cancer*. PMID: 39513119
3. Microautophagy regulated by STK38 and GABARAPs is essential to repair lysosomes and prevent aging.. *EMBO reports*. PMID: 37987447
4. Role of Dok1 in cell signaling mediated by RET tyrosine kinase.. *The Journal of biological chemistry*. PMID: 12087092
5. Subcellular compartmentalization of docking protein-1 contributes to progression in colorectal cancer.. *EBioMedicine*. PMID: 27428427

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.3 |
| 高置信度残基 (pLDDT>90) 占比 | 33.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 36.4% |
| 有序区域 (pLDDT>70) 占比 | 45.8% |
| 可用 PDB 条目 | 2V76 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.3），有序残基占 45.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050996, IPR037751, IPR002404, IPR011993, IPR001849; Pfam: PF02174, PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Abl1 | psi-mi:"MI:0096"(pull down) | pubmed:15148308|imex:IM-19322 |
| Nck1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15148308|imex:IM-19322 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| ORF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| 38918" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| Grb2 | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| BCR | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.3 + PDB: 2V76 | pLDDT=67.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, perinuclear region / Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DOK1 — Docking protein 1，研究基础较多，新颖性有限。
2. 蛋白大小481 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 126 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 126 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99704
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115325-DOK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99704
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000115325-DOK1/subcellular

![](https://images.proteinatlas.org/48561/791_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48561/791_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48561/794_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48561/794_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48561/798_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48561/798_E7_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99704-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99704 |
| SMART | SM01244;SM00233;SM00310; |
| UniProt Domain [FT] | DOMAIN 4..119; /note="PH"; DOMAIN 151..259; /note="IRS-type PTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00389" |
| InterPro | IPR050996;IPR037751;IPR002404;IPR011993;IPR001849; |
| Pfam | PF02174;PF00169; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115325-DOK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CRKL | Intact, Biogrid | true |
| EGFR | Intact, Biogrid | true |
| ABL1 | Biogrid | false |
| BCR | Biogrid | false |
| FGR | Biogrid | false |
| INPP5D | Biogrid | false |
| KIT | Biogrid | false |
| LYN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
