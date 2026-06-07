---
type: protein-evaluation
gene: "LENG8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LENG8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LENG8 / KIAA1932 |
| 蛋白名称 | Leukocyte receptor cluster member 8 |
| 蛋白大小 | 800 aa / 88.2 kDa |
| UniProt ID | Q96PV6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 800 aa / 88.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000717, IPR045107, IPR005062; Pfam: PF03399 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1932 |

**关键文献**:
1. Structural mechanism of DDX39B regulation by human TREX-2 and a related complex in mRNP remodeling.. *Nature communications*. PMID: 40595470
2. Development and validation of cuproptosis-related lncRNA signatures for prognosis prediction in colorectal cancer.. *BMC medical genomics*. PMID: 36949429
3. LENG8 mediates RNA nuclear retention and degradation in eukaryotes.. *bioRxiv : the preprint server for biology*. PMID: 40832163
4. LENG8-AS1: A Prognostic Biomarker in Colorectal Cancer-Differential Expression and Clinical Implications.. *Indian journal of clinical biochemistry : IJCB*. PMID: 41675117
5. Potential susceptibility genes in patients with stage III and IV periodontitis: A whole-exome sequencing pilot study.. *Biomolecules & biomedicine*. PMID: 37435641

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.6 |
| 高置信度残基 (pLDDT>90) 占比 | 3.8% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 55.4% |
| 有序区域 (pLDDT>70) 占比 | 34.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.6），有序残基占 34.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000717, IPR045107, IPR005062; Pfam: PF03399 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCID2 | 0.966 | 0.945 | — |
| CDC42EP5 | 0.672 | 0.000 | — |
| TTYH1 | 0.648 | 0.000 | — |
| NCBP3 | 0.630 | 0.602 | — |
| GIGYF1 | 0.623 | 0.000 | — |
| LENG9 | 0.621 | 0.000 | — |
| FNBP4 | 0.620 | 0.000 | — |
| LAIR2 | 0.573 | 0.000 | — |
| LAIR1 | 0.564 | 0.000 | — |
| FCAR | 0.530 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RHOXF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| deoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000480663.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pyrG | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fdhD2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DMRTB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| MAPK1IP1L | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| PYGO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.6 + PDB: 无 | pLDDT=55.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LENG8 — Leukocyte receptor cluster member 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小800 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PV6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167615-LENG8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LENG8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PV6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LENG8/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LENG8/IF_images/U-251MG_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000167615-LENG8/subcellular

![](https://images.proteinatlas.org/42004/537_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/42004/537_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/42004/540_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/42004/540_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/42004/553_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/42004/553_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96PV6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96PV6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 636..800; /note="PCI"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01185" |
| InterPro | IPR000717;IPR045107;IPR005062; |
| Pfam | PF03399; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167615-LENG8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SNRPA | Intact, Biogrid | true |
| ARID5A | Intact | false |
| ATN1 | Biogrid | false |
| BAG3 | Intact | false |
| CAMK2A | Intact | false |
| CEP70 | Intact | false |
| CFAP53 | Intact | false |
| COG2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
