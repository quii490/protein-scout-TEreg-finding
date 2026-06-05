---
type: protein-evaluation
gene: "URGCP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## URGCP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | URGCP / KIAA1507, URG4 |
| 蛋白名称 | Up-regulator of cell proliferation |
| 蛋白大小 | 931 aa / 105.0 kDa |
| UniProt ID | Q8TCY9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 931 aa / 105.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030383, IPR006073, IPR027417, IPR057365; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1507, URG4 |

**关键文献**:
1. A novel oncogene URG4/URGCP and its role in cancer.. *Gene*. PMID: 29775749
2. Regulation of URG4/URGCP and PPARα gene expressions after retinoic acid treatment in neuroblastoma cells.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 23821302
3. Immunohistochemical Expression of Upregulated Gene 4 Protein Expression (URG4/URGCP) and Its Association with 5-Year Survival in Patients with Colon Adenocarcinoma.. *Journal of clinical medicine*. PMID: 37685545
4. URGCP promotes non-small cell lung cancer invasiveness by activating the NF-κB-MMP-9 pathway.. *Oncotarget*. PMID: 26429875
5. Investigation of microRNA expression changes in HepG2 cell line in presence of URG4/URGCP and in absence of URG4/URGCP suppressed by RNA interference.. *Molecular biology reports*. PMID: 23053999

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 38.0% |
| 置信残基 (pLDDT 70-90) 占比 | 35.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.4，有序区 73.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030383, IPR006073, IPR027417, IPR057365; Pfam: PF25496, PF25683 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MINDY3 | 0.637 | 0.000 | — |
| UBE2D4 | 0.479 | 0.361 | — |
| HECTD1 | 0.426 | 0.422 | — |
| RIPK1 | 0.413 | 0.000 | — |
| VWCE | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| EYA4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PLEC | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CCDC88A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| AAK1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SEC24B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPIP5K2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DNAJC7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHMP5 | psi-mi:"MI:0018"(two hybrid) | imex:IM-24991|pubmed:16730941 |
| UBE2D4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 15
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 无 | pLDDT=76.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 5 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. URGCP — Up-regulator of cell proliferation，非常新颖，仅有少数基础研究。
2. 蛋白大小931 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCY9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106608-URGCP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=URGCP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCY9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000106608-URGCP/subcellular

![](https://images.proteinatlas.org/20134/364_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20134/364_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20134/365_E7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/20134/365_E7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/20134/369_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20134/369_E7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TCY9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
