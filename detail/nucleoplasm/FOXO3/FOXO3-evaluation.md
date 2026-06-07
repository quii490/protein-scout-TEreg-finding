---
type: protein-evaluation
gene: "FOXO3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXO3 — REJECTED (研究热度过高 (PubMed strict=1579，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXO3 / FKHRL1, FOXO3A |
| 蛋白名称 | Forkhead box protein O3 |
| 蛋白大小 | 673 aa / 71.3 kDa |
| UniProt ID | O43524 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytosol; Nucleus; Mitochondrion matrix; Mitochond |
| 蛋白大小 | 10/10 | ×1 | 10 | 673 aa / 71.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1579 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.7; PDB: 2K86, 2LQH, 2LQI, 2UZK, 6MNL, 7V9B, 9QNG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001766, IPR032067, IPR032068, IPR030456, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm, cytosol; Nucleus; Mitochondrion matrix; Mitochondrion outer membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrial matrix (GO:0005759)
- mitochondrial outer membrane (GO:0005741)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1579 |
| PubMed broad count | 4421 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKHRL1, FOXO3A |

**关键文献**:
1. FOXO3-Engineered Human ESC-Derived Vascular Cells Promote Vascular Protection and Regeneration.. *Cell stem cell*. PMID: 30661960
2. The rules and regulatory mechanisms of FOXO3 on inflammation, metabolism, cell death and aging in hosts.. *Life sciences*. PMID: 37352918
3. The COPS3-FOXO3 positive feedback loop regulates autophagy to promote cisplatin resistance in osteosarcoma.. *Autophagy*. PMID: 36451342
4. SIRT1-mediated deacetylation of FOXO3 enhances mitophagy and drives hormone resistance in endometrial cancer.. *Molecular medicine (Cambridge, Mass.)*. PMID: 39266959
5. Dnmt3a-mediated hypermethylation of FoxO3 promotes redox imbalance during osteoclastogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40106360

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.7 |
| 高置信度残基 (pLDDT>90) 占比 | 9.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.5% |
| 低置信 (pLDDT<50) 占比 | 69.1% |
| 有序区域 (pLDDT>70) 占比 | 13.4% |
| 可用 PDB 条目 | 2K86, 2LQH, 2LQI, 2UZK, 6MNL, 7V9B, 9QNG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.7），有序残基占 13.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001766, IPR032067, IPR032068, IPR030456, IPR036388; Pfam: PF00250, PF16676, PF16675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIRT1 | 0.999 | 0.774 | — |
| CDK2 | 0.999 | 0.117 | — |
| TP53 | 0.998 | 0.776 | — |
| AKT1 | 0.998 | 0.853 | — |
| CTNNB1 | 0.998 | 0.546 | — |
| HIF1A | 0.997 | 0.311 | — |
| CDKN1A | 0.995 | 0.294 | — |
| SMAD3 | 0.995 | 0.634 | — |
| MDM2 | 0.995 | 0.742 | — |
| CREBBP | 0.995 | 0.971 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| B4DVZ6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ENSMUSP00000135380.2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24477|pubmed:20072126 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| YWHAH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11897|pubmed:17979178 |
| ATG101 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NIPSNAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| FKBP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PGK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.7 + PDB: 2K86, 2LQH, 2LQI, 2UZK, 6MNL,  | pLDDT=50.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Mitochondrion matrix; / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXO3 — Forkhead box protein O3，研究基础较多，新颖性有限。
2. 蛋白大小673 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1579 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1579 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43524
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118689-FOXO3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXO3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43524
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000118689-FOXO3/subcellular

![](https://images.proteinatlas.org/4074/624_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/4074/624_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/4074/628_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/4074/628_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/4074/630_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/4074/630_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43524-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43524 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR032067;IPR032068;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250;PF16676;PF16675; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000118689-FOXO3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKT1 | Intact, Biogrid | true |
| CREBBP | Intact, Biogrid | true |
| SIRT1 | Intact, Biogrid | true |
| SMAD3 | Intact, Biogrid | true |
| SMAD4 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
