---
type: protein-evaluation
gene: "CBR1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBR1 — REJECTED (研究热度过高 (PubMed strict=189，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBR1 / CBR, CRN, SDR21C1 |
| 蛋白名称 | Carbonyl reductase [NADPH] 1 |
| 蛋白大小 | 277 aa / 30.4 kDa |
| UniProt ID | P16152 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 277 aa / 30.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=189 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.8; PDB: 1WMA, 2PFG, 3BHI, 3BHJ, 3BHM, 4Z3D |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045313, IPR036291, IPR020904, IPR002347; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular vesicle (GO:1903561)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 189 |
| PubMed broad count | 385 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CBR, CRN, SDR21C1 |

**关键文献**:
1. Integrated ubiquitomics characterization of hepatocellular carcinomas.. *Hepatology (Baltimore, Md.)*. PMID: 39348425
2. Functional Validation of Doxorubicin-Induced Cardiotoxicity-Related Genes.. *JACC. CardioOncology*. PMID: 38510289
3. Human carbonyl reductases.. *Current drug metabolism*. PMID: 20942781
4. Human skeletal muscle possesses both reversible proteomic signatures and a retained proteomic memory after repeated resistance training.. *The Journal of physiology*. PMID: 40183698
5. Vitamin K2 inhibits PGE2-mediated osteoblast ferroptosis by upregulation of CBR1 via the Nrf2/Keap1 pathway.. *Communications biology*. PMID: 40721947

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.8 |
| 高置信度残基 (pLDDT>90) 占比 | 98.6% |
| 置信残基 (pLDDT 70-90) 占比 | 0.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 99.0% |
| 可用 PDB 条目 | 1WMA, 2PFG, 3BHI, 3BHJ, 3BHM, 4Z3D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1WMA, 2PFG, 3BHI, 3BHJ, 3BHM, 4Z3D）+ AlphaFold极高置信度预测（pLDDT=97.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045313, IPR036291, IPR020904, IPR002347; Pfam: PF00106 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKR1B1 | 0.991 | 0.045 | — |
| CBR3 | 0.983 | 0.727 | — |
| DHFR2 | 0.981 | 0.000 | — |
| DHFR | 0.975 | 0.000 | — |
| SPR | 0.974 | 0.000 | — |
| AKR1C3 | 0.971 | 0.045 | — |
| AKR1B10 | 0.959 | 0.045 | — |
| CYP3A4 | 0.941 | 0.000 | — |
| PTGES3 | 0.939 | 0.057 | — |
| PTGES | 0.939 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| ERCC8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FTSJ1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NME2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.8 + PDB: 1WMA, 2PFG, 3BHI, 3BHJ, 3BHM,  | pLDDT=97.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CBR1 — Carbonyl reductase [NADPH] 1，研究基础较多，新颖性有限。
2. 蛋白大小277 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 189 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 189 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16152
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159228-CBR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16152
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000159228-CBR1/subcellular

![](https://images.proteinatlas.org/18433/1126_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/18433/1126_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/18433/144_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/18433/144_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16152-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P16152 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045313;IPR036291;IPR020904;IPR002347; |
| Pfam | PF00106; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159228-CBR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBR3 | Intact, Biogrid, Bioplex | true |
| AGPAT1 | Bioplex | false |
| C18orf21 | Bioplex | false |
| CCR1 | Bioplex | false |
| CERS3 | Bioplex | false |
| EGFR | Intact | false |
| ESR1 | Biogrid | false |
| GAPDHS | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
