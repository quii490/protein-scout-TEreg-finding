---
type: protein-evaluation
gene: "DHPS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHPS — REJECTED (研究热度过高 (PubMed strict=500，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHPS / DS |
| 蛋白名称 | Deoxyhypusine synthase |
| 蛋白大小 | 369 aa / 41.0 kDa |
| UniProt ID | P49366 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 369 aa / 41.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=500 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.1; PDB: 1DHS, 1RLZ, 1ROZ, 1RQD, 6P4V, 6PGR, 6WKZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002773, IPR036982, IPR029035; Pfam: PF01916 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 500 |
| PubMed broad count | 1559 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DS |

**关键文献**:
1. Spermidine-mediated hypusination of translation factor EIF5A improves mitochondrial fatty acid oxidation and prevents non-alcoholic steatohepatitis progression.. *Nature communications*. PMID: 36057633
2. Knockout or inhibition of DHPS suppresses ovarian tumor growth and metastasis by attenuating the TGFβ pathway.. *Scientific reports*. PMID: 39762448
3. Hypusine Signaling Promotes Pulmonary Vascular Remodeling in Pulmonary Arterial Hypertension.. *American journal of respiratory and critical care medicine*. PMID: 38261723
4. Hypusination Maintains Intestinal Homeostasis and Prevents Colitis and Carcinogenesis by Enhancing Aldehyde Detoxification.. *Gastroenterology*. PMID: 37271289
5. Impact of dhps mutations on sulfadoxine-pyrimethamine protective efficacy and implications for malaria chemoprevention.. *Nature communications*. PMID: 40341172

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 89.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 93.2% |
| 可用 PDB 条目 | 1DHS, 1RLZ, 1ROZ, 1RQD, 6P4V, 6PGR, 6WKZ, 6WL6, 6XXH, 6XXI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1DHS, 1RLZ, 1ROZ, 1RQD, 6P4V, 6PGR, 6WKZ, 6WL6, 6XXH, 6XXI）+ AlphaFold极高置信度预测（pLDDT=94.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002773, IPR036982, IPR029035; Pfam: PF01916 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF5A | 0.999 | 0.799 | — |
| DOHH | 0.999 | 0.091 | — |
| EIF5A2 | 0.993 | 0.882 | — |
| EIF5AL1 | 0.924 | 0.521 | — |
| MAPK3 | 0.841 | 0.819 | — |
| DHFR | 0.792 | 0.000 | — |
| ODC1 | 0.745 | 0.069 | — |
| SRM | 0.728 | 0.067 | — |
| RPL9 | 0.722 | 0.655 | — |
| SMS | 0.694 | 0.064 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| folP | psi-mi:"MI:0018"(two hybrid) | pubmed:18000013 |
| sulA | psi-mi:"MI:0946"(miniaturized immunoprecipitation) | pubmed:19098921|imex:IM-20227 |
| FOL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| bglG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| groES | psi-mi:"MI:0946"(miniaturized immunoprecipitation) | pubmed:19098921|imex:IM-20227 |
| malR | psi-mi:"MI:0946"(miniaturized immunoprecipitation) | pubmed:19098921|imex:IM-20227 |
| JJJ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| XDJ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA1 | psi-mi:"MI:0096"(pull down) | imex:IM-18714|pubmed:23217712 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 1DHS, 1RLZ, 1ROZ, 1RQD, 6P4V,  | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DHPS — Deoxyhypusine synthase，研究基础较多，新颖性有限。
2. 蛋白大小369 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 500 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 500 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49366
- Protein Atlas: https://www.proteinatlas.org/ENSG00000095059-DHPS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHPS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49366
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000095059-DHPS/subcellular

![](https://images.proteinatlas.org/29413/2018_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/29413/2018_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/29413/303_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/29413/303_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/29413/342_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/29413/342_G3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49366-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49366 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002773;IPR036982;IPR029035; |
| Pfam | PF01916; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000095059-DHPS/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EIF5A2 | Intact, Biogrid | true |
| MAPK3 | Intact, Biogrid | true |
| RPL9 | Intact, Biogrid | true |
| ARHGAP15 | Intact | false |
| BRCA1 | Biogrid | false |
| EIF5A | Intact | false |
| LNX1 | Intact | false |
| MAPK1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
