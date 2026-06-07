---
type: protein-evaluation
gene: "IGFN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IGFN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IGFN1 / EEF1A2BP1, KYIP1 |
| 蛋白名称 | Immunoglobulin-like and fibronectin type III domain-containing protein 1 |
| 蛋白大小 | 1251 aa / 137.8 kDa |
| UniProt ID | Q86VF2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Midbody ring; UniProt: Nucleus; Cytoplasm, myofibril, sarcomere, Z line |
| 蛋白大小 | 5/10 | ×1 | 5 | 1251 aa / 137.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003961, IPR036116, IPR007110, IPR036179, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Midbody ring | Approved |
| UniProt | Nucleus; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EEF1A2BP1, KYIP1 |

**关键文献**:
1. Single nuclei profiling identifies cell specific markers of skeletal muscle aging, frailty, and senescence.. *Aging*. PMID: 36516485
2. Whole-Exome Sequencing Among Chinese Patients With Hereditary Diffuse Gastric Cancer.. *JAMA network open*. PMID: 36484990
3. Identification of a Z-band associated protein complex involving KY, FLNC and IGFN1.. *Experimental cell research*. PMID: 20206623
4. Recognition of a Novel Gene Signature for Human Glioblastoma.. *International journal of molecular sciences*. PMID: 35456975
5. Proteomic resolution of IGFN1 complexes reveals a functional interaction with the actin nucleating protein COBL.. *Experimental cell research*. PMID: 32768501

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 21.8% |
| 置信残基 (pLDDT 70-90) 占比 | 53.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.7% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.4，有序区 75.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR007110, IPR036179, IPR013783; Pfam: PF00041, PF07679, PF18362 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLNC | 0.682 | 0.071 | — |
| FSIP2 | 0.556 | 0.074 | — |
| COBL | 0.550 | 0.087 | — |
| MSS51 | 0.493 | 0.079 | — |
| GAREM1 | 0.463 | 0.460 | — |
| FRAS1 | 0.415 | 0.000 | — |
| PRAMEF13 | 0.414 | 0.098 | — |
| AHNAK2 | 0.409 | 0.074 | — |
| OSBPL3 | 0.408 | 0.000 | — |
| FNDC10 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| POF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KIFC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TAX1BP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LHX9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SERTAD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PIBF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MYOD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| USP54 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NHLRC4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 无 | pLDDT=77.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, myofibril, sarcomere, Z line / Midbody ring | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

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
1. IGFN1 — Immunoglobulin-like and fibronectin type III domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1251 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163395-IGFN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IGFN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VF2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Midbody ring (approved)。来源: https://www.proteinatlas.org/ENSG00000163395-IGFN1/subcellular

![](https://images.proteinatlas.org/50415/780_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50415/780_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50415/788_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50415/788_C9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86VF2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86VF2 |
| SMART | SM00060;SM00409;SM00408; |
| UniProt Domain [FT] | DOMAIN 29..119; /note="Ig-like 1"; DOMAIN 309..398; /note="Ig-like 2"; DOMAIN 454..539; /note="Ig-like 3"; DOMAIN 646..741; /note="Fibronectin type-III 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316"; DOMAIN 746..845; /note="Fibronectin type-III 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316"; DOMAIN 847..942; /note="Fibronectin type-III 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316"; DOMAIN 946..1030; /note="Ig-like 4"; DOMAIN 1043..1137; /note="Fibronectin type-III 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316"; DOMAIN 1151..1245; /note="Ig-like 5" |
| InterPro | IPR003961;IPR036116;IPR007110;IPR036179;IPR013783;IPR013098;IPR003599;IPR003598;IPR040849;IPR050964; |
| Pfam | PF00041;PF07679;PF18362; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163395-IGFN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KLHL25 | Intact | false |
| MEOX2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
