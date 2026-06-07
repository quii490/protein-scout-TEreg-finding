---
type: protein-evaluation
gene: "C2CD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C2CD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C2CD3 |
| 蛋白名称 | C2 domain-containing protein 3 |
| 蛋白大小 | 2353 aa / 260.4 kDa |
| UniProt ID | Q4AC94 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Centrosome, Basal body; 额外: Acrosome, Equatoria; UniProt: Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytos |
| 蛋白大小 | 2/10 | ×1 | 2 | 2353 aa / 260.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037775, IPR057537, IPR000008, IPR035892; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome, Basal body; 额外: Acrosome, Equatorial segment, Principal piece | Supported |
| UniProt | Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- microtubule organizing center (GO:0005815)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Joubert Syndrome.. **. PMID: 20301500
2. The ciliary protein C2cd3 is required for mandibular musculoskeletal tissue patterning.. *Differentiation; research in biological diversity*. PMID: 38810379
3. The luminal ring protein C2CD3 acts as a radial in-to-out organizer of the distal centriole and appendages.. *PLoS biology*. PMID: 41364719
4. CEP120 interacts with C2CD3 and Talpid3 and is required for centriole appendage assembly and ciliogenesis.. *Scientific reports*. PMID: 30988386
5. The value of genome-wide analysis in craniosynostosis.. *Frontiers in genetics*. PMID: 38318288

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 3.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 49.9% |
| 有序区域 (pLDDT>70) 占比 | 38.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 38.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037775, IPR057537, IPR000008, IPR035892; Pfam: PF00168, PF25339 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OFD1 | 0.821 | 0.436 | — |
| CEP164 | 0.786 | 0.000 | — |
| CEP89 | 0.764 | 0.089 | — |
| IFT88 | 0.735 | 0.000 | — |
| CEP120 | 0.732 | 0.000 | — |
| SCLT1 | 0.726 | 0.000 | — |
| CEP83 | 0.720 | 0.000 | — |
| FBF1 | 0.677 | 0.000 | — |
| KIAA0586 | 0.623 | 0.000 | — |
| CPLANE1 | 0.615 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2AC12 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| OFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep131 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep120 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep135 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BBS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-25741|pubmed:24997988 |
| BBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-25741|pubmed:24997988 |
| BBS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-25741|pubmed:24997988 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium basal body; Cytopl / Nucleoplasm, Centrosome, Basal body; 额外: Acrosome, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C2CD3 — C2 domain-containing protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小2353 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4AC94
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168014-C2CD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C2CD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4AC94
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000168014-C2CD3/subcellular

![](https://images.proteinatlas.org/38552/2200_E9_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/38552/2200_E9_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/40433/1177_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/40433/1177_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/40433/2120_G1_16_red_green.jpg)
![](https://images.proteinatlas.org/40433/2120_G1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4AC94-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q4AC94 |
| SMART | SM00239; |
| UniProt Domain [FT] | DOMAIN 521..678; /note="C2 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 787..919; /note="C2 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 985..1147; /note="C2 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 1171..1339; /note="C2 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 1403..1533; /note="C2 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 1617..1745; /note="C2 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041" |
| InterPro | IPR037775;IPR057537;IPR000008;IPR035892; |
| Pfam | PF00168;PF25339; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168014-C2CD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP135 | Biogrid | false |
| OFD1 | Intact | false |
| PCM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
