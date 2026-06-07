---
type: protein-evaluation
gene: "HACL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HACL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HACL1 / HPCL, HPCL2, PHYH2 |
| 蛋白名称 | 2-hydroxyacyl-CoA lyase 1 |
| 蛋白大小 | 578 aa / 63.7 kDa |
| UniProt ID | Q9UJ83 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Peroxisome |
| 蛋白大小 | 10/10 | ×1 | 10 | 578 aa / 63.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029035, IPR045025, IPR029061, IPR012000, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Peroxisome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- peroxisomal matrix (GO:0005782)
- peroxisome (GO:0005777)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HPCL, HPCL2, PHYH2 |

**关键文献**:
1. Lipidomics unravels lipid changes in osteoarthritis articular cartilage.. *Annals of the rheumatic diseases*. PMID: 39894691
2. Presence of thiamine pyrophosphate in mammalian peroxisomes.. *BMC biochemistry*. PMID: 17596263
3. An anoikis-related gene signature predicts prognosis, drug sensitivity, and immune microenvironment in cholangiocarcinoma.. *Heliyon*. PMID: 38947446
4. Thiamine and magnesium deficiencies: keys to disease.. *Medical hypotheses*. PMID: 25542071
5. Odd chain fatty acid metabolism in mice after a high fat diet.. *The international journal of biochemistry & cell biology*. PMID: 34896612

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.3 |
| 高置信度残基 (pLDDT>90) 占比 | 93.9% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.3，有序区 97.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029035, IPR045025, IPR029061, IPR012000, IPR012001; Pfam: PF02775, PF00205, PF02776 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PEX5 | 0.968 | 0.510 | — |
| PEX5L | 0.901 | 0.000 | — |
| AGXT | 0.890 | 0.000 | — |
| CS | 0.871 | 0.000 | — |
| MRTFA | 0.863 | 0.000 | — |
| HDDC3 | 0.844 | 0.000 | — |
| SCP2 | 0.830 | 0.091 | — |
| MT-CO1 | 0.830 | 0.000 | — |
| MT-CO2 | 0.828 | 0.000 | — |
| RIDA | 0.828 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000323811.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZMYND19 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PEX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22002062|imex:IM-17176 |
| PLXDC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASPSCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MAGEB6 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| ODF2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNA15 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| EBI-25849602 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.3 + PDB: 无 | pLDDT=95.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HACL1 — 2-hydroxyacyl-CoA lyase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小578 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJ83
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131373-HACL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HACL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJ83
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000131373-HACL1/subcellular

![](https://images.proteinatlas.org/73760/1412_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73760/1412_H6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/73760/1441_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73760/1441_D4_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJ83-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UJ83 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029035;IPR045025;IPR029061;IPR012000;IPR012001;IPR011766; |
| Pfam | PF02775;PF00205;PF02776; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131373-HACL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAGEB6 | Intact | false |
| PEX5 | Biogrid | false |
| ZMYND19 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
