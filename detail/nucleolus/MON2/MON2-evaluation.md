---
type: protein-evaluation
gene: "MON2"
date: 2026-06-03
tags: [protein-scout, nucleolus, re-evaluation, recovery]
status: scored
category: nucleolus
normalized_score: 58.2
raw_score: 106.5
nuclear_score: 4
---

## MON2 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MON2 / KIAA1040, SF21 |
| 蛋白名称 | Protein MON2 homolog |
| 蛋白大小 | 1717 aa / 190.4 kDa |
| UniProt ID | Q7Z3U7 |
| PubMed (strict) | 29 |
| PubMed (broad) | 134 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: Early endosome membrane |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1717 aa / 190.4 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (21-40→8) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9，PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR032629, IPR015403, IPR032691, IPR032 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/183** | |
| **归一化总分** | | | **58.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Approved |
| UniProt | Early endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)
- early endosome membrane (GO:0031901)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 134 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1040, SF21 |

**关键文献**:
1. Dopey proteins are essential but overlooked regulators of membrane trafficking.. *Journal of cell science*. PMID: 35388894
2. Targeted RNA sequencing in diagnostically challenging head and neck carcinomas identifies novel MON2::STAT6, NFATC2::NUTM2B, POC5::RAF1, and NSD3::NCOA2 gene fusions.. *Histopathology*. PMID: 39628352
3. Mon2, a relative of large Arf exchange factors, recruits Dop1 to the Golgi apparatus.. *The Journal of biological chemistry*. PMID: 16301316
4. Mon2-monocytes and increased CD-11b expression before transcatheter aortic valve implantation are associated with earlier death.. *International journal of cardiology*. PMID: 32413468
5. Mon2 is a negative regulator of the monomeric G protein, Arl1.. *FEMS yeast research*. PMID: 22594927

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 28.9% |
| 置信残基 (pLDDT 70-90) 占比 | 49.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 12.5% |
| 有序区域 (pLDDT>70) 占比 | 78.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 78.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR032629, IPR015403, IPR032691, IPR032817; Pfam: PF16213, PF16206, PF09324 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DOP1A | 0.981 | 0.840 | — |
| DOP1B | 0.936 | 0.840 | — |
| MIA3 | 0.766 | 0.000 | — |
| VPS26A | 0.761 | 0.067 | — |
| FBXO38 | 0.748 | 0.000 | — |
| VPS26B | 0.746 | 0.067 | — |
| ATG2B | 0.729 | 0.000 | — |
| ARL1 | 0.709 | 0.572 | — |
| RIC1 | 0.649 | 0.095 | — |
| SEC24B | 0.625 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DOP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| KAP123 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPS0A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| 14-3-3zeta | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| ENSP00000377250.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PET9 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |

**已知复合体成员** (GO Cellular Component):
- cytosol (GO:0005829)
- early endosome membrane (GO:0031901)
- extracellular exosome (GO:0070062)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Early endosome membrane / Nucleoplasm, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. MON2 — Protein MON2 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小1717 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z3U7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000061987-MON2
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000061987-MON2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MON2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z3U7
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MON2
- Packet data timestamp: 2026-06-03 21:51:55

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:51:55），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000061987-MON2/subcellular

![](https://images.proteinatlas.org/38697/431_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38697/431_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38697/437_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38697/437_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38697/443_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38697/443_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z3U7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z3U7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016024;IPR032629;IPR015403;IPR032691;IPR032817; |
| Pfam | PF16213;PF16206;PF09324;PF12783; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000061987-MON2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EGFR | Biogrid | false |
| GGA1 | Intact | false |
| MFSD4A | Biogrid | false |
| NTRK1 | Biogrid | false |
| SPTLC1 | Opencell | false |
| STOM | Intact | false |
| TAF12 | Opencell | false |
| TNFSF13B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
